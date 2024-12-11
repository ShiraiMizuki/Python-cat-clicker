import tkinter as tk
from gettext import textdomain
from tkinter import messagebox, Radiobutton, StringVar, Button, Scale
from PIL import Image, ImageTk
import random
import re
import pygame ##tylko do muzyki i kontrolowania muzyki

pygame.init()
w = tk.Tk()
w.title("Spooky Scary Gato Clicker :3")
w.geometry("1920x1080")
w.configure(bg='black')
                                                                       # Loading Sounds


pygame.init()
boom = pygame.mixer.Sound('mp3/VineBoomSoundEffect.mp3')
kys = pygame.mixer.Sound('mp3/Gravity-[AudioTrimmer.com].mp3')
music = ["mp3/BlackNo.1.mp3" , "mp3/Nettie.mp3"]
current_song_index = 0


#ZMARNOWANE 2 GODZINY WALONE AI NIE MOGLO TEGO ZROBIC


def play_next_song():
    global current_song_index
    pygame.mixer.music.stop()
    current_song_index += 1
    if current_song_index >= len(music):
        current_song_index = 0
    pygame.mixer.music.load(music[current_song_index])
    pygame.mixer.music.play()


                                                                 #loading images


kotdynia = Image.open('img/cat-halloween.png')
kotdynia = kotdynia.resize((400, 400), )
kotdynia = ImageTk.PhotoImage(kotdynia)
kotbully = Image.open('img/dontbully.png')
kotbully = kotbully.resize((450, 550), )
kotbully = ImageTk.PhotoImage(kotbully)
veryscary = Image.open('img/veryscary.png')
veryscary = ImageTk.PhotoImage(veryscary)
steele = Image.open('img/Type_O_Negative_logo.png')
steele = ImageTk.PhotoImage(steele)
clickerzdj = Image.open('img/cat_drinking_boba.png')
clickerzdj = ImageTk.PhotoImage(clickerzdj)
scaryuni = Image.open('img/scary_uni.jpg')
scaryuni = scaryuni.resize((250, 200), )
scaryuni = ImageTk.PhotoImage(scaryuni)
cute_pumpkin = Image.open('img/cute_pumpkin_gato.jpg')
cute_pumpkin = cute_pumpkin.resize((250, 200), )
cute_pumpkin = ImageTk.PhotoImage(cute_pumpkin)
halloweenmiku = Image.open('img/halloweenmiku.webp')
halloweenmiku = halloweenmiku.resize((250, 200), )
halloweenmiku = ImageTk.PhotoImage(halloweenmiku)
serj = Image.open('img/serjmybeloved.webp')
serj = serj.resize((250, 200), )
serj = ImageTk.PhotoImage(serj)
bandito = Image.open('img/el_bandito-1.png')
bandito = bandito.resize((250, 200), )
bandito = ImageTk.PhotoImage(bandito)
devil_cato = Image.open('img/devil_cat.jpg')
devil_cato = devil_cato.resize((250, 200), )
devil_cato = ImageTk.PhotoImage(devil_cato)
jinx_cat = Image.open('img/jinx.jpg')
jinx_cat = jinx_cat.resize((250, 200), )
jinx_cat = ImageTk.PhotoImage(jinx_cat)
autism = Image.open('img/autism.jpg')
autism = autism.resize((250, 200), )
autism = ImageTk.PhotoImage(autism)
witchcat = Image.open('img/witch_cat.jpg')
witchcat = witchcat.resize((250, 200), )
witchcat = ImageTk.PhotoImage(witchcat)
jumpscareo1zdj = Image.open('img/jumpscare1.jpg')
jumpscareo1zdj = jumpscareo1zdj.resize((1200, 900), )
jumpscareo1zdj = ImageTk.PhotoImage(jumpscareo1zdj)
jumpscareo2zdj = Image.open('img/jumpscare2.jpg')
jumpscareo2zdj = jumpscareo2zdj.resize((1200, 900), )
jumpscareo2zdj = ImageTk.PhotoImage(jumpscareo2zdj)
jumpscareo3zdj = Image.open('img/jumpscare3.jpg')
jumpscareo3zdj = jumpscareo3zdj.resize((1200, 900), )
jumpscareo3zdj = ImageTk.PhotoImage(jumpscareo3zdj)
jumpscareo4zdj = Image.open('img/steelejumpscare.png')
jumpscareo4zdj = jumpscareo4zdj.resize((1200, 900), )
jumpscareo4zdj = ImageTk.PhotoImage(jumpscareo4zdj)
bonuszdj = Image.open('img/bonuszdj.jpg')
bonuszdj = bonuszdj.resize((250, 200), )
bonuszdj = ImageTk.PhotoImage(bonuszdj)
astolfo = Image.open('img/astolfospooky.webp')
astolfo = astolfo.resize((250, 200), )
astolfo = ImageTk.PhotoImage(astolfo)
sleepy = Image.open('img/eepy spooky.jpg')
sleepy = sleepy.resize((250, 200), )
sleepy = ImageTk.PhotoImage(sleepy)


                                                                       # variables


skip_song = False
window_open = False
window_open2 = False
window_open3 = False
multiplayersgreen = 25
multiplayersRB = 2
twelvesmulti = 3
oddevenmulti = 2
Costmulti = 2
points = 20000
pointonclick = 1
bonupointonclick = pointonclick * 2
upgradeclick = 100
upgradeautoclick = 250
current_volume = 50
autoclick = 0
colour_win = False
oddeveno_win = False
twelves_win = False
loose = False
result = ""
numberrouletee = ""
idfk = tk.StringVar(value="none")
oddeven = tk.StringVar(value='none')
twelves = tk.StringVar(value='none')
jinxbought = False
pumpkinbought = False
devilbought = False
witchbought = False
unibought = False
mikubought = False
serjbought = False
banditobought = False
autismbought = False
astolfobought= False
eepybought = False
# roulette
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
green = [0]
odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
firstwelve = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
secondtwelve = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
thirdtwelve = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
bet = 0
textoxoxoxoxoxo = 'changes the basic cat image to cute eepy cat price: 3000'
textoxoxoxoxox = 'changes the basic cat image to jinx the cat price: 250'
textoxoxoxoxo = 'changes the basic cat image to autumn cat price: 350'
textoxoxoxox = 'changes the basic cat image to a cute cat in a pumpkin price: 400'
textoxoxoxo = 'changes the basic cat image to the real devil cat price: 900'
textoxoxox = 'changes the basic cat image to witch cat price: 1400'
textoxoxo = 'changes the basic cat image to spooky uni the cat price: 2000'
textoxox = 'changes the basic cat image to halloween miku price: 4000'
textoxo = 'changes the basic cat image to serj tankian price: 8400'
textox = 'changes the basic cat image to El bandito price: 1000000'
texto = 'changes the basic cat image to spooky Astolfo price: 500000'
muscioxoxoxox = 'Add Gravity cost: 800'
muscioxoxoxo = 'Add I Dont Wanna Be Me to songs cost: 700'
muscioxoxox = 'Add Pain to songs cost: 600'
muscioxoxo = 'Add Dark Entries to songs cost: 500'
muscioxox = 'Add Lesbian Vampyres From Outer Space to songs cost: 400'
muscioxo = 'Add Werewolfe to songs cost: 300'
musciox = 'Add All Hallows Eve to songs cost: 200'
muscio = 'Add halloween in heaven to songs cost: 100'


                                                                                              #roulette


def roulette():
    global window_open2
    global bet
    global multiplayersRB, frame, multiplayersgreen, submit, rblack, rred, rgreen, nocolour, odd, even, first12, second12, third12, multiplayerstwelves, multiplayersoddeven, nonoddoreven, notwelves, oddb, evenb, info, roulettewindow
    if window_open2:
        return
    window_open2 = True
    roulettewindow = tk.Toplevel(w)
    roulettewindow.attributes('-topmost', True)
    roulettewindow.title("roulette :3")
    roulettewindow.geometry("400x800")
    roulettewindow.config(bg='black')
    multiplayers = tk.Label(roulettewindow, text='multiplayer for red and black 2x')
    multiplayers.config(fg="white", font=('yugothicuisemibold', 10), bg="#A900D1")
    multiplayersoddeven = tk.Label(roulettewindow, text='multiplayer for odd or even 2x')
    multiplayersoddeven.config(fg="white", font=('yugothicuisemibold', 10), bg="#A900D1")
    multiplayerstwelves = tk.Label(roulettewindow, text='multiplayer for twelves = 3x')
    multiplayerstwelves.config(fg="white", font=('yugothicuisemibold', 10), bg="#A900D1")
    multiplayersgreen = tk.Label(roulettewindow, text='mutiplayer green = 25x')
    multiplayersgreen.config(fg="white", font=('yugothicuisemibold', 10), bg="#A900D1")
    rblack = Radiobutton(roulettewindow, text='black', variable=idfk, value='black')
    rblack.config(fg="#A900D1", bg="white")
    rred = Radiobutton(roulettewindow, text='red', variable=idfk, value='red')
    rred.config(fg="#A900D1", bg="white")
    rgreen = Radiobutton(roulettewindow, text='green', variable=idfk, value='green')
    rgreen.config(fg="#A900D1", bg="white")
    nocolour = Radiobutton(roulettewindow, text='no colour', variable=idfk, value='color not choosen')
    nocolour.config(fg="#A900D1", bg="white")
    oddb = Radiobutton(roulettewindow, text='odd', variable=oddeven, value='odd')
    oddb.config(fg="#A900D1", bg="white")
    evenb = Radiobutton(roulettewindow, text='even', variable=oddeven, value='even')
    evenb.config(fg="#A900D1", bg="white")
    nonoddoreven = Radiobutton(roulettewindow, text='no odd or even', variable=oddeven, value='none')
    nonoddoreven.config(fg="#A900D1", bg="white")
    first12 = Radiobutton(roulettewindow, text='first12', variable=twelves, value='first')
    first12.config(fg="#A900D1", bg="white")
    second12 = Radiobutton(roulettewindow, text='second12', variable=twelves, value='second')
    second12.config(fg="#A900D1", bg="white")
    third12 = Radiobutton(roulettewindow, text='third12', variable=twelves, value='third')
    third12.config(fg="#A900D1", bg="white")
    notwelves = Radiobutton(roulettewindow, text='no twelves', variable=twelves, value='none')
    notwelves.config(fg="#A900D1", bg="white")
    bet = tk.Entry(roulettewindow, )
    submit = tk.Button(roulettewindow, text='submit bets', command=betsubmitt)
    info = tk.Label(roulettewindow, fg="white", font=('yugothicuisemibold', 10), bg="black")
    rblack.pack()
    rred.pack()
    rgreen.pack()
    nocolour.pack()
    oddb.pack()
    evenb.pack()
    nonoddoreven.pack()
    first12.pack()
    second12.pack()
    third12.pack()
    notwelves.pack()
    multiplayers.pack()
    multiplayersgreen.pack()
    multiplayersoddeven.pack()
    multiplayerstwelves.pack()
    info.pack()
    bet.pack()
    submit.pack()

    def roulette_closed():
        global window_open2
        window_open2 = False
        roulettewindow.destroy()

    roulettewindow.protocol('WM_DELETE_WINDOW', roulette_closed)


def betsubmitt():
    global rnumber, beto, score, points, colour, bonus, oddeveno, twelves, bonusodeven, bonusthwelves, colour_win, oddeveno_win, twelves_win, tak, win, green_win, twelvos, winammout
    rnumber = random.randint(0, 36)
    beto = bet.get()
    colour = idfk.get()
    oddeveno = oddeven.get()
    green_win = False
    twelves_win = False
    oddeveno_win = False
    colour_win = False
    twelvos = twelves.get()
    if re.fullmatch(r"^(?:\d+\.\d+|\d+|\.\d+)$", str(beto)) is None:
        messagebox.showinfo('error', "Your bet is not a number")
    else:
        if int(beto) > points:
            messagebox.showinfo('error', 'you have not enough mons')
        else:
            points = points - int(beto)
            score.config(text="Score:" + str(points))
            if colour == 'none':
                if oddeveno != 'none':
                    if oddeveno == 'even' and rnumber in even:
                        oddeveno_win = True
                    elif oddeveno == 'odd' and rnumber in odd:
                        oddeveno_win = True
                    else:
                        oddeveno_win = False
                        info.config(text='You have lost :(')
                        return
                if twelvos != 'none':
                    if twelvos == 'first' and rnumber in firstwelve:
                        twelves_win = True
                    elif twelvos == 'second' and rnumber in secondtwelve:
                        twelves_win = True
                    elif twelvos == 'third' and rnumber in thirdtwelve:
                        twelves_win = True
                    else:
                        twelves_win = False
                        info.config(text='You have lost :(')
                        return
            elif colour == 'red' and rnumber in red:
                colour_win = True
                if oddeveno != 'none':
                    if oddeveno == 'even' and rnumber in even:
                        oddeveno_win = True
                    elif oddeveno == 'odd' and rnumber in odd:
                        oddeveno_win = True
                    else:
                        oddeveno_win = False
                        info.config(text='You have lost :(')
                        return
                if twelvos != 'none':
                    if twelvos == 'first' and rnumber in firstwelve:
                        twelves_win = True
                    elif twelvos == 'second' and rnumber in secondtwelve:
                        twelves_win = True
                    elif twelvos == 'third' and rnumber in thirdtwelve:
                        twelves_win = True
                    else:
                        twelves_win = False
                        info.config(text='You have lost :(')
                        return
            elif colour == 'black' and rnumber in black:
                colour_win = True
                if oddeveno != 'none':
                    if oddeveno == 'even' and rnumber in even:
                        oddeveno_win = True
                    elif oddeveno == 'odd' and rnumber in odd:
                        oddeveno_win = True
                    else:
                        oddeveno_win = False
                        info.config(text='You have lost :(')
                        return
                if twelvos != 'none':
                    if twelvos == 'first' and rnumber in firstwelve:
                        twelves_win = True
                    elif twelvos == 'second' and rnumber in secondtwelve:
                        twelves_win = True
                    elif twelvos == 'third' and rnumber in thirdtwelve:
                        twelves_win = True
                    else:
                        twelves_win = False
                        info.config(text='You have lost :(')
                        return
            elif colour == 'green' and rnumber in green:
                if oddeveno != 'none':
                    if oddeveno == 'even' and rnumber in even:
                        oddeveno_win = True
                    elif oddeveno == 'odd' and rnumber in odd:
                        oddeveno_win = True
                    else:
                        oddeveno_win = False
                        info.config(text='You have lost :(')
                        return
                if twelvos != 'none':
                    if twelvos == 'first' and rnumber in firstwelve:
                        twelves_win = True
                    elif twelvos == 'second' and rnumber in secondtwelve:
                        twelves_win = True
                    elif twelvos == 'third' and rnumber in thirdtwelve:
                        twelves_win = True
                    else:
                        info.config(text='You have lost :(')
                        twelves_win = False
                        return
            else:
                info.config(text='You have lost :(')
            if colour_win == True and twelves_win == True and oddeveno_win == True:
                bonus = multiplayersRB + twelvesmulti + oddevenmulti
                points = points + int(beto) * bonus
                winammout = int(beto) * bonus - int(beto)
                score.config(text="Score:" + str(points))
                info.config(text='You have won ' + str(winammout) + 'Points :3333')
            elif colour_win == True and twelves_win == True:
                bonus = multiplayersRB + twelvesmulti
                winammout = int(beto) * bonus - int(beto)
                points = points + int(beto) * bonus
                score.config(text="Score:" + str(points))
                info.config(text='You have won ' + str(winammout) + 'Points :3333')
            elif colour_win == True and oddeveno_win == True:
                bonus = multiplayersRB + oddevenmulti
                points = points + int(beto) * bonus
                winammout = int(beto) * bonus - int(beto)
                score.config(text="Score:" + str(points))
                info.config(text='You have won ' + str(winammout) + 'Points :3333')
            elif twelves_win == True and oddeveno_win == True:
                bonus = oddeveno_win + twelvesmulti
                points = points + int(beto) * bonus
                winammout = int(beto) * bonus - int(beto)
                score.config(text="Score:" + str(points))
                info.config(text='You have won ' + str(winammout) + 'Points :3333')
            elif twelves_win == True:
                bonus = twelvesmulti
                points = points + int(beto) * bonus
                winammout = int(beto) * bonus - int(beto)
                score.config(text="Score:" + str(points))
                info.config(text='You have won ' + str(winammout) + 'Points :3333')
            elif oddeveno_win == True:
                bonus = oddevenmulti
                points = points + int(beto) * bonus
                winammout = int(beto) * bonus - int(beto)
                score.config(text="Score:" + str(points))
                info.config(text='You have won ' + str(winammout) + 'Points :3333')
            elif colour_win == True:
                bonus = multiplayersRB
                points = points + int(beto) * bonus
                winammout = int(beto) * bonus - int(beto)
                score.config(text="Score:" + str(points))
                info.config(text='You have won ' + str(winammout) + 'Points :3333')
            elif green_win == True and twelves_win == True and oddeveno_win == True:
                bonus = multiplayersgreen + twelvesmulti + oddevenmulti
                points = points + int(beto) * bonus
                winammout = int(beto) * bonus - int(beto)
                score.config(text="Score:" + str(points))
                info.config(text='You have won ' + str(winammout) + 'Points :3333')
            elif green_win == True and twelves_win == True:
                bonus = multiplayersgreen + twelvesmulti
                points = points + int(beto) * bonus
                winammout = int(beto) * bonus - int(beto)
                score.config(text="Score:" + str(points))
                info.config(text='You have won ' + str(winammout) + 'Points :3333')
            elif green_win == True and oddeveno_win == True:
                bonus = multiplayersgreen + oddevenmulti
                points = points + int(beto) * bonus
                winammout = int(beto) * bonus - int(beto)
                score.config(text="Score:" + str(points))
                info.config(text='You have won ' + str(winammout) + 'Points :3333')
            elif green_win == True:
                bonus = multiplayersgreen
                points = points + int(beto) * bonus
                winammout = int(beto) * bonus - int(beto)
                score.config(text="Score:" + str(points))
                info.config(text='You have won ' + str(winammout) + 'Points :3333')
            else:
                info.config(text='You have lost :(')
                return


                                                        # Starting page


def start():
    l1.place_forget()
    start.place_forget()
    menu.place_forget()
    quit.place_forget()
    lkotdynia.place_forget()
    l2.place_forget()
    peeter.place_forget()
    lsteele.place_forget()
    lveryscary.place_forget()
    lkotbully.place_forget()
    lkotdynia.place_forget()
    score.place(y=20, x=860)
    upgrades.place(y=340, x=20)
    roulette.place(y=480, x=20)
    settings.place(y=620, x=20)
    frame.place(y=200, x=560)
    clicker.pack()

def adjust_volume(val):
    global current_volume
    current_volume = int(val)
    volume = current_volume / 100
    pygame.mixer.music.set_volume(volume)
def menu():
    global song_skip , slider , slider_value ,window_open3
    if window_open3:
        return
    window_open3 = True
    menuwindow = tk.Toplevel(w)
    menuwindow.attributes('-topmost', True)
    menuwindow.title("Menu :3")
    menuwindow.config(bg='black')
    menuwindow.geometry("400x300")
    volume_slider = tk.Scale(menuwindow, from_=0, to=100, orient="horizontal", label="Volume", command=adjust_volume)
    volume_slider.set(current_volume)
    volume_slider.config(fg="white", font=('yugothicuisemibold', 10), bg="#A900D1")
    song_skip = tk.Button(menuwindow, text='skip song' , command=play_next_song  )
    song_skip.config(fg="white", font=('yugothicuisemibold', 10), bg="#A900D1")
    song_skip.pack()
    volume_slider.pack()
    def menu_closed():
        global window_open3
        window_open3 = False
        menuwindow.destroy()
    menuwindow.protocol('WM_DELETE_WINDOW', menu_closed)

def menu2():
    global song_skip , slider , slider_value , window_open3
    if window_open3:
        return
    window_open3 = True
    menuwindow = tk.Toplevel(w)
    menuwindow.attributes('-topmost', True)
    menuwindow.config(bg='black')
    menuwindow.title("Menu :3")
    menuwindow.geometry("400x300")
    volume_slider = tk.Scale(menuwindow, from_=0, to=100, orient="horizontal", label="Volume", command=adjust_volume)
    volume_slider.set(current_volume)
    volume_slider.config(fg="white",font=('yugothicuisemibold', 10), bg="#A900D1")
    song_skip = tk.Button(menuwindow, text='skip song' , command=play_next_song  )
    song_skip.config(fg="white",font=('yugothicuisemibold', 10), bg="#A900D1")
    song_skip.pack()
    volume_slider.pack()
    def menu_closed():
        global window_open3
        window_open3 = False
        menuwindow.destroy()
    menuwindow.protocol('WM_DELETE_WINDOW', menu_closed)
def quit():
    w.destroy()

def test():
    messagebox.showinfo("showinfo", "Information")


                                                              # CILICKER

def scorea():
    global points, x, y
    points = points + pointonclick
    score.config(text="Score:" + str(points))
    x = random.randint(0, 1200 - 250)
    y = random.randint(0, 700 - 200)
    clicker.place(x=x, y=y)

def scoreabonus():
    global points, x, y
    points = points + bonupointonclick
    score.config(text="Score:" + str(points))
    x = random.randint(0, 1200 - 250)
    y = random.randint(0, 700 - 200)
    clickerbonus.place(x=x, y=y)

def scoreabonusforget():
    clickerbonus.place_forget()

def scoreabonusremember():
    global x , y
    x = random.randint(0, 1200 - 250)
    y = random.randint(0, 700 - 200)
    clickerbonus.place(x=x, y=y)
    frame.after(6000, scoreabonusforget)

                                                                     # upgrades

def upgrades():
    global clickbutton
    global window_open
    global clickpersbutton
    global La_bandito, pumpkin_cat, devil_cat, Jinx_image, witch_cat, scary_uni, halloween_miku, serjmybeloved, space, space1, space2, hallohevenb , hallowseveb , werewolfb , lesbb , darkentriesb , painb , idontwanna , gravityb , autismb , astolfob , eepyb
    if window_open:
        return
    window_open = True
    upgradeswindow = tk.Toplevel(w)
    upgradeswindow.attributes('-topmost', True)
    upgradeswindow.title("Uprgrades :3")
    upgradeswindow.geometry("400x800")
    upgradeswindow.config(bg='black')
    space1 = tk.Label(upgradeswindow, text='upgrades', fg="white", font=('yugothicuisemibold', 10), bg="#A900D1")
    clickbutton = tk.Button(upgradeswindow, text='adds 1 more point per click price:' + str(upgradeclick),command=clickbuttons, fg="white", font=('yugothicuisemibold', 10), bg="#A900D1")
    clickpersbutton = tk.Button(upgradeswindow, text='adds 1 more point per second price:' + str(upgradeautoclick), command=upgradeautoclicks, fg="white", font=('yugothicuisemibold', 10), bg="#A900D1")
    space = tk.Label(upgradeswindow, text='images', fg="white", font=('yugothicuisemibold', 10), bg="#A900D1")
    Jinx_image = tk.Button(upgradeswindow, text=textoxoxoxoxox, fg="white",font=('yugothicuisemibold', 10), bg="#A900D1", command=jinxbuy)
    autismb = tk.Button(upgradeswindow, text=textoxoxoxoxo, fg="white",font=('yugothicuisemibold', 10), bg="#A900D1", command=autismbuy)
    pumpkin_cat = tk.Button(upgradeswindow, text=textoxoxoxox,fg="white", font=('yugothicuisemibold', 10), bg="#A900D1", command=pumpkinbuy)
    devil_cat = tk.Button(upgradeswindow, text=textoxoxoxo,fg="white", font=('yugothicuisemibold', 10), bg="#A900D1", command=devilbuy)
    witch_cat = tk.Button(upgradeswindow, text=textoxoxox, fg="white",font=('yugothicuisemibold', 10), bg="#A900D1", command=witchbuy)
    scary_uni = tk.Button(upgradeswindow, text=textoxoxo,fg="white", font=('yugothicuisemibold', 10), bg="#A900D1", command=unibuy)
    eepyb = tk.Button(upgradeswindow, text=textoxoxoxoxoxo,fg="white", font=('yugothicuisemibold', 10), bg="#A900D1", command=eepybuy)
    halloween_miku = tk.Button(upgradeswindow, text=textoxox,fg="white", font=('yugothicuisemibold', 10), bg="#A900D1", command=mikubuy)
    serjmybeloved = tk.Button(upgradeswindow, text=textoxo,fg="white", font=('yugothicuisemibold', 10), bg="#A900D1", command=serjbuy)
    astolfob = tk.Button(upgradeswindow, text=texto,fg="white", font=('yugothicuisemibold', 10), bg="#A900D1", command=astolfobuy)
    La_bandito = tk.Button(upgradeswindow, text=textox, fg="white",font=('yugothicuisemibold', 10), bg="#A900D1", command=banditobuy)
    space2 = tk.Label(upgradeswindow, text='Songs', fg="white", font=('yugothicuisemibold', 10), bg="#A900D1")
    hallohevenb = tk.Button(upgradeswindow, text=muscio, fg="white",font=('yugothicuisemibold', 10), bg="#A900D1", command=hallohevenbuy)
    hallowseveb = tk.Button(upgradeswindow, text=musciox, fg="white",font=('yugothicuisemibold', 10), bg="#A900D1", command=hallowsevebuy)
    werewolfb = tk.Button(upgradeswindow, text=muscioxo, fg="white",font=('yugothicuisemibold', 10), bg="#A900D1", command=werewolfbuy)
    lesbb = tk.Button(upgradeswindow, text=muscioxox, fg="white",font=('yugothicuisemibold', 10), bg="#A900D1", command=lesbbuy)
    darkentriesb = tk.Button(upgradeswindow, text=muscioxoxo, fg="white",font=('yugothicuisemibold', 10), bg="#A900D1", command=darkentriesbuy)
    painb =  tk.Button(upgradeswindow, text=muscioxoxox, fg="white",font=('yugothicuisemibold', 10), bg="#A900D1", command=painbuy)
    idontwanna =  tk.Button(upgradeswindow, text=muscioxoxoxo, fg="white",font=('yugothicuisemibold', 10), bg="#A900D1", command=idontwannabuy)
    gravityb =  tk.Button(upgradeswindow, text=muscioxoxoxox, fg="white",font=('yugothicuisemibold', 10), bg="#A900D1", command=gravitybuy)
    space1.pack()
    clickbutton.pack()
    clickpersbutton.pack()
    space.pack()
    Jinx_image.pack()
    autismb.pack()
    pumpkin_cat.pack()
    devil_cat.pack()
    witch_cat.pack()
    scary_uni.pack()
    eepyb.pack()
    halloween_miku.pack()
    serjmybeloved.pack()
    astolfob.pack()
    La_bandito.pack()
    space2.pack()
    hallohevenb.pack()
    hallowseveb.pack()
    werewolfb.pack()
    lesbb.pack()
    darkentriesb.pack()
    painb.pack()
    idontwanna.pack()
    gravityb.pack()
    def upgrades_closed():
        global window_open
        window_open = False
        upgradeswindow.destroy()
    upgradeswindow.protocol('WM_DELETE_WINDOW', upgrades_closed)
def gravitybuy():
    global points , muscioxoxoxox
    if points < 800:
        messagebox.showinfo('error', 'you dont have enough mons')
    else:
        muscioxoxoxox = 'you have bought Gravity'
        music.append("mp3/Gravity.mp3")
        points = points - 800
        score.config(text="Score:" + str(points))
        gravityb.config(text=muscioxoxoxox, command='null')
def idontwannabuy():
    global points , muscioxoxoxo
    if points < 700:
        messagebox.showinfo('error', 'you dont have enough mons')
    else:
        muscioxoxoxo = 'you have bought I Dont Wanna Be Me'
        music.append("mp3/I Don't Wanna Be Me.mp3")
        points = points - 700
        score.config(text="Score:" + str(points))
        idontwanna.config(text=muscioxoxoxo, command='null')
def painbuy():
    global points , muscioxoxox
    if points < 600:
        messagebox.showinfo('error', 'you dont have enough mons')
    else:
        muscioxoxox = 'you have bought Pain'
        music.append("mp3/Pain.mp3")
        points = points - 600
        score.config(text="Score:" + str(points))
        painb.config(text=muscioxoxox, command='null')
def darkentriesbuy():
    global points , muscioxoxo
    if points < 500:
        messagebox.showinfo('error', 'you dont have enough mons')
    else:
        muscioxoxo = 'you have bought Dark Entries'
        music.append("mp3/Bauhaus - Dark Entries.mp3")
        points = points - 500
        score.config(text="Score:" + str(points))
        darkentriesb.config(text=muscioxoxo, command='null')
def lesbbuy():
    global points , muscioxox
    if points < 400:
        messagebox.showinfo('error', 'you dont have enough mons')
    else:
        muscioxox = 'you have bought Lesbian Vampyres From Outer Space'
        music.append("mp3/LesbianVampyresFromOuterSpace.mp3")
        points = points - 400
        score.config(text="Score:" + str(points))
        lesbb.config(text=muscioxox, command='null')
def werewolfbuy():
    global points , muscioxo
    if points < 300:
        messagebox.showinfo('error', 'you dont have enough mons')
    else:
        muscioxo = 'you have bought Werewolfe'
        music.append("mp3/Werewolfe.mp3")
        points = points - 300
        score.config(text="Score:" + str(points))
        werewolfb.config(text=muscioxo, command='null')
def hallowsevebuy():
    global points , musciox
    if points < 200:
        messagebox.showinfo('error', 'you dont have enough mons')
    else:
        musciox = 'you have bought All Hallows Eve'
        music.append("mp3/All Hallows Eve.mp3")
        points = points - 200
        score.config(text="Score:" + str(points))
        hallowseveb.config(text=musciox , command='null')
def hallohevenbuy():
    global points , muscio
    if points < 100:
        messagebox.showinfo('error', 'you dont have enough mons')
    else:
        muscio = 'you have bought halloween in heaven'
        music.append("mp3/Halloween in Heaven.mp3")
        points = points - 100
        score.config(text="Score:" + str(points))
        hallohevenb.config(text=muscio , command='null')
def jinxbuy():
    global points, jinxbought , textoxoxoxoxox
    if points < 250 and jinxbought == False:
        messagebox.showinfo('error', 'you dont have enough mons')
    else:
        textoxoxoxoxox = 'jinx the cat has been bought (click to change image)'
        if jinxbought != True:
            points = points - 250
            score.config(text="Score:" + str(points))
        Jinx_image.config(text=textoxoxoxoxox)
        clicker.config(image=jinx_cat)
        jinxbought = True
def autismbuy():
    global points, autismbought , textoxoxoxoxo
    if points < 350 and autismbought == False:
        messagebox.showinfo('error', 'you dont have enough mons')
    else:
        textoxoxoxoxo = 'autumn cat has bought (click to change image)'
        if jinxbought != True:
            points = points - 350
            score.config(text="Score:" + str(points))
            autismb.config(text=textoxoxoxoxo)
        clicker.config(image=autism)
        autismbought = True
def pumpkinbuy():
    global points, pumpkinbought , textoxoxoxox
    if points < 400 and pumpkinbought == False:
        messagebox.showinfo('error', 'you dont have enough mons')
    else:
        textoxoxoxox = 'cute pumpkin cat bought (click to change image)'
        if pumpkinbought != True:
            points = points - 400
            score.config(text="Score:" + str(points))
        pumpkin_cat.config(text=textoxoxoxox)
        clicker.config(image=cute_pumpkin)
        pumpkinbought = True
def devilbuy():
    global points, devilbought , textoxoxoxo
    if points < 900 and devilbought == False:
        messagebox.showinfo('error', 'you dont have enough mons')
    else:
        textoxoxoxo = 'true devil cat bought (click to change image)'
        if devilbought != True:
            points = points - 900
            score.config(text="Score:" + str(points))
        devil_cat.config(text=textoxoxoxo)
        clicker.config(image=devil_cato)
        devilbought = True
def witchbuy():
    global points, witchbought , textoxoxox
    if points < 1400 and witchbought == False:
        messagebox.showinfo('error', 'you dont have enough mons')
    else:
        textoxoxox = 'witch cat bought (click to change image)'
        if witchbought != True:
            points = points - 1400
            score.config(text="Score:" + str(points))
        witch_cat.config(text=textoxoxox)
        clicker.config(image=witchcat)
        witchbought = True
def unibuy():
    global points, unibought , textoxoxo
    if points < 2000 and unibought == False:
        messagebox.showinfo('error', 'you dont have enough mons')
    else:
        textoxoxo = 'uni the cat bought (click to change image)'
        if unibought != True:
            points = points - 2000
            score.config(text="Score:" + str(points))
        scary_uni.config(text=textoxoxo)
        clicker.config(image=scaryuni)
        unibought = True
def eepybuy():
    global points, eepybought, textoxox
    if points < 3000 and eepybought == False:
        messagebox.showinfo('error', 'you dont have enough mons')
    else:
        textoxoxoxoxoxo = 'miku has been bought (click to change image)'
        if eepybought != True:
            points = points - 3000
            score.config(text="Score:" + str(points))
        eepyb.config(text=textoxoxoxoxoxo)
        clicker.config(image=sleepy)
        eepybought = True
def mikubuy():
    global points, mikubought , textoxox
    if points < 4000 and unibought == False:
        messagebox.showinfo('error', 'you dont have enough mons')
    else:
        textoxox = 'miku has been bought (click to change image)'
        if mikubought != True:
            points = points - 4000
            score.config(text="Score:" + str(points))
        halloween_miku.config(text=textoxox)
        clicker.config(image=halloweenmiku)
        mikubought = True
def serjbuy():
    global points, serjbought , textoxo
    if points < 8400 and serjbought == False:
        messagebox.showinfo('error', 'you dont have enough mons')
    else:
        textoxo = 'serj has been bought (click to change image)'
        if serjbought != True:
            points = points - 8400
            score.config(text="Score:" + str(points))
        serjmybeloved.config(text=textoxo)
        clicker.config(image=serj)
        serjbought = True
def banditobuy():
    global points, banditobought , textox
    if points < 1000000 and banditobought == False:
        messagebox.showinfo('error', 'you dont have enough mons')
    else:
        textox = 'El bandito has been bought (click to change image)'
        if banditobought != True:
            points = points - 1000000
            score.config(text="Score:" + str(points))
        La_bandito.config(text=textox)
        clicker.config(image=bandito)
        banditobought = True
def astolfobuy():
    global points, astolfobought, texto
    if points < 500000 and astolfobought == False:
        messagebox.showinfo('error', 'you dont have enough mons')
    else:
        texto = 'Astolfo has been bought (click to change image)'
        if astolfobought != True:
            points = points - 500000
            score.config(text="Score:" + str(points))
        astolfob.config(text=texto)
        clicker.config(image=astolfo)
        astolfobought = True
def clickbuttons():
    global points
    global upgradeclick
    global pointonclick
    if points >= upgradeclick:
        points = points - upgradeclick
        pointonclick = pointonclick + 1
        score.config(text="Score:" + str(points))
        upgradeclick = upgradeclick * Costmulti
        clickbutton.config(text='adds 1 more point per click price:' + str(upgradeclick))
    else:
        messagebox.showinfo("Click some more", "You are too poor")

def upgradeautoclicks():
    global points
    global upgradeautoclick
    global clickpersbutton
    global autoclick
    if points >= upgradeautoclick:
        points = points - upgradeautoclick
        score.config(text="Score:" + str(points))
        upgradeautoclick = upgradeautoclick * Costmulti
        clickpersbutton.config(text='adds 1 more point per second price:' + str(upgradeautoclick))
        autoclick = autoclick + 1
    else:
        messagebox.showinfo("Click some more", "You are too poor")


def upgradeautoclicks2():
    global points
    global autoclick
    points = points + autoclick
    score.config(text="Score:" + str(points))
    w.after(1000, upgradeautoclicks2)


                                                                        #Jumpscares


def jumpscare1f():
    global timeo,  jumpscareo1, humpscarp
    timeo = random.randint(500000, 7000000)
    humpscarp = random.randint(1, 4)
    humpscarp = 4
    if humpscarp == 1:
        jumpscareo1.place(x=350, y=10)
        w.update_idletasks()
        pygame.mixer.Sound.play(boom)
        jumpscareo1.after(3000, jumpscero1forget)
        w.after(timeo, jumpscare1f)
    elif humpscarp == 2:
        jumpscareo2.place(x=350, y=10)
        w.update_idletasks()
        pygame.mixer.Sound.play(boom)
        jumpscareo1.after(3000, jumpscero1forget)
        w.after(timeo, jumpscare1f)
    elif humpscarp == 3:
        jumpscareo3.place(x=350, y=10)
        w.update_idletasks()
        pygame.mixer.Sound.play(boom)
        jumpscareo1.after(3000, jumpscero1forget)
        w.after(timeo, jumpscare1f)
    else :
        jumpscareo4.place(x=350, y=10)
        w.update_idletasks()
        pygame.mixer.Sound.play(kys)
        jumpscareo1.after(3000, jumpscero1forget)
        w.after(timeo, jumpscare1f)


def jumpscero1forget():
    jumpscareo1.place_forget()
    jumpscareo2.place_forget()
    jumpscareo3.place_forget()
    jumpscareo4.place_forget()


                                                                        # Main page


l1 = tk.Label(w, text="Spooky Scary Gato Clicker", bg='black', fg="#A900D1")
l1.config(font=('yugothicuisemibold', 55, "bold"))
start = tk.Button(
    text='Start',
    fg="white",
    font=('yugothicuisemibold', 50,),
    bg='#A900D1',
    command=start,
    border=0,
    width=18,
)
menu = tk.Button(
    text='Settings',
    fg="white",
    font=('yugothicuisemibold', 50,),
    bg='#A900D1',
    command=menu,
    border=0,
    width=18,
)
quit = tk.Button(
    text='Quit',
    fg="white",
    font=('yugothicuisemibold', 50,),
    bg='#A900D1',
    command=quit,
    border=0,
    width=18,
)
frame = tk.Frame(w, width=1200, height=700, bg='black')
frame.pack_propagate(False)
frame.place_forget()
score = tk.Label(w, text="Score:" + str(points), fg="white", font=('yugothicuisemibold', 40,), bg='#A900D1', border=0,
                 width=10)
score.place_forget()
upgrades = tk.Button(w, text='Upgrades', command=upgrades, fg="white", font=('yugothicuisemibold', 40,), bg='#A900D1',
                     border=0, width=10)
upgrades.place_forget()
roulette = tk.Button(w, text='Roulette', command=roulette, fg="white", font=('yugothicuisemibold', 40,), bg='#A900D1',
                     border=0, width=10)
roulette.place_forget()
settings = tk.Button(w, text='Settings', command=menu2, fg="white", font=('yugothicuisemibold', 40,), bg='#A900D1',
                     border=0, width=10)
settings.place_forget()
clicker = tk.Button(frame, image=clickerzdj, command=scorea, border=0)
clicker.place_forget()
clickerbonus = tk.Button(frame, image=bonuszdj, command=scoreabonus, border=0)
clickerbonus.place_forget()
jumpscareo1 = tk.Label(w, image=jumpscareo1zdj)
jumpscareo1.place_forget()
jumpscareo2 = tk.Label(w, image=jumpscareo2zdj)
jumpscareo2.place_forget()
jumpscareo3 = tk.Label(w, image=jumpscareo3zdj)
jumpscareo3.place_forget()
jumpscareo4 = tk.Label(w, image=jumpscareo4zdj)
jumpscareo4.place_forget()
l2 = tk.Label(w, text="Gambling Update !!", bg='black', fg="#A900D1")
l2.config(font=('yugothicuisemibold', 20, "bold"))
lveryscary = tk.Label(w, image=veryscary, border=0)
lkotdynia = tk.Label(w, image=kotdynia, border=0)
lkotbully = tk.Label(w, image=kotbully, border=0)
lsteele = tk.Label(w, image=steele, border=0)
podpis = tk.Label(w, text="yes", bg='black', fg="#A900D1")
podpis.config(font=('yugothicuisemibold', 14,))
peeter = tk.Label(w, text="A good metal band", bg='black', fg="#0cda00")
peeter.config(font=('yugothicuisemibold', 14,))
peeter.place(x=166, y=310)
lsteele.place(x=110, y=20)
podpis.place(x=50, y=980)
lveryscary.place(x=1500, y=400)
lkotbully.place(x=50, y=396)
lkotdynia.place(x=1450, y=600)
l1.place(x=500, y=80)
l2.place(x=840, y=200)
start.place(x=610, y=400)
menu.place(x=610, y=600)
quit.place(x=610, y=800)
upgradeautoclicks2()
w.after(10000, jumpscare1f)
frame.after(18000 , scoreabonusremember)
pygame.mixer.music.load(music[current_song_index])
pygame.mixer.music.play()
w.mainloop()