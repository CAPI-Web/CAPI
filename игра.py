from threading import *
from tkinter import *
from time import *
from random import *
import sys
import os
#import time
#test
print("Hello, World!")
none = False

cam1 = False
cam2 = False
cam3 = False
cam4 = False
cam5 = False
camStatus = [bool(none), bool(cam1), bool(cam2), bool(cam3), bool(cam4), bool(cam5)]


eyeSpawn1 = False
eyeSpawn2 = False
eyeSpawn3 = False

isLeshOnCam = False

eye1 = 0
eye2 = 0
eye3 = 0

eyes = [none, eyeSpawn1, eyeSpawn2, eyeSpawn3]
eyePlace = [none, eye1, eye2, eye3]
eyeIndex = 1
placeIndex = 1
fGame = 0


sounds = [none, "z", "x", "c", "v", "b", "n", "m"]
soundRound = 1
lPos = 1
eyePos = 2
mouthPos = 3
sound = 0
client_answer = "a"



temp = 0
leshLastPos = 0
eyeLastPos = 0
mouthLastPos = 0
singing = False

camShow = 0

vis1L = 0
vis2L = 0
vis3L = 0
vis4L = 0
vis5L = 0



def main():
    def bExitt_click():
        root.destroy()

    def bcont_click():
        file=open('уровень.txt', 'a+')
        level=file.read()
        #print(level)

    def bAut_click():
        print('CAPI')

    def bStart_click():
        #def bExit_click(event): #из игры в главное меню
        #    fGame.destroy()
        #    global temp
        #    temp = 0

        def bCams_click(event): #В камерах
            def Cam1(event):
                def bVBack_click(event):


                    vis1L.destroy()
                    vis1L.bind_all("<KeyPress-Escape>", bVBack_click)



                global vis1L
                global camShow
                camShow = 1

                vis1 = PhotoImage(file='cam1.png')  # работа Ильи
                vis1L = Label(fCams)
                vis1L.image = vis1
                vis1L['image'] = vis1L.image
                vis1L.place(relwidth=1, relheight=1)

                fCams.bind_all("<KeyPress-Escape>", bVBack_click)
                #bVBack = Button(vis1L, text='назад', command=bVBack_click)
                #bVBack.place(x=1880, y=1055)









                global eyePlace
                

            def Cam2(event):
                def bVBack_click(event):


                    vis2L.destroy()
                    vis2L.bind_all("<KeyPress-Escape>", bVBack_click)

                global camShow
                global vis2L
                camShow = 2
                vis2=PhotoImage(file='cam2.png')
                vis2L=Label(fCams)
                vis2L.image=vis2
                vis2L['image']=vis2L.image
                vis2L.place(relwidth=1, relheight=1)

                fCams.bind_all("<KeyPress-Escape>", bVBack_click)





            def Cam3(event):
                def bVBack_click(event):
                    vis3L.destroy()
                    vis3L.bind_all("<KeyPress-Escape>", bVBack_click)

                def Talk_click(event):
                    def bTBack_click(event):
                        #fBar.destroy()
                        fCams.bind_all("<KeyPress-Escape>", bVBack_click)
                        #BBarL.destroy()

                def BarMan():
                    BBar = PhotoImage(file='бармен ок.png')  # работа Ильи
                    BBarL = Label(vis3L)
                    BBarL.image = BBar
                    BBarL['image'] = BBarL.image
                    BBarL.place(x=900, y=300)


                    #fBar=Frame(vis3L, bg='yellow')
                    #fBar.place(relwidth=1, relheight=1)
                    #fBar.bind_all("<KeyPress-Escape>", bTBack_click)
                    #fBar.bind_all("<KeyPress-Down>", bTBack_click)

                global camShow
                global vis3L
                camShow = 3



                vis3=PhotoImage(file='cam3.png')#работа Ильи
                vis3L=Label(fCams)
                vis3L.image=vis3
                vis3L['image']=vis3L.image
                vis3L.place(relwidth=1, relheight=1)

                bTalk=Button(vis3L, text='БАРМЕН', command=BarMan)
                bTalk.pack(expand=1, anchor=S)


                fCams.bind_all("<KeyPress-Escape>", bVBack_click)
                fCams.bind_all("<KeyPress-Down>", Talk_click)


            def Cam4(event):
                def bVBack_click(event):
                    vis4L.destroy()
                    vis4L.bind_all("<KeyPress-Escape>", bVBack_click)

                global camShow
                global vis4L
                camShow = 4

                vis4 = PhotoImage(file='cam4.png')
                vis4L = Label(fCams)
                vis4L.image = vis4
                vis4L['image'] = vis4L.image
                vis4L.place(relwidth=1, relheight=1)

                fCams.bind_all("<KeyPress-Escape>", bVBack_click)


            def Cam5(event):
                def bVBack_click(event):
                    vis5L.destroy()
                    vis5L.bind_all("<KeyPress-Escape>", bVBack_click)

                global camShow
                global vis5L
                camShow = 5

                vis5 = PhotoImage(file='cam5.png')#работа Ильи
                vis5L = Label(fCams)
                vis5L.image = vis5
                vis5L['image'] = vis5L.image
                vis5L.place(relwidth=1, relheight=1)

                fCams.bind_all("<KeyPress-Escape>", bVBack_click)


            def bCBack_click(event): #закрыть камеры
                fCams.destroy()
                fGame.bind_all("<KeyPress-down>", bCams_click)

            fCams=Frame(fGame, bg='gray')
            fCams.place(x=1, y=1, relwidth=1, relheight=1)
            bCBack=Button(fCams, text='<                                                                                                                                   >', command=bCBack_click)
            bCBack.pack(side=BOTTOM,)
            bExit=Button(fCams, text='Выйти', command=bExit_click)
            bExit.pack(expand=1, anchor=NE)

            fr1=Frame(fCams, bg='black')
            fr1.place(x=450, y=600, relwidth=0.05, relheight=0.3)

            fc1=Frame(fCams, bg='black')
            fc1.place(x=450, y=650, relwidth=0.2, relheight=0.05)

            fr2=Frame(fCams, bg='black')
            fr2.place(x=700, y=550, relwidth=0.1, relheight=0.2)

            fc2=Frame(fCams, bg='black')
            fc2.place(x=300, y=700, relwidth=0.1, relheight=0.05)

            fr3=Frame(fCams, bg='black')
            fr3.place(x=50, y=600, relwidth=0.2, relheight=0.2)

            fr4=Frame(fCams, bg='black')
            fr4.place(x=150, y=400, relwidth=0.1, relheight=0.15)

            fc3=Frame(fCams, bg='black')
            fc3.place(x=220, y=500, relwidth=0.03, relheight=0.1)

            fv11=Frame(fCams, bg='black')
            fv11.place(x=100, y=700, relwidth=0.02, relheight=0.25)

            fv12=Frame(fCams, bg='black')
            fv12.place(x=100, y=950, relwidth=0.3, relheight=0.03)

            fv21=Frame(fCams, bg='black')
            fv21.place(x=830, y=700, relwidth=0.02, relheight=0.25)

            fv22=Frame(fCams, bg='black')
            fv22.place(x=630, y=950, relwidth=0.1235, relheight=0.03)



            bCam1=Button(fCams, text='cam1', command = Cam1,  width = 4, height=1)
            bCam2=Button(fCams, text='cam2', command = Cam2,  width = 4, height=1)
            bCam3=Button(fCams, text='cam3', command = Cam3,  width = 4, height=1)
            bCam4=Button(fCams, text='cam4', command = Cam4,  width = 4, height=1)
            bCam5=Button(fCams, text='cam5', command = Cam5,  width = 4, height=1)

            bCam1.place(x=700, y=550)
            bCam2.place(x=397, y=791)
            bCam3.place(x=170, y=537)
            bCam4.place(x=100, y=957)
            bCam5.place(x=830, y=960)

            fCams.bind_all("<KeyPress-1>", Cam1)
            fCams.bind_all("<KeyPress-2>", Cam2)
            fCams.bind_all("<KeyPress-3>", Cam3)
            fCams.bind_all("<KeyPress-4>", Cam4)
            fCams.bind_all("<KeyPress-5>", Cam5)

            fr0=Frame(fCams, bg='black')
            fr0.place(x=300, y=900, relwidth=0.2, relheight=0.1)
            lYou=Label(fr0, text='YOU', bg='black', fg='white')
            lYou.place(x=180, y=35)

            fCams.bind_all("<KeyPress-Down>", bCBack_click)

        def flower_click(event):
            global lPos
            a = 0
            b = 100
            if lPos == 10 or lPos == 9 or lPos == 8:
                toWater = randint(a, b)
                if toWater <= 20:
                    if lPos == 10:
                        lPos = 7
                    elif lPos == 8:
                        lPos = 2
                    elif lPos == 9:
                        lPos = 1
                    else:
                        pass
                else:
                    pass
            else:
                pass

            if singing == True:
                MouthSingEntity = PhotoImage(file='рот поёт.png')
                MouthSingEntityL = Label(fGame)
                MouthSingEntityL.image = MouthSingEntity
                MouthSingEntityL['image'] = MouthSingEntityL.image
                MouthSingEntityL.place(x=960, y=540)

                mouthQuestion = Label(fGame, bg="white", fg="black", text=sounds[sound])
                mouthQuestion.place(x=900, y=500)

                                      # игра
        fGam = PhotoImage(file='office.png')
        fGame = Label(root)
        fGame.image = fGam
        fGame['image'] = fGame.image
        fGame.place(relwidth=1, relheight=1)

        def bExit_click():
            fGame.destroy()
            global temp
            temp = 0
        bExit=Button(fGame, text='Выйти', command=bExit_click)
        bExit.pack(expand=1, anchor=NE)
        bCams=Button(fGame, text='<                                                                                                                                   >', command=bCams_click)
        bCams.place(x=750, y=1030)
        flower = Button(fGame, text = 'цветочек', bg = 'green', fg = "black")
        flower.place(x = 1800, y = 800)

        fGame.bind_all("<KeyPress-Down>", bCams_click)
        fGame.bind_all("<KeyPress-Caps_Lock>", bExit_click)
        fGame.bind_all("<KeyPress-f>", flower_click)

        global temp
        temp = 1













    def bSett_click(): #натсройки

        def bBack_click(): #из настроек на главное меню
            setmL.destroy()#работа Ильи
            backB.destroy()#работа Ильи
            MusicLowB.destroy()#работа Ильи
            MusicHighB.destroy()#работа Ильи
            ResolutionLowB.destroy()#работа Ильи
            ResolutionHighB.destroy()#работа Ильи
            GraphicsLowB.destroy()#работа Ильи
            GraphicsHighB.destroy()#работа Ильи
            DifficultyLowB.destroy()#работа Ильи
            DifficultyHighB.destroy()#работа Ильи

        setm=PhotoImage(file='настройки бэк.png')
        setmL=Label(root)
        setmL.image=setm
        setmL['image']=setmL.image
        setmL.place(relwidth=1, relheight=1)

        back = PhotoImage(file='назад.png')#работа Ильи
        backB = Button(root, text="       Назад       ", font="Arial 40", command=bBack_click)#работа Ильи
        backB.place(x=52, y=930)#работа Ильи

        MusicLowB = Button(root, text="<", width=3, height=3)#работа Ильи
        MusicLowB.place(x=900, y=130)#работа Ильи

        MusicHighB = Button(root, text=">", width=3, height=3)#работа Ильи
        MusicHighB.place(x=1200, y=130)#работа Ильи

        ResolutionLowB = Button(root, text="<", width=3, height=3)#работа Ильи
        ResolutionLowB.place(x=900, y=300)#работа Ильи

        ResolutionHighB = Button(root, text=">", width=3, height=3)#все здесь моё
        ResolutionHighB.place(x=1200, y=300)

        GraphicsLowB = Button(root, text="<", width=3, height=3)
        GraphicsLowB.place(x=900, y=450)

        GraphicsHighB = Button(root, text=">", width=3, height=3)
        GraphicsHighB.place(x=1200, y=450)

        DifficultyLowB = Button(root, text="<", width=3, height=3)
        DifficultyLowB.place(x=900, y=620)

        DifficultyHighB = Button(root, text=">", width=3, height=3)
        DifficultyHighB.place(x=1200, y=620)




    root=Tk() #стар
    root['bg']='#000000'
    root.geometry('')
    root.title('Игра')
    root.attributes('-fullscreen', True)
    canvas=Canvas(root, width=1920,  height=1080)
    root.resizable(False, False)
    canvas.pack()
    menu=PhotoImage(file='меню.png')
    menuL=Label(root)
    menuL.image=menu
    menuL['image']=menuL.image
    menuL.place(relwidth=1, relheight=1)

    newGame=PhotoImage(file='новая игра.png')
    startB=Button(menuL, image=newGame, command=bStart_click)
    startB.place(x=20, y=325)

    cont=PhotoImage(file='продолжить.png')
    contB=Button(menuL, image=cont, command=bcont_click)
    contB.place(x=20, y=470)


    sett=PhotoImage(file='настройки.png')
    settB=Button(menuL, image=sett, command=bSett_click)
    settB.place(x=20, y=608)


    aut=PhotoImage(file='авторы.png')
    autB=Button(menuL, image=aut, command=bAut_click)
    autB.place(x=20, y=745)
    def bExitt_click():
        root.destroy()
        os._exit(1)
    exitt=PhotoImage(file='выйти.png')
    exittB=Button(menuL, image=exitt, command=bExitt_click)
    exittB.place(x=250, y=745)





    root.mainloop()



def tick():
    global temp
    global leshLastPos
    global eyeLastPos
    global eyePos
    global lPos
    global cam1
    global cam2
    global cam3
    global cam4
    global cam5
    global camStatus
    global eyeIndex
    global placeIndex
    global soundRound
    global sound
    global singing

    while True:
        if temp == 1:

            a = 0
            b = 100

            for i in range(0, 36):

                sleep(5)
                moveRnd = randint(a, b)
                print(moveRnd)


                if moveRnd <= 30: #Леший ходьба
                    if lPos == 1:
                        lPos = 7
                        leshLastPos = 1


                    elif lPos == 2:
                        directionRnd = randint(0, 3)

                        if directionRnd == 0:
                            if leshLastPos == 3:
                                directionRnd = randint(1, 2)
                                if directionRnd == 1:
                                    lPos = 6
                                else:
                                    lPos = 4
                            lPos = 3


                        elif directionRnd == 1:
                            lPos = 4

                        else:
                            if leshLastPos == 6:
                                directionRnd = randint(1, 2)
                                if directionRnd == 1:
                                    lPos = 3
                                else:
                                    lPos = 4



                    elif lPos == 3:
                        lPos = 2


                    elif lPos == 4:
                        lPos = 8


                    elif lPos == 5:
                        lPos = 9


                    elif lPos == 6:
                        directionRnd = randint(1, 3)
                        if directionRnd == 1:
                            if leshLastPos == 2:
                                directionRnd = randint(1, 2)
                                if directionRnd == 1:
                                    lPos = 7
                                else:
                                    lPos = 10
                        elif directionRnd == 2:
                            if leshLastPos == 7:
                                directionRnd = randint(1, 2)
                                if directionRnd == 1:
                                    lPos = 2
                                else:
                                    lPos = 10


                        else:
                            lPos = 10

                    elif lPos == 7:
                        if leshLastPos == 1:
                            lPos = 6
                        else:
                            if leshLastPos == 6:
                                lPos = 1
                            else:
                                lPos = 6

                    elif lPos == 8 or lPos == 10 or lPos == 9:
                        death = randint(0, 100)
                        if death <= 20:
                            print('you dead!')
                            temp = 0
                        else:
                            pass
                else:
                    pass






                '''
                if moveRnd<=45: #Глаз ходьба
                    if eyePos==1:
                        directionRnd=randint(0, 2)
                        if directionRnd==1:
                            if eyeLastPos == 5:
                                eyePos = 7
                            else:
                                eyePos = 5

                        else:
                            if eyeLastPos == 7:
                                eyePos = 5
                            else:
                                eyePos = 7

                    elif eyePos == 2:
                        directionRnd = randint(0, 3)

                        if directionRnd == 0:
                            if eyeLastPos == 3:
                                directionRnd = randint(1, 2)
                                if directionRnd == 1:
                                    eyePos = 6
                                else:
                                     eyePos = 4
                            eyePos = 3


                        elif directionRnd == 1:
                            eyePos = 4

                        else:
                            if eyeLastPos == 6:
                                directionRnd = randint(1, 2)
                                if directionRnd == 1:
                                     eyePos = 3
                                else:
                                    eyePos = 4



                    elif eyePos == 3:
                        directionRnd = 2


                    elif eyePos == 4:
                        eyePos = 8


                    elif eyePos == 5:
                         eyePos = 9


                    elif eyePos == 6:
                        directionRnd = randint(1, 3)
                        if directionRnd == 1:
                            if eyeLastPos == 2:
                                directionRnd = randint(1, 2)
                                if directionRnd == 1:
                                    eyePos = 7
                                else:
                                    eyePos = 10
                        elif directionRnd == 2:
                            if eyeLastPos == 7:
                                 directionRnd = randint(1, 2)
                                 if directionRnd == 1:
                                     eyePos = 2
                                 else:
                                     eyePos = 10


                        else:
                            eyePos = 10

                    elif eyePos == 7:
                        if eyeLastPos == 1:
                            eyePos = 6
                        else:
                            if eyeLastPos == 6:
                                 eyePos = 1
                            else:
                                 eyePos = 6

                    elif eyePos == 8 or eyePos == 10 or eyePos == 9:
                        death = randint(0, 100)
                        if death <= 20:
                            print('you dead!')
                            temp = 0
                        else:
                            pass


                else:
                    pass

                eyeLastPos = eyePos






                '''

                superRnd = randint(a, b) #Леший супер
                if superRnd <= 20:
                    camBroken = True
                else:
                    camBroken = False

                if camBroken:
                    if lPos == 1:
                        camStatus[1] = True
                    elif lPos == 2:
                        camStatus[2] = True
                    elif lPos == 3:
                        camStatus[3] = True
                    elif lPos == 4 or lPos == 8:
                        camStatus[4] = True
                    elif lPos == 5 or lPos == 9:
                        camStatus[5] = True
                    else:
                        pass
                else:
                    pass
                print('леший ходьба: ', lPos )
                #print("Глаз Ходьба: ", eyePos)
                print("Статус камер (False - рабочая, True - сломанная): ", camStatus[1], camStatus[2], camStatus[3], camStatus[4], camStatus[5])





                '''

                if eyeIndex < 4: #Глаз супер
                    spawnChance = randint(a, b)
                    if spawnChance <= 20:
                        if eyes[eyeIndex] == False:
                            eyes[eyeIndex] = True
                            camChoose = randint(1, 6)

                            while camChoose == eyePos:
                                camChoose = randint(1, 6)
                            eyePlace[placeIndex] = camChoose
                        eyeIndex += 1
                        placeIndex += 1
                        print("состояние глаз: ", eyes[1], eyes[2], eyes[3])
                        print("место глаз: ", eyePlace[1], eyePlace[2], eyePlace[3])
                    else:
                        print('глаза не двигались')
                else:
                    pass
                death = randint(a, b)
                #print(death)
                if death <= 15:
                    print("you dead!")
                    break
                else:
                    pass

                if soundRound < 4:  # Рот супер
                    print('Статус пения: ', singing)
                    soundcheckRnd = randint(a, b)
                    if soundcheckRnd <= 100:
                        lastSound = sounds[sound]
                        sound = randint(1, 7)
                        print("Рот говорит: ", sounds[sound])
                        soundRound += 1
                        singing = True
                    else:
                        print("Рот не говорит")
                    if soundRound == 4:
                        death = randint(a, b)
                        if death <= 25:
                            print("Тебя убила ульта рта")
                            break
                    else:
                        pass

                    if singing == True:  # диалог

                        print(' по мнению тиков ты сказал: ', client_answer)
                        if client_answer != lastSound and soundRound >= 1 and client_answer != 'a':
                            death = randint(a, b)
                            if death <= 90:
                                print("Ты произнес не тот звук и умер")
                                break
                            else:
                                print("Ты ошибся, но Рот не заметил")
                    else:
                        pass
                        '''


def EventShow():
    global vis5L
    global vis4L
    global vis3L
    global vis2L
    global vis1L
    global camShow
    global lPos
    global isLeshOnCam
    while True:
        if temp == 1:

            for i in range(0, 36):
                sleep(5)



                if camShow == 1:
                    if lPos == 1:
                        print("Лешего видно на 1 камере")
                        leshEntity = PhotoImage(file='lesh cam1.png')
                        leshEntityL = Label(vis1L)
                        leshEntityL.image = leshEntity
                        leshEntityL['image'] = leshEntityL.image
                        if(isLeshOnCam == False):
                            leshEntityL.place(x=1 , y=1)
                            isLeshOnCam = True

                        if vis2L != 0:
                            vis2L.destroy()
                            vis2L = 0
                        if vis3L != 0:
                            vis3L.destroy()
                            vis3L = 0
                        if vis4L != 0:
                            vis4L.destroy()
                            vis4L = 0
                        if vis5L != 0:
                            vis5L.destroy()
                            vis5L = 0

                    if lPos == 4 or lPos == 6 or lPos == 7 or lPos == 8 or lPos == 9 or lPos == 10:
                        print('Леший ушел')
                        isLeshOnCam = False
                        leshEntityL.destroy()




                if camShow == 2:
                    if lPos == 2:
                        print("Лешего видно на 2 камере")
                        leshEntity = PhotoImage(file='lesh cam2.png')
                        leshEntityL = Label(vis2L)
                        leshEntityL.image = leshEntity
                        leshEntityL['image'] = leshEntityL.image
                        leshEntityL.place(x=-1, y=-1)
                        if vis1L != 0:
                            vis1L.destroy
                            vis1L = 0
                        if vis3L != 0:
                            vis3L.destroy
                            vis3L = 0
                        if vis4L != 0:
                            vis4L.destroy
                            vis4L = 0
                        if vis5L != 0:
                            vis5L.destroy
                            vis5L = 0

                if camShow == 3:
                    if lPos == 3:
                        print("Лешего видно на 3 камере")
                        leshEntity = PhotoImage(file='lesh cam3.png')
                        leshEntityL = Label(vis3L)
                        leshEntityL.image = leshEntity
                        leshEntityL['image'] = leshEntityL.image
                        leshEntityL.place(x=-1, y=-1)
                        if vis1L != 0:
                            vis1L.destroy
                            vis1L = 0
                        if vis2L != 0:
                            vis2L.destroy
                            vis2L = 0
                        if vis4L != 0:
                            vis4L.destroy
                            vis4L = 0
                        if vis5L != 0:
                            vis5L.destroy
                            vis5L = 0

                if camShow == 4:
                    if lPos == 4:
                        num = 1
                        while num <= 4:
                            File = '1'
                            vent_level = 'lesh cam' + File
                            if num == 1:
                                File = 2
                            elif num == 2:
                                File = 3
                            elif File == 3:
                                File = 4
                            elif File == 4:
                                break
                        print("Лешего видно на 4 камере")
                        leshEntity = PhotoImage(file='le')
                        leshEntityL = Label(vis3L)
                        leshEntityL.image = leshEntity
                        leshEntityL['image'] = leshEntityL.image
                        leshEntityL.place(x=-1, y=-1)
                        if vis1L != 0:
                            vis1L.destroy
                            vis1L = 0
                        if vis2L != 0:
                            vis2L.destroy
                            vis2L = 0
                        if vis4L != 0:
                            vis4L.destroy
                            vis4L = 0
                        if vis5L != 0:
                            vis5L.destroy
                            vis5L = 0



                if camShow == 5:
                    if lPos == 5:
                        print("Лешего видно на 5 камере")
                        leshEntity = PhotoImage(file='lesh cam5_3.png')
                        leshEntityL = Label(vis5L)
                        leshEntityL.image = leshEntity
                        leshEntityL['image'] = leshEntityL.image
                        leshEntityL.place(x=-1, y=-1)
                        if vis1L != 0:
                            vis1L.destroy
                            vis1L = 0
                        if vis2L != 0:
                            vis2L.destroy
                            vis2L = 0
                        if vis3L != 0:
                            vis3L.destroy
                            vis3L = 0
                        if vis4L != 0:
                            vis4L.destroy
                            vis4L = 0











mainT = Thread(target = main)
tickT = Thread(target = tick)
eventShowT = Thread(target = EventShow)

mainT.start()
tickT.start()
eventShowT.start()



