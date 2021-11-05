# -*- encoding: utf-8 -*-
import  datetime
import os

list=[]
for i in range(23):
    val="20"+str(i//12+20).zfill(2)+"/"+str(i%12+1)+"/1"
    list.append(val)

print(list)
time_dict={}
for i in range(len(list)):
    time_dict[list[i]]=0
# print(time_dict)
address_dict={}
address_list=['Inner West (A)', 'Ku-ring-gai (A)', 'Hunters Hill (A)', 'Canada Bay (A)', 'Strathfield (A)', 'Parramatta (C)', 'The Hills Shire (A)', 'Cumberland (A)', 'Liverpool (C)', 'Canterbury-Bankstown (A)', 'Camden (A)', 'Penrith (C)', 'Blacktown (C)', 'Wollondilly (A)', 'Tweed (A)', 'Oberon (A)', 'Northern Beaches (A)', 'Burwood (A)', 'Bayside (A)', 'Georges River (A)', 'Randwick (C)', 'Willoughby (C)', 'Ryde (C)', 'Fairfield (C)', 'Sydney (C)', 'Sutherland Shire (A)', 'Maitland (C)', 'Campbelltown (C) (NSW)', 'Bathurst Regional (A)', 'Hornsby (A)', 'Newcastle (C)', 'Queanbeyan-Palerang Regional (A)', 'Central Coast (C) (NSW)', 'Bega Valley (A)', 'Snowy Valleys (A)', 'Wagga Wagga (C)', 'Blue Mountains (C)', 'North Sydney (A)', 'Waverley (A)', 'Lake Macquarie (C)', 'Armidale Regional (A)', 'Lismore (C)', 'Bourke (A)', 'Woollahra (A)', 'Hawkesbury (C)', 'Singleton (A)', 'Liverpool Plains (A)', 'Inverell (A)', 'Wollongong (C)', 'Shoalhaven (C)', 'Wingecarribee (A)', 'Lane Cove (A)', 'Mosman (A)', 'Bellingen (A)', 'Port Stephens (A)', 'Hilltops (A)', 'Port Macquarie-Hastings (A)', 'Byron (A)', 'Balranald (A)', 'Kempsey (A)', 'Shellharbour (C)', 'Cessnock (C)', 'Tamworth Regional (A)', 'Mid-Coast (A)', 'Upper Hunter Shire (A)', 'Kyogle (A)', 'Eurobodalla (A)', 'Yass Valley (A)', 'Richmond Valley (A)', 'Glen Innes Severn (A)', 'Kiama (A)', 'Edward River (A)', 'Cootamundra-Gundagai Regional (A)', 'Nambucca (A)', 'Ballina (A)', 'Snowy Monaro Regional (A)', 'Lithgow (C)', 'Blayney (A)', 'Mid-Western Regional (A)', 'Cabonne (A)', 'Goulburn Mulwaree (A)', 'Greater Hume Shire (A)', 'Coolamon (A)', 'Orange (C)', 'Muswellbrook (A)', 'Narrabri (A)', 'Warrumbungle Shire (A)', 'Dubbo Regional (A)', 'Coffs Harbour (C)', 'Clarence Valley (A)', 'Albury (C)', 'Narrandera (A)', 'Murrumbidgee (A)', 'Leeton (A)', 'Moree Plains (A)', 'Walgett (A)', 'Temora (A)', 'Forbes (A)', 'Dungog (A)', 'Griffith (C)', 'Uralla (A)', 'Correctional settings', 'Walcha (A)', 'Tenterfield (A)', 'Upper Lachlan Shire (A)', 'Lachlan (A)', 'Cowra (A)', 'Coonamble (A)', 'Gwydir (A)', 'Cobar (A)', 'Parkes (A)', 'Broken Hill (C)', 'Gunnedah (A)', 'Bland (A)', 'Narromine (A)', 'Federation (A)', 'Central Darling (A)', 'Wentworth (A)', 'Junee (A)', 'Carrathool (A)', 'Bogan (A)', 'Warren (A)', 'Weddin (A)', 'Lockhart (A)', 'Berrigan (A)', 'Brewarrina (A)', 'Hay (A)', 'Murray River (A)', 'Gilgandra (A)']
dp={}
print(address_list)
for i in list:
    dp[i] = {}
    for j in address_list:
        dp[i][j] = 0
print(dp)
xlist=[0]*4
ylist=[0]*4
zlist=[0]*4
alist=[0]*4
blist=[0]*4
tmlist=["2020/8/2","2020/1/1","2020/6/1","2021/3/15"]
tm1list=[""]*4
tm2list=[""]*4
tm3list=[""]*4
for i in range(len(tmlist)):
    tm1list[i]=datetime.datetime.strptime(tmlist[i],"%Y/%m/%d")-datetime.timedelta(days=30)
    tm2list[i] =datetime.datetime.strptime(tmlist[i], "%Y/%m/%d") - datetime.timedelta(days=15)
    tm3list[i] = datetime.datetime.strptime(tmlist[i], "%Y/%m/%d") + datetime.timedelta(days=15)

print("+++++++++=")
print(tm1list)
print(tm2list)
print(tm3list)
#datatest=datetime.datetime.strptime("2020/1/2","%Y/%m/%d")
with open(r"C:\Users\Administrator\PycharmProjects\helloflask\venv\Include\pcr_testing_table1_location_agg.csv") as inputfile:
    # print(inputfile.readline())
    for index,line in enumerate(inputfile):
        if index >0   :
            arraytemp=line.split(',')
            num=len(arraytemp)
            if num==7 :
                datetemp=datetime.datetime.strptime(arraytemp[0],"%Y/%m/%d")
                count=int(arraytemp[6])
                for i in range(4):
                    if tm1list[i] <= datetemp < tm2list[i]:
                        xlist[i] += count
                    if tm2list[i] <= datetemp < datetime.datetime.strptime(tmlist[i],"%Y/%m/%d"):
                        ylist[i] += count
                    if datetime.datetime.strptime(tmlist[i],"%Y/%m/%d") <= datetemp < tm3list[i]:
                        zlist[i] += count
                #print(time_dict[list[tn-1]])
        # else:
        #     print(line)
        #     print(line.split(',')[6])
    inputfile.close()

for i in range(4):
    if xlist[i]!=0:
        alist[i]=ylist[i]/xlist[i]
    if ylist[i]!=0:
        blist[i]=zlist[i]/ylist[i]
print(alist)
print(blist)
print(xlist)
print(ylist)
print(zlist)

print("---------")
for i in range(4):
    print(str(blist[i]-alist[i]))
print("====1======")
print(time_dict)
print(address_dict)
print("=====2=====")
