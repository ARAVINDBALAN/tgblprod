import sqlite3
import pandas as pd
import os
import datetime, calendar

root = os.getcwd()


class SKU:
    def __init__(self,inp, n, ind,empty=0):
        if empty == 0:
            self.name = inp["MATERIAL"][n]
            self.blend = inp["Blend"][n]
            self.depolist = []
            for n in inp.index:
                if inp["MATERIAL"][n] == self.name:
                    self.depolist.append((inp["DEPO"][n], inp["L" + str(ind) + " Indent"][n]))
            self.quantity = 0
            for n in inp.index:
                if inp["MATERIAL"][n] == self.name:
                    self.quantity += inp["L" + str(ind) + " Indent"][n]
        else:
            self.name = ""
            self.blend = ""
            self.depolist = []
            self.quantity = 0


class Machine:
    def __init__(self, machname, dfobject, blend, hopper):
        self.name = machname
        self.skulist = []
        self.skuop = {}
        self.hopper = ""
        for n in dfobject.index:
            if dfobject["MACHINE / WORK CENTER "][n] == self.name:
                self.skulist.append(dfobject["SKU CODE"][n])
                for j in blend.index:
                    if blend["Material"][j] == dfobject["SKU CODE"][n]:
                        self.skuop[dfobject["SKU CODE"][n]] = [blend["Blend Code"][j], dfobject["OUTPUT PER SHIFT"][n],
                                                               dfobject["OUTPUT PER HOUR"][n]]
        for n in hopper.index:
            if hopper["Work Center Number"][n] == self.name:
                self.hopper = hopper["Hopper"][n]
        self.complist = []
        self.workqueue = {}

    def add2q(self, sku2add, date, shift, skulist, inp, n, ind):
        flag = 0
        cursku = SKU(inp, 1, 2, 1)
        for n in skulist:
            if n.name == sku2add:
                cursku = n
        print(cursku.name)
        if cursku.name != "":
            if self.workqueue[date][shift] != "":
                return False
            elif self.workqueue[date][shift] == "":
                if self.skuop[cursku.name][1] < inp["L"+str(ind)+" Indent"][n] and self.skuop[cursku.name][1] < cursku.quantity:
                    self.workqueue[date][shift] = [(cursku.name, self.skuop[cursku.name][1]),"N"]
                    cursku.quantity = cursku.quantity - self.skuop[cursku.name][1]
                    inp.at[n, "L"+str(ind)+" Indent"] -= self.skuop[cursku.name][1]
                    return True
                elif self.skuop[cursku.name][1] >= cursku.quantity or self.skuop[cursku.name][1] >= inp["L"+str(ind)+" Indent"][n]:
                    self.workqueue[date][shift] = [(cursku.name, cursku.quantity),"Y"]
                    cursku.quantity = 0
                    inp.at[n, "L" + str(ind) + " Indent"] -= cursku.quantity
                    return True
                else:
                    return False
        else:
            return False

    def initializeworkq(self, daysremaining):
        for m in daysremaining:
            self.workqueue[m] = ["", "", ""]

    def findbros(self, machlist):
        for n in machlist:
            if n.name != self.name and n.hopper == self.hopper:
                self.complist.append(n)

    def inbrolist(self, skuname):
        for m in self.complist:
            if skuname in m.skulist:
                return 1
        return 0


def getmach(machlist, skuname):
    retlist = []
    for n in machlist:
        if skuname in n.skulist:
            retlist.append(n)
    return retlist


def sortm(mlist, inp, n, w1, w2):
    cursku, curblend = inp["MATERIAL"][n], inp["Blend"][n]
    othersku = []
    notblend = []
    smcount = {}
    difcount = {}
    final = {}
    sortedm = []
    lastind = inp.index[len(inp.index) - 1]
    for m in mlist:
        for i in inp.index:
            if (i != n) and (inp["Blend"][i] == curblend) and (m.inbrolist(inp["MATERIAL"][i])):
                othersku.append(lastind - i)
        smcount[m] = len(othersku) * (sum(othersku))
        for i in inp.index:
            if (i not in othersku) and (not m.inbrolist(inp["MATERIAL"][i])):
                notblend.append(int(lastind - i))
        difcount[m] = (len(notblend)) * (sum(notblend))
    for m in mlist:
        final[m] = w1 * smcount[m] + w2 * difcount[m]
    while bool(final):
        maxi = -256
        largest = 0
        for m in mlist:
            # print(m.name)
            try:
                if final[m] > maxi:
                    maxi = final[m]
                    largest = m
            except KeyError:
                pass
        sortedm.append(largest)
        del final[largest]
    return sortedm


def findskuobj(skulist, skuname):
    for n in skulist:
        if n.name == skuname:
            return n
        else:
            df = {1: [1,2,3], 2: [3,5,6]}
            temp = SKU(df,1,1,empty=1)
            return temp


def schedule(excelpath, daysremaining, ind):
    # Connecting to DB
    connection = sqlite3.connect("pulp.db")
    db = connection.cursor()
    # Connecting to Excel
    inp = pd.read_excel(excelpath, "output_from_km_dimension.xlsx", usecols=[1, 2, 3, 4, 9, 10, 11, 29])
    # Adding remaining columns
    # for n in daysremaining:
    #     inp[str(n)+"balance"] = inp["L"+str(ind)+" Indent"]
    excelpath = pd.ExcelFile(root + "\\backend\\SKU wise - Machine wise capacities.xlsx")
    cols = [0, 1, 2, 4, 5, 6, 7]
    skumach = pd.read_excel(excelpath, "Sheet3", skiprows=5, usecols=cols)
    excelpath = pd.ExcelFile(root + "\\backend\\SKU - Blend Correlation, SKU details.xlsx")
    skublend = pd.read_excel(excelpath, "Sheet1", skiprows=1, usecols=[1, 2, 3])
    excelpath = pd.ExcelFile(root + "\\backend\\Hopper - machine correlation.xlsx")
    hopper = pd.read_excel(excelpath, "Sheet1", skiprows=1, usecols=[1, 2])
    skumach["MACHINE / WORK CENTER "] = pd.Series(skumach["MACHINE / WORK CENTER "]).fillna(method='ffill')
    machlist = []
    for n in skumach.index:
        temp = skumach["MACHINE / WORK CENTER "][n]
        if temp not in machlist:
            machlist.append(temp)
    temp = machlist
    machlist = []
    for n in temp:
        temp1 = Machine(n, skumach, skublend, hopper)
        temp1.initializeworkq(daysremaining)
        machlist.append(temp1)
    for n in machlist:
        n.findbros(machlist)
    availm = {}
    for n in inp.index:
        msku = getmach(machlist, inp["MATERIAL"][n])
        msku = sortm(msku, inp, n, 1, 1)
        availm[inp["MATERIAL"][n]] = msku
    skulist = []  # sorted list of SKU objects
    for n in inp.index:
        temp = SKU(inp, n, ind) # initializing new SKU object
        if len(skulist) == 0:
            skulist.append(temp)
        for i in skulist:
            if i.name != temp.name:
                skulist.append(temp)
                break
    for dates in daysremaining:
        for shift in range(3):
            for n in inp.index:
                cursku = inp["MATERIAL"][n]
                for m in availm[inp["MATERIAL"][n]]:
                    status = m.add2q(cursku, dates, shift, skulist, inp, n, ind)
                    print(m.name,m.workqueue, status)
                    if status:
                        break
                # print("Loop ended")
    for m in machlist:
        print(m.name, m.workqueue)

path = root + "\\backend\\output_from_km_dimension.xlsx"
year = 2019
month = 11
num_days = calendar.monthrange(year, month)[1]
days = [datetime.date(year, month, day) for day in range(1, num_days + 1)]
indent = 1
schedule(path, days, indent)
