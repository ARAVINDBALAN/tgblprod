import pandas as pd
import os
#import testui 
import math
import datetime
from database import select_date_from_table,insert_into_tenative
#/home/aravind/.local/bin/pyinstaller
#inputs are main data after stage one and no of days_remaining
# here datelist is in string converting to datetime object in function() 


killdill = 10
def ddd(killdill):
    print(killdill)

truck_capacity = {160:[16000,28560000000],145:[14500,58540000000],90:[9000,25870000000],65:[6500,35000000000]}
truck_pref=[["KL01",160],["KL01",90],["AP01",65],["AP03",65],["GO01",160],["KK01",160],["KK02",160],["KK02",145],["TN01",160],["TN02",90],["TN03",90],["MH01",65],["MH02",145],["MH04",160]]
depo_list=["KL01","AP01","AP03","GO01","KK01","KK02","TN01","TN02","TN03","MH01","MH02","MH04"]
depo_qt=[None]
'''function to check if indent is from l1 or l2 when scheduling '''


def tenative(datelist,excelpath):
    no_of_trucks_volume = 0
    remaining_trucks_volume = 0
    no_of_trucks_weight = 0
    remaining_trucks_weight = 0
    flag=0
    #output for get_sku_with_km_sku
    path = pd.ExcelFile(excelpath)
    df = pd.read_excel(path)
    depo = list(df["DEPO"].unique())
    weight = []
    volume = []

    day = str(datelist[0])[-2:]
    if(int(day) >= 16):
        '''checking if selected dates is in L2 INDENT '''
        g_wt=df.groupby("DEPO")["L2 Gross weight"].sum()
        v_wt = df.groupby("DEPO")["L1 volume "].sum()
        print(g_wt,v_wt)
    else:
        '''checking if selected dates is in L1 INDENT '''
        g_wt=df.groupby("DEPO")["L1 Gross weight"].sum()
        v_wt = df.groupby("DEPO")["L1 volume "].sum()
        print(g_wt,v_wt)

       
    #volume
    for i in depo:
            print(i)
    #1st truck
            iter=0
            iter_flag=0

            #to get truck capacity
            truck_cap = 0
            while(iter_flag==0):
                if i==truck_pref[iter][0]:
                    truck_cap=truck_pref[iter][1]
                    iter_flag=1
                iter=iter+1

            #calculate no of truck max weight wise
            no_of_trucks_volume=int(v_wt.get(i)/truck_capacity[truck_cap][1])
           

            # calculate no of truck remaining weight wise
            remaining_trucks_volume_temp=v_wt.get(i)-(no_of_trucks_volume * truck_capacity[truck_cap][1])
            
    #2nd truck
            if i == truck_pref[iter][0]:
                truck_cap = truck_pref[iter][1]
                remaining_trucks_volume = remaining_trucks_volume_temp / truck_capacity[truck_cap][1]
                rem_temp=v_wt.get(i)-(remaining_trucks_volume * truck_capacity[truck_cap][1])
                if rem_temp>0:
                    remaining_trucks_volume = remaining_trucks_volume + 1

    #case where 2nd truck option unavailable but still more sku to transport
            else:
                if remaining_trucks_volume_temp>0:
                    no_of_trucks_volume = no_of_trucks_volume + 1
            print(math.ceil(no_of_trucks_volume))
            volume.append([i,math.ceil(no_of_trucks_volume)])



    #weight
    for i in depo:
            print(i)
    #1st truck
            iter=0
            iter_flag=0

            #to get truck capacity
            while(iter_flag==0):
                if i==truck_pref[iter][0]:
                    truck_cap=truck_pref[iter][1]
                    iter_flag=1
                iter=iter+1

            #calculate no of truck max weight wise
            no_of_trucks_weight=int(g_wt.get(i)/truck_capacity[truck_cap][0])
           

            # calculate no of truck remaining weight wise
            remaining_trucks_weight_temp=g_wt.get(i)-(no_of_trucks_weight * truck_capacity[truck_cap][0])
            
    #2nd truck
            if i == truck_pref[iter][0]:
                truck_cap = truck_pref[iter][1]
                remaining_trucks_weight = remaining_trucks_weight_temp / truck_capacity[truck_cap][0]
                rem_temp=g_wt.get(i)-(remaining_trucks_weight * truck_capacity[truck_cap][0])
                if rem_temp>0:
                    remaining_trucks_weight = remaining_trucks_weight + 1

    #case where 2nd truck option unavailable but still more sku to transport
            else:
                if remaining_trucks_weight_temp>0:
                    no_of_trucks_weight = no_of_trucks_weight + 1
            print(math.ceil(no_of_trucks_weight))
            weight.append([i,math.ceil(no_of_trucks_weight)])
    #print(weight,volume)
    return [weight,volume]





#print(a)


def volume_or_weight_map(wevol):
    weight = wevol[0]
    volume = wevol[1]
    true_list = []
    for i in range(len(volume)):
        if(volume[i][1]>weight[i][1]):
            temp = volume[i].append("volume")
            true_list.append(volume[i])
            
        else:
            temp = weight[i].append("weight")
            true_list.append(weight[i])
    return true_list



#volume_or_weight_map(a)






''' function to schedule trucks according to week , odd or even days based algorithm  '''
''' moday,tuesday , wednesy - karnataka
    mon,teus - except kerala
    wednesday - goa,maharashtra,andra
    thursday - tamil 
    tuesday,fri = kerala
    '''
schedule_list = {}
depo_truck={"KL01":0,"AP01":0,"AP03":0,"GO01":0,"KK01":0,"KK02":0,"TN01":0,"TN02":0,"TN03":0,"MH01":0,"MH02":0,"MH04":0}
map_list = {"Monday":["AP01","AP03","GO01","KK01","KK02","TN01","TN02","TN03","MH01","MH02","MH04"],
            "Tuesday":["AP01","AP03","GO01","KK01","KK02","TN01","TN02","TN03","MH01","MH02","MH04"],
            "Wednesday":["GO01","MH01","MH02","MH04"],
            "Thursday":["TN01","TN02","TN03"],
            "Friday":["KL01"]
            }


depo_day_map ={
	"KL01":["Monday","Tuesday","Wednesday","Thursday","Friday"],
	"AP01":["Monday","Tuesday","Wednesday"],
	"TN01":["Tuesday","Wednesday","Thursday"],
	"TN02":["Monday","Wednesday"],
	"TN03":["Monday","Tuesday"],
	"GO01":["Tuesday","Wednesday"],
	"KK01":["Monday","Tuesday","Friday"],
    "KK02":["Wednesday","Monday"],
	"AP03":["Wednesday"],
	"MH01":["Tuesday"],
    "MH02":["Wednesday"],
    "MH04": ["Tuesday"],
}



dummy  = {}


# code written as based on daterange 
# def schedule_two_week_truck(datelist,output_from_tenative,depo_truck):
#     days=[0]*len(datelist)
#     for i in range(len(datelist)):
#         d = datelist[i].split('-')
#         date = datetime.date(int(d[0]),int(d[1]),int(d[2]))
#         days[i] = date
#     #for dno in range(len(depo_truck_list)):
#     total_truck = 0 
#     for i in range(len(output_from_tenative)):
#         total_truck+=output_from_tenative[i][1]
#     print(total_truck)
#     for i in range(len(datelist)):
#         schedule_list[datelist[i]]=depo_truck
#     #print(schedule_list)

    
#     print(schedule_list)

''''
take a depo , copy datelist for evry depo , pop and delete for count of truck for depos
 '''


def schedule_two_week_truck(datelist,output_from_tenative,depo_truck,depo_list):
    datelistforschedule = []
    for i in datelist:
        d = i.split('-')
        print(d)
        i = datetime.date(int(d[0]),int(d[1]),int(d[2]))
        datelistforschedule.append(i)
    print(datelistforschedule)
    for depos in output_from_tenative:
        
        datas = datelistforschedule[:]
        truck_no = depos[1]
        print(truck_no)
        for d in datas:
            if(truck_no>0):
                if(d.strftime("%A") in depo_day_map[depos[0]]):
                    depos.append(str(d))
                    datas.remove(d)
                    truck_no-=1
                
    return output_from_tenative


def sort_by_date(opfromschedule,datelist,count):
    datedict ={}
    n = count
    for i in datelist:
        datedict[i] = []
    while n > 0:
        for i in datelist:
            for depo in opfromschedule:
                if i in depo:
                    datedict[i].append(depo[0])
                    count -= 1

    return datedict


#b=[['AP01', 2, 'weight'], ['TN01', 4, 'volume'], ['TN02', 5, 'weight'], ['TN03', 2, 'weight'], ['KL01', 7, 'volume'], ['GO01', 2, 'volume'], ['KK01', 16, 'volume'], ['KK02', 5, 'volume'], ['AP03', 1, 'weight'], ['MH01', 1, 'weight']]
#c = volume_or_weight_map(a)

#print("schedule",c)

datesfromtable = select_date_from_table("working_days")
scheduledates = []
for i in datesfromtable:
    scheduledates.append(str(i[0]))
print(scheduledates)

#b=schedule_two_week_truck(scheduledates,c,depo_truck,depo_list)
#datedict = sort_by_date(b,scheduledates)

# for i in datedict:
#     #print("xfgfgjfjb")
#     temp_to_database = [str(i),str(datedict[i])]
#     insert_into_tenative(temp_to_database)
