import logging as l
import datetime
import playsound as pl
l.basicConfig(filename="log.log",level=l.DEBUG  , format= "%(asctime)s %(levelname)s %(name)s %(message)s")
def set_alarm():
    print(".............................Welocme................................")
    Alarm_time=(input("Enter Time in 24hr clock HH:MM:SS=\n"))
    l.info("time entred by user")
    Alarm_Date=(input("Enter Date in MM/DD/YY"))
    l.info("Date entred by user")
    Alarm_Hour=Alarm_time[0:2]
    l.info("SETTING ALARM HOUR")
    Alarm_Min=Alarm_time[3:5]
    l.info("SETTING ALARM MIN")
    Alarm_SEC=Alarm_time[6:8]
    l.info("SETTING ALARM SECOND")
    print("Setting up alarm.....")
    print("Alarm Set Successfully.....")
    while True:
        now = datetime.datetime.now()
        l.info("SETTING now = currunt time")
        current_hour = now.strftime("%H")
        l.info("current_hour = now.strftime(%H)")
        current_minute = now.strftime("%M")
        l.info("current_minute = now.strftime(%M)")
        current_seconds = now.strftime("%S")
        l.info("current_seconds = now.strftime(%S)")
        current_DAY = now.strftime("%D")
        l.info("current_DAY = now.strftime(%D)")

        l.info("current_DAY == Alarm_Date")
        if current_DAY == Alarm_Date:
            l.info("current_hour == Alarm_Hour")
            if current_hour == Alarm_Hour:
                l.info("current_minute == Alarm_Min")
                if current_minute == Alarm_Min:
                    l.info("current_seconds == Alarm_SEC")
                    if current_seconds == Alarm_SEC:
                        print("WAKE UP")
                        l.info("playing alarm tone")
                        pl.playsound('ok.mp3.mp3')
                        break
def exit():
    print("GOOD BYE....TRY AGAIN MY CODE")

if __name__ == "__main__":
    print("FOR SET ALARM ENTRE 1 \n" ,"FOR EXIT PRESS 2")
    Option=int(input("Entre your option to continue......= "))
    if Option == 1:
        set_alarm()
    elif Option == 2:
        exit()
    else:
        print("Please Entre valid Input")
