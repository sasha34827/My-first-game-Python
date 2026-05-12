import time
from tkinter import *
from time import *

root = Tk()
root.title('Кликер')
root.geometry('500x500')
root.resizable(width=False, height=False)
root['bg'] = '#efcaa3'

click_all = 0
point = 0
lvl_click = 1
bonus = 0
sled_lvl = None
price = 20
lvl_autof = 1
price_lvl_autof = 5000
sec = 15
green = False
price_green = 1000
price_blue = 1000
blue = False
up_sec_lvl = 1
h = '#f0a594'
xxx = 1
green_theme = False
blue_theme = False

def apply_theme_to_window(window, theme):
    if theme == 'blue':
        window.configure(bg='#7cc8f8')
        for child in window.winfo_children():
            if isinstance(child, Label):
                child.config(bg='#7cc8f8', fg='#1385cd')
            elif isinstance(child, Button):
                child.config(bg='#489eef', activebackground='#2472a3')
    elif theme == 'green':
        window.configure(bg='#c7f6ac')
        for child in window.winfo_children():
            if isinstance(child, Label):
                child.config(bg='#c7f6ac', fg='#51ac4d')
            elif isinstance(child, Button):
                child.config(bg='#91f08f', activebackground='#51ac4d')

def wkl_design_b():
    global xxx, blue_theme
    blue_theme = True
    green_theme = False
    xxx = 2
    root.configure(bg='#7cc8f8')
    lable_kogda_autof.config(bg='#7cc8f8')
    lable_poluchenie.config(bg='#7cc8f8')
    lable_point.config(bg='#7cc8f8')
    lable_ostalos.config(bg='#7cc8f8')
    lable_lvl.config(bg='#7cc8f8')
    st.config(bg='#489eef', activebackground='#2472a3')
    ak.config(bg='#489eef', activebackground='#2472a3')
    p.config(bg='#489eef', activebackground='#2472a3')
    autof.config(bg='#489eef', activebackground='#2472a3')
    shop_open.config(bg='#489eef', activebackground='#2472a3')
    lable_kogda_autof.config(fg='#1385cd')
    lable_point.config(fg='white')
    lable_ostalos.config(fg='#1385cd')
    lable_lvl.config(fg='#1385cd')
    lable_poluchenie.config(fg='#1385cd')

def wkl_design_g():
    global xxx, green_theme
    green_theme = True
    blue_theme = False
    xxx = 3
    root.configure(bg='#c7f6ac')
    lable_kogda_autof.config(bg='#c7f6ac')
    lable_poluchenie.config(bg='#c7f6ac')
    lable_point.config(bg='#c7f6ac')
    lable_ostalos.config(bg='#c7f6ac')
    lable_lvl.config(bg='#c7f6ac')
    st.config(bg='#91f08f', activebackground='#51ac4d')
    ak.config(bg='#91f08f', activebackground='#51ac4d')
    p.config(bg='#91f08f', activebackground='#51ac4d')
    autof.config(bg='#91f08f', activebackground='#51ac4d')
    shop_open.config(bg='#91f08f', activebackground='#51ac4d')
    lable_kogda_autof.config(fg='#51ac4d')
    lable_point.config(fg='white')
    lable_ostalos.config(fg='#51ac4d')
    lable_lvl.config(fg='#51ac4d')
    lable_poluchenie.config(fg='#51ac4d')

def open_store():
    global point, green, blue, green_theme, blue_theme
    shop = Toplevel(root)
    shop.title('Магазин')
    shop.geometry('1000x500')
    shop.resizable(width=False, height=False)
    shop['bg'] = '#efcaa3'

    if blue_theme:
        apply_theme_to_window(shop, 'blue')
    elif green_theme:
        apply_theme_to_window(shop, 'green')

    def buy_design_green():
        global point, green
        if not green:
            if point >= price_green:
                point -= price_green
                green = True
                lable_point.config(text=str(point))
                buy_design_g.config(text='Зеленый дизайн\nПриобретено', bg='#71f47f', fg='#2e7035')

    def buy_design_blue():
        global point, blue
        if not blue:
            if point >= price_blue:
                point -= price_blue
                blue = True
                lable_point.config(text=str(point))
                buy_design_b.config(text='Синий дизайн\nПриобретено', bg='#71f47f', fg='#2e7035')

                def apply_blue_theme():
                    wkl_design_b()
                    shop.configure(bg='#7cc8f8')
                    wkl_blue.config(bg='#489eef', activebackground='#2472a3')

                wkl_blue = Button(shop, text='Включить', bg='#e6b27f', fg='black',
                                  activebackground='#97724e', font=('Arial', 20, 'bold'),
                                  command=apply_blue_theme, padx=1, pady=3)
                wkl_blue.place(relx=0.5, rely=0.7, anchor=CENTER)

    def buy_design_green_theme():
        global point, green_theme
        if not green_theme:
            if point >= 1000:
                point -= 1000
                green_theme = True
                lable_point.config(text=str(point))
                buy_design_green_theme_btn.config(text='Зеленый дизайн\nПриобретено', bg='#71f47f', fg='#2e7035')

                def apply_green_theme():
                    wkl_design_g()
                    shop.configure(bg='#c7f6ac')
                    wkl_green.config(bg='#91f08f', activebackground='#51ac4d')

                wkl_green = Button(shop, text='Включить', bg='#e6b27f', fg='black',
                                   activebackground='#97724e', font=('Arial', 20, 'bold'),
                                   command=apply_green_theme, padx=1, pady=3)
                wkl_green.place(relx=0.2, rely=0.7, anchor=CENTER)

    #buy_design_g = Button(shop, text='Зеленый дизайн\nЦена: 1000', bg='#7d7d7d', fg='white',
    #                      font=('Arial', 20, 'bold'), command=buy_design_green, padx=1, pady=3)
    #buy_design_g.place(relx=0.2, rely=0.5, anchor=CENTER)

    buy_design_b = Button(shop, text='Синий дизайн\nЦена: 1000', bg='#7d7d7d', fg='white',
                          font=('Arial', 20, 'bold'), command=buy_design_blue, padx=1, pady=3)
    buy_design_b.place(relx=0.5, rely=0.5, anchor=CENTER)

    buy_design_green_theme_btn = Button(shop, text='Зеленый дизайн\nЦена: 1000', bg='#7d7d7d', fg='white',
                                        font=('Arial', 20, 'bold'), command=buy_design_green_theme, padx=1, pady=3)
    buy_design_green_theme_btn.place(relx=0.2, rely=0.5, anchor=CENTER)

def open_state():
    global click_all
    state = Toplevel(root)
    state.title('Статистика')
    state.geometry('500x500')
    state.resizable(width=False, height=False)

    if blue_theme:
        apply_theme_to_window(state, 'blue')
    elif green_theme:
        apply_theme_to_window(state, 'green')
    else:
        state['bg'] = '#efcaa3'

    lable_state = Label(state, text=f'Все ваши клики: {click_all}\nчтоб обновить статистику - перезапустите окно',
                        bg=state['bg'], fg='#c9864f', font=('Arial', 15, 'bold'))
    lable_state.place(relx=0.5, rely=0.5, anchor=CENTER)

def open_farm_window():
    global sec, lvl_autof, price_lvl_autof, point
    farm_win = Toplevel(root)
    farm_win.title('АВТОФЕРМА')
    farm_win.geometry('500x500')
    farm_win.resizable(width=False, height=False)

    if blue_theme:
        apply_theme_to_window(farm_win, 'blue')
    elif green_theme:
        apply_theme_to_window(farm_win, 'green')
    else:
        farm_win['bg'] = '#efcaa3'

    def auto_money():
        global point
        point += sec * lvl_autof * 2
        lable_point.config(text=str(point))
        root.after(1000, auto_money)

    def upgrade_farm():
        global point, lvl_autof, price_lvl_autof, sec
        if point >= price_lvl_autof:
            point -= price_lvl_autof
            lvl_autof += 1
            sec = int(sec * 1.2)
            price_lvl_autof = int(price_lvl_autof * 1.3)
            farm_win.leble_zarobotok.config(text=f'В секунду ферма приносит {sec * lvl_autof * 2} монет')
            farm_win.leble_lvlaf.config(text=f'Уровень вашей фермы: {lvl_autof}')
            farm_win.sled_lvl.config(text=f'Цена следующего уровня фермы: {price_lvl_autof}')
            lable_point.config(text=str(point))

    def buy_farm():
        global point, lvl_autof, price_lvl_autof, sec
        if point >= 10000:
            point -= 10000
            lable_point.config(text=str(point))
            buy_autof.destroy()
            root.after(1000, auto_money)

            farm_win.leble_zarobotok = Label(farm_win, text=f'В секунду ферма приносит {sec * lvl_autof * 2} монет',
                                             bg=farm_win['bg'], fg='#c9864f', font=('Arial', 15, 'bold'))
            farm_win.leble_zarobotok.place(relx=0.5, rely=0.5, anchor=CENTER)

            farm_win.sled_lvl = Label(farm_win, text=f'Цена следующего уровня фермы: {price_lvl_autof}',
                                      bg=farm_win['bg'], fg='#c9864f', font=('Arial', 15, 'bold'))
            farm_win.sled_lvl.place(relx=0.5, rely=0.55, anchor=CENTER)

            farm_win.leble_lvlaf = Label(farm_win, text=f'Уровень вашей фермы: {lvl_autof}',
                                         bg=farm_win['bg'], fg='#c9864f', font=('Arial', 15, 'bold'))
            farm_win.leble_lvlaf.place(relx=0.5, rely=0.6, anchor=CENTER)

            farm_win.upgrade_btn = Button(farm_win, text="Купить следующий уровень фермы",
                                          bg='#e6b27f', activebackground='#97724e', fg='black',
                                          font=('Arial', 18, 'bold'), command=upgrade_farm)
            farm_win.upgrade_btn.place(relx=0.5, rely=0.7, anchor=CENTER)

    close_btn = Button(farm_win, text="Закрыть", bg='#e6b27f', activebackground='#97724e',
                       fg='black', font=('Arial', 10, 'bold'), command=farm_win.destroy)
    close_btn.place(relx=0.93, rely=0.03, anchor=CENTER)

    buy_autof = Button(farm_win, text="Купить ферму за 10000", bg='#e6b27f',
                       activebackground='#97724e', fg='black', font=('Arial', 20, 'bold'),
                       command=buy_farm)
    buy_autof.place(relx=0.5, rely=0.5, anchor=CENTER)

def prov_10_lvl():
    if lvl_click >= 10:
        lable_kogda_autof.config(text='')
        autof.place(relx=0, rely=0)

def proverka():
    global point, xxx
    if point < price:
        if xxx == 2:
            p.config(bg='#489eef')
        elif xxx == 3:
            p.config(bg='#91f08f')
        else:
            p.config(bg='#f0a594')
    else:
        if xxx == 2:
            p.config(bg='#489eef')
        elif xxx == 3:
            p.config(bg='#91f08f')
        else:
            p.config(bg='#e6b27f')

def price_update():
    global price
    price = int(20 * lvl_click * lvl_click)
    lable_ostalos.config(text=f'Для прокачки нужно: {price} монет')

def lvl_click_update():
    global lvl_click, bonus
    if lvl_click >= 35:
        bonus = 25
    elif lvl_click >= 25:
        bonus = 17
    elif lvl_click >= 20:
        bonus = 13
    elif lvl_click >= 15:
        bonus = 10
    elif lvl_click >= 10:
        bonus = 6
    elif lvl_click >= 7:
        bonus = 4
    elif lvl_click >= 4:
        bonus = 2
    lable_poluchenie.config(text=f'Монет за клик: {lvl_click + bonus}')

def lvl():
    global lvl_click
    lable_lvl.config(text=f'Ваш уровень: {lvl_click}')

def prokachka():
    global point, lvl_click
    if point >= price:
        point -= price
        lvl_click += 1
        lvl_click_update()
        price_update()
        proverka()
        lvl()
        prov_10_lvl()
        lable_point.config(text=str(point))

def click():
    global point, click_all
    point += lvl_click
    click_all += 1
    if lvl_click >= 35:
        point += 25
    elif lvl_click >= 25:
        point += 17
    elif lvl_click >= 20:
        point += 13
    elif lvl_click >= 15:
        point += 10
    elif lvl_click >= 10:
        point += 6
    elif lvl_click >= 7:
        point += 4
    elif lvl_click >= 4:
        point += 2
    proverka()
    lable_point.config(text=str(point))

def secret():
    global point
    point += 10000
    lable_point.config(text=str(point))
    print("Все работает")

root.bind('<space>', lambda event: click())
root.bind('W', lambda event: secret())

lable_kogda_autof = Label(root, text='Ферма откроется на 10 уровне', bg='#efcaa3', fg='#c9864f', font=('Arial', 10, 'bold'))
lable_kogda_autof.place(relx=0.21, rely=0.02, anchor=CENTER)

lable_poluchenie = Label(root, text=f'Монет за клик: {lvl_click}', bg='#efcaa3', fg='#c9864f', font=('Arial', 10, 'bold'))
lable_poluchenie.place(relx=0.5, rely=0.65, anchor=CENTER)

lable_point = Label(root, text='0', bg='#efcaa3', fg='white', font=('Arial', 35, 'bold'))
lable_point.place(relx=0.5, rely=0.2, anchor=CENTER)

lable_ostalos = Label(root, text=f'Для прокачки нужно: {price} монет', bg='#efcaa3', fg='#c9864f', font=('Arial', 10, 'bold'))
lable_ostalos.place(relx=0.5, rely=0.7, anchor=CENTER)

lable_lvl = Label(root, text=f'Ваш уровень: {lvl_click}', bg='#efcaa3', fg='#c9864f', font=('Arial', 10, 'bold'))
lable_lvl.place(relx=0.5, rely=0.6, anchor=CENTER)

st = Button(root, text='Статистика', bg='#e6b27f', activebackground='#97724e',
            font=('Arial', 20, 'bold'), padx=1, pady=1, command=open_state)
st.place(relx=0.81, rely=0.07, anchor=CENTER)

ak = Button(root, text='КЛИК', bg='#e6b27f', activebackground='#97724e',
            font=('Arial', 20, 'bold'), padx=5, pady=5, command=click)
ak.place(relx=0.5, rely=0.5, anchor=CENTER)

p = Button(root, text='Новый уровень клика', bg=h, activebackground='#97724e',
           font=('Arial', 20, 'bold'), padx=5, pady=5, command=prokachka)
p.place(relx=0.5, rely=0.8, anchor=CENTER)

autof = Button(root, text='АВТОФЕРМА', bg='#e6b27f', activebackground='#97724e',
               font=('Arial', 20, 'bold'), padx=5, pady=5, command=open_farm_window)
autof.place(relx=-1, rely=-1)

shop_open = Button(root, text='Магазин', bg='#e6b27f', activebackground='#97724e',
                   font=('Arial', 20, 'bold'), padx=5, pady=5, command=open_store)
shop_open.place(relx=0.7, rely=0.14)

root.mainloop()