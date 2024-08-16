import os
import time
import datetime

#if this is True then the Server is On Else Off

MinecraftServerStatus = False

def main():
    now = datetime.datetime.now()
    print(f"Time is {now.hour}:{now.minute}")

    if(now.hour == 0) and (now.minute == 50):
        TenMinuteWarningMinecraft()
    
    if(now.hour == 1) and (now.minute == 0) and (MinecraftServerStatus != False):
        CloseMinecraftServer()
    
    if ((now.hour >= 1) and (now.minute > 5)) and (MinecraftServerStatus == False):
        StartMinecraftServer()


    


    time.sleep(60)
    main()


def TenMinuteWarningMinecraft():
    os.system("tmux new -t mine")
    os.system("/say Server shuts down in 10 minutes")
    os.system("tmux detach")


def StartMinecraftServer():
    os.system("tmux new -t mine")
    os.system("cd Minecraft-Server")
    os.system("java -Xmx12G -jar fabric-server-mc.1.19.2-loader.0.15.11-launcher.1.0.1.jar nogui")

    f = open("scripts/Dbot/DiscordBot/MCStatus.txt", "w+")

    f.write("y")

    f.close()

    MinecraftServerStatus = True

    os.system("tmux detach")



def CloseMinecraftServer():

    os.system("tmux new -t mine")
    os.system("/stop")

    MinecraftServerStatus = False

    f = open("scripts/Dbot/DiscordBot/MCStatus.txt", "w+")

    f.write("n")

    f.close()

    os.system("tmux detach")
    


if __name__ == ("__main__"):
    main()