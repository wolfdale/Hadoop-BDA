#####################################################################
##  City codes Mapping
##    Delhi  01 / Chandigarh 02 /jaipur 03 /lucknow 04 /srinagar 05
##    mumbai 06 /pune 07 /banglore 08/ hydrabad 09 /kolkata 10
##    chennai 11
#####################################################################

import random
import sys


#Northern Cities Delhi/Chandigarh/Lucknow
def north_random(month):             
        if month==1:
                _max = random.randint(15,22)
                _min = random.randint(5,9)
        elif month==2:
                _max = random.randint(17,26)
                _min = random.randint(7,13)
        elif month==3:
                _max = random.randint(22,30)
                _min = random.randint(10,20)
        elif month==4:
                _max = random.randint(33,38)
                _min = random.randint(17,23)
        elif month==5:
                _max = random.randint(36,42)
                _min = random.randint(22,26)
        elif month==6:
                _max = random.randint(38,45)
                _min = random.randint(26,31)
        elif month==7:
                _max = random.randint(33,42)
                _min = random.randint(27,30)
        elif month==8:
                _max = random.randint(32,39)
                _min = random.randint(25,29)
        elif month==9:
                _max = random.randint(32,37)
                _min = random.randint(24,26)
        elif month==10:
                _max = random.randint(29,35)
                _min = random.randint(18,24)
        elif month==11:
                _max = random.randint(27,30)
                _min = random.randint(9,17)
        elif month==12:
                _max = random.randint(15,24)
                _min = random.randint(4,14)
        return (_max,_min)


#Extreme North Cities Srinagar       
def extreme_north_random(month):
        if month==1:
                _max = random.randint(15,22)
                _min = random.randint(5,9)
        elif month==2:
                _max = random.randint(17,26)
                _min = random.randint(7,13)
        elif month==3:
                _max = random.randint(22,30)
                _min = random.randint(10,20)
        elif month==4:
                _max = random.randint(33,38)
                _min = random.randint(17,23)
        elif month==5:
                _max = random.randint(36,42)
                _min = random.randint(22,26)
        elif month==6:
                _max = random.randint(38,45)
                _min = random.randint(26,31)
        elif month==7:
                _max = random.randint(33,42)
                _min = random.randint(27,30)
        elif month==8:
                _max = random.randint(32,39)
                _min = random.randint(25,29)
        elif month==9:
                _max = random.randint(32,37)
                _min = random.randint(24,26)
        elif month==10:
                _max = random.randint(29,35)
                _min = random.randint(18,24)
        elif month==11:
                _max = random.randint(27,30)
                _min = random.randint(9,17)
        elif month==12:
                _max = random.randint(15,24)
                _min = random.randint(4,14)
        return (_max,_min)


#Western Cities Jaipur
def west_random(month):
        if month==1:
                _max = random.randint(15,22)
                _min = random.randint(5,9)
        elif month==2:
                _max = random.randint(17,26)
                _min = random.randint(7,13)
        elif month==3:
                _max = random.randint(22,30)
                _min = random.randint(10,20)
        elif month==4:
                _max = random.randint(33,38)
                _min = random.randint(17,23)
        elif month==5:
                _max = random.randint(36,42)
                _min = random.randint(22,26)
        elif month==6:
                _max = random.randint(38,45)
                _min = random.randint(26,31)
        elif month==7:
                _max = random.randint(33,42)
                _min = random.randint(27,30)
        elif month==8:
                _max = random.randint(32,39)
                _min = random.randint(25,29)
        elif month==9:
                _max = random.randint(32,37)
                _min = random.randint(24,26)
        elif month==10:
                _max = random.randint(29,35)
                _min = random.randint(18,24)
        elif month==11:
                _max = random.randint(27,30)
                _min = random.randint(9,17)
        elif month==12:
                _max = random.randint(15,24)
                _min = random.randint(4,14)
        return (_max,_min)


#Mid Southern Random Mumbai/Pune
def mid_southern_random(month):
        if month==1:
                _max = random.randint(15,22)
                _min = random.randint(5,9)
        elif month==2:
                _max = random.randint(17,26)
                _min = random.randint(7,13)
        elif month==3:
                _max = random.randint(22,30)
                _min = random.randint(10,20)
        elif month==4:
                _max = random.randint(33,38)
                _min = random.randint(17,23)
        elif month==5:
                _max = random.randint(36,42)
                _min = random.randint(22,26)
        elif month==6:
                _max = random.randint(38,45)
                _min = random.randint(26,31)
        elif month==7:
                _max = random.randint(33,42)
                _min = random.randint(27,30)
        elif month==8:
                _max = random.randint(32,39)
                _min = random.randint(25,29)
        elif month==9:
                _max = random.randint(32,37)
                _min = random.randint(24,26)
        elif month==10:
                _max = random.randint(29,35)
                _min = random.randint(18,24)
        elif month==11:
                _max = random.randint(27,30)
                _min = random.randint(9,17)
        elif month==12:
                _max = random.randint(15,24)
                _min = random.randint(4,14)
        return (_max,_min)

        

#Southern Cities Banglore/Hydrabad       
def south_random(month):
        if month==1:
                _max = random.randint(15,22)
                _min = random.randint(5,9)
        elif month==2:
                _max = random.randint(17,26)
                _min = random.randint(7,13)
        elif month==3:
                _max = random.randint(22,30)
                _min = random.randint(10,20)
        elif month==4:
                _max = random.randint(33,38)
                _min = random.randint(17,23)
        elif month==5:
                _max = random.randint(36,42)
                _min = random.randint(22,26)
        elif month==6:
                _max = random.randint(38,45)
                _min = random.randint(26,31)
        elif month==7:
                _max = random.randint(33,42)
                _min = random.randint(27,30)
        elif month==8:
                _max = random.randint(32,39)
                _min = random.randint(25,29)
        elif month==9:
                _max = random.randint(32,37)
                _min = random.randint(24,26)
        elif month==10:
                _max = random.randint(29,35)
                _min = random.randint(18,24)
        elif month==11:
                _max = random.randint(27,30)
                _min = random.randint(9,17)
        elif month==12:
                _max = random.randint(15,24)
                _min = random.randint(4,14)
        return (_max,_min)

#Eastern Cities kolkata
def east_random(month):
        if month==1:
                _max = random.randint(15,22)
                _min = random.randint(5,9)
        elif month==2:
                _max = random.randint(17,26)
                _min = random.randint(7,13)
        elif month==3:
                _max = random.randint(22,30)
                _min = random.randint(10,20)
        elif month==4:
                _max = random.randint(33,38)
                _min = random.randint(17,23)
        elif month==5:
                _max = random.randint(36,42)
                _min = random.randint(22,26)
        elif month==6:
                _max = random.randint(38,45)
                _min = random.randint(26,31)
        elif month==7:
                _max = random.randint(33,42)
                _min = random.randint(27,30)
        elif month==8:
                _max = random.randint(32,39)
                _min = random.randint(25,29)
        elif month==9:
                _max = random.randint(32,37)
                _min = random.randint(24,26)
        elif month==10:
                _max = random.randint(29,35)
                _min = random.randint(18,24)
        elif month==11:
                _max = random.randint(27,30)
                _min = random.randint(9,17)
        elif month==12:
                _max = random.randint(15,24)
                _min = random.randint(4,14)
        return (_max,_min)



#Deep southern Cities Chennai
def deep_southern_random(month):
        if month==1:
                _max = random.randint(15,22)
                _min = random.randint(5,9)
        elif month==2:
                _max = random.randint(17,26)
                _min = random.randint(7,13)
        elif month==3:
                _max = random.randint(22,30)
                _min = random.randint(10,20)
        elif month==4:
                _max = random.randint(33,38)
                _min = random.randint(17,23)
        elif month==5:
                _max = random.randint(36,42)
                _min = random.randint(22,26)
        elif month==6:
                _max = random.randint(38,45)
                _min = random.randint(26,31)
        elif month==7:
                _max = random.randint(33,42)
                _min = random.randint(27,30)
        elif month==8:
                _max = random.randint(32,39)
                _min = random.randint(25,29)
        elif month==9:
                _max = random.randint(32,37)
                _min = random.randint(24,26)
        elif month==10:
                _max = random.randint(29,35)
                _min = random.randint(18,24)
        elif month==11:
                _max = random.randint(27,30)
                _min = random.randint(9,17)
        elif month==12:
                _max = random.randint(15,24)
                _min = random.randint(4,14)
        return (_max,_min)


def build_data ( month, start_year, end_year ):
        if month==(1 or 3 or 5 or 7 or 8 or 10 or 12):
                end=32
        else:
                end = 31
        fo=open("Weather_data "+str(month)+".txt","wb")
        for year in range (start_year, end_year+1):
                for city_code in range(1,12):
                        for day in range(1,end):
                                if city_code==(1 or 2 or 4):
                                        (_max,_min)=north_random(month)
                                elif city_code==5:
                                        (_max,_min)=extreme_north_random(month)
                                elif city_code==3:
                                        (_max,_min)=west_random(month)		
                                elif city_code==( 6 or 7):
                                        (_max,_min)=mid_southern_random(month)
                                elif city_code==(8 or 9):
                                        (_max,_min)=south_random(month)
                                elif city_code==10:
                                        (_max,_min)=east_random(month)
                                elif city_code==11:
                                        (_max,_min)=deep_southern_random(month)
                                fo.write(str(city_code)+" ")
                                fo.write(str(day)+ " ")
                                fo.write(str(month) + " ")
                                fo.write(str(year)+ " ")
                                fo.write(str(_max)+" ")
                                fo.write(str(_min)+ " ")
                                fo.write( "\n" )
        fo.close()


if __name__ == '__main__':
        month = sys.argv[1]
        start_year = sys.argv[2]
        end_year = sys.argv[3]
        build_data(int(month),int(start_year),int(end_year))
