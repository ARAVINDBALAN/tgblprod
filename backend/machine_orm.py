# Getting input from machine config
# Taking each input 

import pandas as pd
#machine
#name,producing sku, production rate , sku packet size
2019-10-202019-10-202019-10-202019-10-20
machine_orm_sheet = pd.read_excel(" ")




  #print(schedule_list)
    loopcount=0
    while(total_truck>0):
        if(loopcount==-1):
            break
        loopcount+=1
        # for i in range(len(datelist)):
        #     if(days[i].strftime("%A")=="Monday" or days[i].strftime("%A")=="Wednesday" or days[i].strftime("%A")=="Saturday"):
        #         for j in range(len(output_from_tenative)):
        #             if(output_from_tenative[j][0]=="KA01"):
        #                 total_truck-=1
        #                 schedule_list[datelist[i]][0]["KA01"]+=1
        #     if(days[i].strftime("%A")=="Tuesday" or days[i].strftime("%A")=="Wednesday"):
        #         for j in range(len(output_from_tenative)):
        #             if(output_from_tenative[j][0]=="GO01"):
        #                 total_truck-=1
        #                 schedule_list[datelist[i]][0]["GO01"]+=1
        for i in range(len(output_from_tenative)):
            if(output_from_tenative[i][1]<=0):
                continue
            if(loopcount>10000000):
                loopcount=-1
                break
            for j in range(len(datelist)):
                if(output_from_tenative[i][0] in map_list["Monday"] and days[j].strftime("%A")=="Monday"):
                    if(output_from_tenative[i][1]<=0):
                        break
                    total_truck-=1
                    print(total_truck)
                    output_from_tenative[i][1]-=1
                    for k in range(len(schedule_list[datelist[j]])):
                        if schedule_list[datelist[j]][k][0] == output_from_tenative[i][0]:
                            schedule_list[datelist[j]][k][1]+=1
                            break
                if(output_from_tenative[i][0] in map_list["Tuesday"]and days[j].strftime("%A")=="Tuesday"):
                    if(output_from_tenative[i][1]<=0):
                        break
                    total_truck-=1
                    output_from_tenative[i][1]-=1
                    for k in range(len(schedule_list[datelist[j]])):
                        if schedule_list[datelist[j]][k][0] == output_from_tenative[i][0]:
                            schedule_list[datelist[j]][k][1]+=1
                            break
                    #schedule_list[datelist[j]][0][output_from_tenative[i][0]]+=1
                if(output_from_tenative[i][0] in map_list["Wednesday"]and days[j].strftime("%A")=="Wednesday"):
                    if(output_from_tenative[i][1]<=0):
                        break
                    total_truck-=1
                    output_from_tenative[i][1]-=1
                    for k in range(len(schedule_list[datelist[j]])):
                        if schedule_list[datelist[j]][k][0] == output_from_tenative[i][0]:
                            schedule_list[datelist[j]][k][1]+=1
                            break
                    #schedule_list[datelist[j]][0][output_from_tenative[i][0]]+=1
                if(output_from_tenative[i][0] in map_list["Thursday"]and days[j].strftime("%A")=="Thursday"):
                    if(output_from_tenative[i][1]<=0):
                        break
                    total_truck-=1
                    output_from_tenative[i][1]-=1
                    for k in range(len(schedule_list[datelist[j]])):
                        if schedule_list[datelist[j]][k][0] == output_from_tenative[i][0]:
                            schedule_list[datelist[j]][k][1]+=1
                            break
                    #schedule_list[datelist[j]][0][output_from_tenative[i][0]]+=1
                if(output_from_tenative[i][0] in map_list["Friday"]and days[j].strftime("%A")=="Friday"):
                    if(output_from_tenative[i][1]<=0):
                        break
                    total_truck-=1
                    output_from_tenative[i][1]-=1
                    for k in range(len(schedule_list[datelist[j]])):
                        if schedule_list[datelist[j]][k][0] == output_from_tenative[i][0]:
                            schedule_list[datelist[j]][k][1]+=1
                            break
                    #schedule_list[datelist[j]][0][output_from_tenative[i][0]]+=1
    print(schedule_list)
    print(output_from_tenative)        



















    for i in range(len(output_from_tenative)):
        if(output_from_tenative[i][1]<=0):
           continue
        while(output_from_tenative[i][1]>0):
            for d in range(len(days)):
                if(days[d].strftime("%A")=="Monday" and output_from_tenative[i][0] in map_list["Monday"]):
                    if(output_from_tenative[i][i]>0):
                        output_from_tenative[i][1]-=1
                        schedule_list[str(days[d])][output_from_tenative[i][0]]+=1
                        print(output_from_tenative[i][0],schedule_list[str(days[d])][output_from_tenative[i][0]],schedule_list)
                        break
                elif(days[d].strftime("%A")=="Tuesday" and output_from_tenative[i][0] in map_list["Tuesday"]):
                    if(output_from_tenative[i][1]>0):
                        output_from_tenative[i][1]-=1
                        schedule_list[str(days[d])][output_from_tenative[i][0]]+=1
                        print(output_from_tenative[i][0],schedule_list[str(days[d])][output_from_tenative[i][0]],schedule_list)
                        break
                elif(days[d].strftime("%A")=="Wednesday" and output_from_tenative[i][0] in map_list["Wednesday"]):
                    if(output_from_tenative[i][1]>0):
                        output_from_tenative[i][1]-=1
                        print(output_from_tenative[i][1])
                        schedule_list[str(days[d])][output_from_tenative[i][0]]+=1
                        print(output_from_tenative[i][0],schedule_list[str(days[d])][output_from_tenative[i][0]],schedule_list)
                        break
                elif(days[d].strftime("%A")=="Thursday" and output_from_tenative[i][0] in map_list["Thursday"]):
                    if(output_from_tenative[i][1]>0):
                        output_from_tenative[i][1]-=1
                        print(output_from_tenative[i][1])
                        schedule_list[str(days[d])][output_from_tenative[i][0]]+=1
                        print(output_from_tenative[i][0],schedule_list[str(days[d])][output_from_tenative[i][0]],schedule_list)
                        break
                elif(days[d].strftime("%A")=="Friday" and output_from_tenative[i][0] in map_list["Friday"]):
                    if(output_from_tenative[i][1]>0):
                        output_from_tenative[i][1]-=1
                        print(output_from_tenative[i][1])
                        t=schedule_list[str(days[d])]
                        t[output_from_tenative[i][0]]+=1
                        print(output_from_tenative[i][0],schedule_list[str(days[d])][output_from_tenative[i][0]],schedule_list)
                        break


