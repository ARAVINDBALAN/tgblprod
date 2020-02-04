"""The function has to be called with three parameters (ind=4, excelpath, daysremaining)
    Indent is by default assigned to 4 """

import pandas as pd
import datetime
import sqlite3
import calendar
import os

# Global Variables
connection = sqlite3.connect("pulp.db")
kmtrackdb = "sku_tab"
shifts = ["S1", "S2", "S3"]
shift_time = 8
it = 0


class UndefinedIndentError(Exception):
    pass


class UndefinedHopperError(Exception):
    pass


class MachineNotFoundForSKU(Exception):
    pass


class Flags:
    def __init__(self):
        self.indentoverload = False
        self.schedulingfail = False
        self.sameflag = False
        self.overtime = False
        self.complete = False
        self.machinefound = False
        self.skumachinenotfound = False


system = Flags()


class SKU:
    def __init__(self, df, index, ind):
        self.skucode = df["MATERIAL"][index]
        self.depo = df["DEPO"][index]
        self.quantity = float(df[ind][index])
        self.machines_comp = self.find_machines()
        self.blend = df["Blend"][index]
        # self.desc = df["MATERIAL DESCRIPTION"][index]
        self.blend_desc = df["Blend Description"][index]
        self.changeover = False

    def find_machines(self):
        temp_df = pd.read_sql_query("select machine_id from machines where sku_code='" + self.skucode + "'", connection)
        machine_list = []
        for i in temp_df.index:
            machine_list += [temp_df["machine_id"][i]]
        return machine_list


class Mach:
    def __init__(self, df, hop_path, name):
        self.machine_id = name
        self.sku_dict = self.get_sku()
        self.schedule = {}
        self.hopper = "0"
        self.find_hopper(hop_path)
        self.comach = []
        self.current_blend = ""

    def get_sku(self):
        temp_df = pd.read_sql_query(
            "select sku_code,rate_hr,case_shift from machines where machine_id='" + self.machine_id + "'", connection)
        sku_dict = {}
        for i in temp_df.index:
            sku_dict[temp_df["sku_code"][i]] = [temp_df["rate_hr"][i], temp_df["case_shift"][i]]
        return sku_dict

    def setupsched(self, daysremaining):
        for i in daysremaining:
            self.schedule[i] = {"S1": [], "S2": [], "S3": []}

    def find_hopper(self, hopper_path):
        df = pd.read_excel(hopper_path, usecols=[1, 2], skiprows=1)
        comach = []
        try:
            for i in df.index:
                # print(df["Work Center Number"][i], str(self.machine_id),type(self.machine_id))
                if df["Work Center Number"][i] == self.machine_id:
                    self.hopper = df["Hopper"][i]
                    break
            if self.hopper == "0":
                raise UndefinedHopperError
        except UndefinedHopperError:
            print("Machine Hopper Co-relation not defined")
            print("Machine name is:" + self.machine_id)
            exit(2)

    def find_comach(self, machine_list):
        for j in machine_list:
            if j.hopper == self.hopper and j.machine_id != self.machine_id:
                self.comach += [j]


class Depo:
    def __init__(self, df, index, indent):
        self.name = df["DEPO"][index]
        self.skulist = {}
        self.skulist = self.getskulist(df, indent)
        self.truck2depo = []

    def getskulist(self, df, indent):
        retdict = {}
        for i in df.index:
            pass
        return retdict


def notindepolist(name, depo_list):
    for i in depo_list:
        if i.name == name:
            return False
        else:
            continue
    return True


def find_sku(name, obj_list, deponame):
    for i in obj_list:
        if i.skucode == name and i.depo == deponame:
            return i


def find_machine(name, obj_list):
    for i in obj_list:
        if i.machine_id == name:
            return i


def allskunotdone(slist):
    for i in slist:
        if i.quantity != 0:
            return True
    return False


def freeinmach(mobj, sku, day, extra, shift):
    if sku.skucode not in mobj.sku_dict.keys():
        return False
    temp = mobj.schedule
    if not extra:
        if len(temp[day][shifts[shift - 1]]) < 2 and hours_remaining(mobj, day, shift) < 8:
            return True
        else:
            return False
    else:
        if len(temp[day][shifts[shift - 1]]) < 3 and hours_remaining(mobj, day, shift) < 8:
            return True
        else:
            return False


def hours_remaining(machine_obj, today, shift):
    hours = 0
    for i in machine_obj.schedule[today][shifts[shift - 1]]:
        hours += i[2]
    return hours


def add_to_schedule(skuobj, machines, tschedule, today, shift, extra=False):
    cur_machine = 0
    system.machinefound = False
    curblend = skuobj.blend
    if skuobj.quantity == 0:
        print("No intent remaining")
        system.skumachinenotfound = False
        return False, False, True
    flag = False
    if not extra:
        for i in machines:
            if (len(i.schedule[today]["S1"]) == 2 and len(i.schedule[today]["S2"]) == 2) or (
                    hours_remaining(i, today, 1) == 8 and hours_remaining(i, today, 2) == 8):
                flag = True
            else:
                flag = False
                break
        if flag:
            return False, True, False
    elif extra:
        for i in machines:
            if (len(i.schedule[today]["S1"]) == 3 and len(i.schedule[today]["S2"]) == 3 and len(
                    i.schedule[today]["S3"]) == 3) or (
                    hours_remaining(i, today, 1) == 8 and hours_remaining(i, today, 2) == 8 and hours_remaining(i,
                                                                                                                today,
                                                                                                                3) == 8):
                flag = True
            else:
                flag = False
                break
        if flag:
            return False, True, False
    if not extra:
        for i in machines:
            if len(i.schedule[today][shifts[shift]]) == 2 or hours_remaining(i, today, shift) == 8:
                flag = True
            else:
                flag = False
                break
        if flag:
            return True, False, False
    elif extra:
        for i in machines:
            if len(i.schedule[today][shifts[shift]]) == 3 or hours_remaining(i, today, shift) == 8:
                flag = True
            else:
                flag = False
                break
        if flag:
            return True, False, False
    for i in machines:
        status = freeinmach(i, skuobj, today, extra, shift)
        if status:
            system.machinefound = True
            cur_machine = i
            break
    if system.machinefound:
        h = hours_remaining(cur_machine, today, shift)
        global it
        print("h", it, ":", h)
        it += 1
        if h == 0:
            max_output = 8 * int(cur_machine.sku_dict[skuobj.skucode][0])
            print("max1:", max_output)
            if skuobj.quantity >= max_output:
                cur_machine.schedule[today][shifts[shift - 1]] += [(skuobj, max_output, 8)]
                skuobj.quantity = skuobj.quantity - max_output
                print(cur_machine.machine_id, cur_machine.schedule[today])
                return False, False, False
            else:
                max_output = skuobj.quantity
                print("max2:", max_output)
                hours = max_output / int(cur_machine.sku_dict[skuobj.skucode][0])
                cur_machine.schedule[today][shifts[shift - 1]] += [(skuobj, max_output, hours)]
                print(cur_machine.machine_id, cur_machine.schedule[today])
                skuobj.quantity = 0
                return False, False, True
        elif 0 < h < 8:
            max_output = (8 - h) * int(cur_machine.sku_dict[skuobj.skucode][0])
            print("max3:", max_output)
            if skuobj.quantity >= max_output:
                cur_machine.schedule[today][shifts[shift - 1]] += [(skuobj, max_output, 8 - h)]
                skuobj.quantity = skuobj.quantity - max_output
                print(cur_machine.machine_id, cur_machine.schedule[today])
                return False, False, False
            else:
                max_output = skuobj.quantity
                print("max4:", max_output)
                hours = max_output / int(cur_machine.sku_dict[skuobj.skucode][0])
                cur_machine.schedule[today][shifts[shift - 1]] += [(skuobj, max_output, hours)]
                print(cur_machine.machine_id, cur_machine.schedule[today])
                skuobj.quantity = 0
                return False, False, True
        else:
            return False, False, True
    else:
        for i in machines:
            if skuobj.skucode in i.sku_dict.keys():
                system.skumachinenotfound = False
        if system.skumachinenotfound:
            print("Machine not configured for SKU:" + skuobj.skucode)
            system.skumachinenotfound = True
            return False, False, True
        else:
            return False, False, True


def scheduler(excelpath, daysremaining, mac_hop_path, ind=4):
    try:
        if ind == 1:
            ind = "L1 Indent"
        elif ind == 2:
            ind = "L2 Indent"
        else:
            raise UndefinedIndentError
    except UndefinedIndentError:
        print("Undefined Indent was passed. Input Error")
        exit(1)
    inp = pd.read_excel(excelpath, "output_from_km_dimension.xlsx", usecols=[1, 2, 3, 4, 9, 10, 11, 29])
    sku_in_indent = []  # initialization of SKU objects
    indices = inp.index
    for i in indices:  # creating each object
        new_sku = SKU(inp, i, ind)
        sku_in_indent += [new_sku]
    machine_list = []  # initialization of machine list
    machine_codes = []
    machine = pd.read_sql_query("select * from machines", connection)  # reading from db to df
    for i in machine.index:  # creating a list of machines
        if machine["machine_id"][i] not in machine_codes:
            machine_codes += [machine["machine_id"][i]]
    for i in machine_codes:
        temp = Mach(machine, mac_hop_path, i)
        temp.setupsched(daysremaining)
        machine_list += [temp]
    for i in machine_list:
        i.find_comach(machine_list)
    depo_list = []
    for i in indices:
        if notindepolist(inp["DEPO"][i], depo_list):
            new_depo = Depo(inp, i, ind)
            depo_list += [new_depo]
    # for i in machine_list:
    #     i.setupsched(daysremaining)  # Initializing machine schedule
    tschedule = {}
    for i in daysremaining:
        tschedule[i] = {}
    end = len(daysremaining)
    prevquantlist = []
    first = True
    system.sameflag = False
    while allskunotdone(sku_in_indent):
        size = len(sku_in_indent)
        i = 0
        if not first:
            system.sameflag = True
        while i < size and len(prevquantlist) > 0:
            if prevquantlist[i] != sku_in_indent[i].quantity:
                system.sameflag = False
                break
            i += 1
        if system.sameflag:
            for i in sku_in_indent:
                if i.quantity != 0:
                    print("Could not process entire indent")
                    system.indentoverload = True
                    system.overtime = True
                    break
        if system.indentoverload:
            break
        curindex = 0
        cur_sku = inp["MATERIAL"][indices[curindex]]
        cur_depo = inp["DEPO"][indices[curindex]]
        cur_sku = find_sku(cur_sku, sku_in_indent, cur_depo)
        i = 0
        shift = 1
        size = len(indices)
        loopcount = 0
        while i < end:
            loopcount += 1
            if loopcount > 100000:
                print("TLE")
                break
            today = daysremaining[i]
            # print(cur_sku.skucode, curindex, inp.index)
            shiftover, dayover, nextsku = add_to_schedule(cur_sku, machine_list, tschedule, today, shift)
            first = False
            if shiftover:
                newshift = ((shift + 1) % 2) + 1
                if shift == 2 and newshift == 1:
                    i += 1
            elif nextsku:
                if system.skumachinenotfound:
                    inp.drop(inp.index[curindex], inplace=True)
                    inp.reset_index(drop=True)
                    indices = inp.index
                    size = len(indices)
                    system.skumachinenotfound = False
                curindex = (curindex + 1) % size
                cur_sku = inp["MATERIAL"][indices[curindex]]
                cur_depo = inp["DEPO"][indices[curindex]]
                cur_sku = find_sku(cur_sku, sku_in_indent, cur_depo)
            elif dayover:
                i += 1
                shift = 1
                curindex = 0
        prevquantlist = []
        for i in sku_in_indent:
            prevquantlist += [i.quantity]
    first = True
    system.sameflag = False
    if (not system.complete) and system.indentoverload:
        while allskunotdone(sku_in_indent):
            print("mainloop")
            size = len(sku_in_indent)
            i = 0
            if first:
                system.sameflag = True
            while i < size and len(prevquantlist) > 0:
                if prevquantlist[i] != sku_in_indent[i].quantity:
                    system.sameflag = False
                    break
                i += 1
            if system.sameflag:
                for i in sku_in_indent:
                    if i.quantity != 0:
                        print("Could not process entire indent with extra")
                        system.indentoverload = True
                        system.schedulingfail = True
                        break
            if system.schedulingfail:
                print("System Failure")
                break
            curindex = 0
            cur_sku = inp["MATERIAL"][indices[curindex]]
            cur_sku = find_sku(cur_sku, sku_in_indent)
            shift = 1
            i = 0
            while i < end:
                today = daysremaining[i]
                ml = machine_list
                shiftover, dayover, nextsku = add_to_schedule(cur_sku, ml, tschedule, today, shift, True)
                first = False
                if shiftover:
                    shift = ((shift + 1) % 3) + 1
                elif nextsku:
                    if system.skumachinenotfound:
                        inp.drop(inp.index[curindex], inplace=True)
                        inp.reset_index(drop=True)
                        indices = inp.index
                        size = len(indices)
                        system.skumachinenotfound = False
                    curindex = (curindex + 1) % size
                    cur_sku = inp["MATERIAL"][indices[curindex]]
                    cur_sku = find_sku(cur_sku, sku_in_indent)
                elif dayover:
                    i += 1
                    shift = 1
                    curindex = 0
            prevquantlist = []
            for i in sku_in_indent:
                prevquantlist += [i.quantity]
    for i in machine_list:
        print(i.machine_id)
        for j in daysremaining:
            print(j.day, "-", j.month, "-", j.year, ":", i.schedule[j])
    output = {}
    f = open("schedule.xlsx","w+")
    for i in daysremaining:
        output = {}
        for j in machine_list:
            for k in j.schedule[i]:
                for m in j.schedule[i][k]:
                    m


# commented here as it doesnot compile it executes as sch30 is imported 

# root = os.getcwd()
# path = root + "\\backend\\output_from_km_dimension.xlsx"
# year = 2019
# month = 11
# num_days = calendar.monthrange(year, month)[1]
# days = [datetime.date(year, month, day) for day in range(1, num_days + 1)]
# indent = 1
# hoppath = root + "\\backend\\Hopper - machine correlation.xlsx"
# scheduler(path, days, hoppath, indent)
