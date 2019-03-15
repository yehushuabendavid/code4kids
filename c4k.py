import pygame as pg
import socket as sk
import sys , time
import os, os.path

pg.init();
mScreen = pg.display.set_mode((1280, 720))
pg.display.set_caption("Code for Kids")
pg.font.init()
myfont = pg.font.SysFont('Comic Sans MS', 30)
txt = myfont.render('Start', False, (0, 0, 0))

framepos = 0
framedir = 1;
anime = {}
anime["GirlRespire"] = {    "start" : 203,    "stop"  :229 , "dir" : 2}
anime["GirlDance"] = {    "start" : 1,    "stop"  :202 , "dir" : 1}

anime["ManRespire"]= {    "start" : 2065,    "stop"  :2084 , "dir" : 2}
anime["ManDance"] =  {    "start" : 230,    "stop"  :500 , "dir" : 1}
anime["ManDance2"] = {    "start" : 700,    "stop"  :800 , "dir" : 2}
anime["ManDance3"] = {    "start" : 865,    "stop"  :1200 , "dir" : 2}
anime["ManDance4"] = {    "start" : 1220,    "stop"  :1400 , "dir" : 2}
anime["ManDance5"] = {    "start" : 1615,    "stop"  :1800 , "dir" : 2}
anime["ManShoot"] =  {    "start" : 1820,    "stop"  :1880 , "dir" : 2}
anime["ManClap"] =   {    "start" : 1881,    "stop"  :1995 , "dir" : 1}
anime["ManSalut"] =  {    "start" : 2012,    "stop"  :2084 , "dir" : 1}
anime["ManHeart"] =  {    "start" : 2135,    "stop"  :2180 , "dir" : 1}

anime["1"] = {    "start" : 203,    "stop"  :229 , "dir" : 2}
anime["2"] = {    "start" : 1,    "stop"  :202 , "dir" : 1}

anime["3"] =  {    "start" : 2065,    "stop"  :2084 , "dir" : 2}
anime["4"] =  {    "start" : 230,    "stop"  :500 , "dir" : 1}
anime["5"] =  {    "start" : 700,    "stop"  :800 , "dir" : 2}
anime["6"] =  {    "start" : 865,    "stop"  :1200 , "dir" : 2}
anime["7"] =  {    "start" : 1220,    "stop"  :1400 , "dir" : 2}
anime["8"] =  {    "start" : 1615,    "stop"  :1800 , "dir" : 2}
anime["9"] =  {    "start" : 1820,    "stop"  :1880 , "dir" : 2}
anime["10"] = {    "start" : 1881,    "stop"  :1995 , "dir" : 1}
anime["11"] = {    "start" : 2012,    "stop"  :2084 , "dir" : 1}
anime["12"] = {    "start" : 2135,    "stop"  :2180 , "dir" : 1}


curentAnime = "GirlRespire";

bg = pg.image.load("./data/backgrounds/fnd1.png");
bg = pg.transform.scale(bg, (1280, 720))
sprites = {};
clock = pg.time.Clock()
displayText = "";
bubble = pg.transform.scale( pg.image.load("./data/Objects/bubble.png"), (1280, 720))
doInput = False
inputTxt = "";
promptTxt = ">";
while True:
    if os.path.exists("c4k"): os.unlink("c4k");
    if os.path.exists("cmd_c4k"):
        cmd = open("cmd_c4k","r").read();
        open("cmd_c4k", "w")
        param=cmd[6:]
        if cmd[:6]=="print:":
            displayText+=param+"\n"

        if cmd[:6]=="clear:":
            displayText=""

        if cmd[:6]=="anime:":
            if param in anime:
                curentAnime=param
        if cmd[:6]=="input:":
            if os.path.exists("rsp_c4k"): os.unlink("rsp_c4k");
            promptTxt=param
            inputTxt=""
            doInput=True

    clock.tick(25)
    mScreen.blit(bg,(0,0))
    framepos += framedir;
    if framepos >= anime[curentAnime]["stop"] :
        if anime[curentAnime]["dir"]==2:
            framedir = -1
            framepos = anime[curentAnime]["stop"] -1
        else:
            framedir = 1
            framepos =  anime[curentAnime]["start"]

    if framepos <= anime[curentAnime]["start"] :
        framedir = 1;
        framepos = anime[curentAnime]["start"]

    if not (framepos in sprites):
        sprites[framepos] = pg.image.load("./data/sprites/fornite."+("000000000"+str(framepos))[-6:]+".png")

    mScreen.blit( sprites[framepos], (0, 0))
    txt = myfont.render('{0} - {1}'.format(curentAnime,framepos), True, (0, 0, 0))
    mScreen.blit(txt, (0, 0))

    ox = 765
    oy = 90;
    x = 0;
    y = 0;
    mx = 400;

    if displayText != "" :
        mScreen.blit(bubble,(0,0))

        for ww in displayText.replace("\n"," CRLF ").split():
            word = myfont.render(ww+" ",True,(0,0,0));
            (w,h)=word.get_size();
            if (((x+w) > mx) or (ww=="CRLF")) :
                x=0
                y+=h*1.2
                continue
            mScreen.blit(word,(ox+x,oy+y))
            x+=w
    x = 0;
    if doInput:
        if displayText == "":
            mScreen.blit(bubble, (0, 0))
        char=""
        if (int(time.time()*2) % 2) :
            char="_"
        for ww in (promptTxt+inputTxt+char).replace("\n"," CRLF ").split():
            word = myfont.render(ww+" ",True,(0,0,255));
            (w,h)=word.get_size();
            if (((x+w) > mx) or (ww=="CRLF")) :
                x=0
                y+=h*1.2
                continue
            mScreen.blit(word,(ox+x,oy+y+h/4))
            x+=w







    pg.display.update()
    for event in pg.event.get():
        k = anime.keys()

        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            pass
        if event.type == pg.KEYDOWN:
            if doInput:
                if event.key == pg.K_RETURN:
                    doInput=False;
                    open("rsp_c4k","w").write(inputTxt);
                    inputTxt="";
                elif event.key == pg.K_BACKSPACE:
                    inputTxt=inputTxt[:-1]
                else:
                    inputTxt+=event.unicode
            if event.key == pg.K_ESCAPE:
                pg.quit()
                open("rsp_c4k", "w").write("Quit");
                sys.exit()

