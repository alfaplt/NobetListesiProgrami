# -*- coding: utf-8 -*-
import tkinter.messagebox as tkmsg
import tkinter as tk
import datetime
import random

list_of_months = ["OCAK", "ŞUBAT", "MART", "NİSAN", "MAYIS", "HAZİRAN", "TEMMUZ", "AĞUSTOS", "EYLÜL", "EKIM", "KASIM", "ARALIK"]
number_of_days_list = {"OCAK":31, "ŞUBAT":28, "MART":31, "NİSAN":30, "MAYIS":31, "HAZİRAN":30, "TEMMUZ":31, "AĞUSTOS":31, "EYLÜL":30, "EKIM":31, "KASIM":30, "ARALIK":31}
today = datetime.date.today()

#  if not pick a month
current_month = list_of_months[today.month]       
previous_month = list_of_months[today.month - 1]

current_month_number_of_days = number_of_days_list[current_month]
previous_month_number_of_days = number_of_days_list[previous_month]
pmnod = previous_month_number_of_days
cmnod = current_month_number_of_days

###########################################################################
class GUI:

    def __init__(self):
        self.widgets()

    def widgets(self):
        global temporary_rule1
        global temporary_rule2
        global temporary_rule3
        global temporary_rule4
        temporary_rule1 = 1
        temporary_rule2 = 1
        temporary_rule3 = 1
        temporary_rule4 = 1

        def rule_picker():
            global temporary_rule1
            global temporary_rule2
            global temporary_rule3
            global temporary_rule4
            temporary_rule1 = rule_checkbutton1_variable.get()
            temporary_rule2 = rule_checkbutton2_variable.get()
            temporary_rule3 = rule_checkbutton3_variable.get()
            temporary_rule4 = rule_checkbutton4_variable.get()
            
        def select_months_radiobutton():
            
            def month_picker():
                global current_month
                global previous_month
                global pmnod
                global cmnod

                current_month = list_of_months_variable.get()
                index_of_last_month = list_of_months.index(list_of_months_variable.get())
                previous_month = list_of_months[index_of_last_month - 1]

                current_month_number_of_days = number_of_days_list[current_month]
                previous_month_number_of_days = number_of_days_list[previous_month]
                
                cmnod = current_month_number_of_days
                pmnod = previous_month_number_of_days
                
            new_window_current_month = tk.Toplevel()
            new_window_current_month.geometry(f"260x180+{(screen_width-260)//2}+{(screen_height-180)//4}")
            new_window_current_month.resizable(width=tk.FALSE, height=tk.FALSE)

            frame1 = tk.Frame(new_window_current_month)
            frame1.grid()
            
            days_label = tk.Label(frame1,text="Ayı Seçiniz")
            days_label.grid()

            frame2 = tk.Frame(new_window_current_month)
            frame2.grid(ipady=5)

            ycolumn = 0
            xrow = 1

            list_of_months_variable = tk.StringVar()
            
            list_of_months_variable.set(None)

            for i in list_of_months:
                tk.Radiobutton(frame2, text=i, variable=list_of_months_variable, value=i, command=month_picker).grid(padx=4, row=xrow, column=ycolumn)
                ycolumn += 1

                if ycolumn > 2:
                    ycolumn = 0
                    xrow += 1

            
            frame3 = tk.Frame(new_window_current_month)
            frame3.grid()

            ok_button = tk.Button(frame3, text="Seçimi Tamamla", command=new_window_current_month.destroy)
            ok_button.pack()

        def Select_wanted_days_checkbutton():
            
            def temporary_wanted_days():
                # global temporary_wanted_days_list   
                # temporary_wanted_days_list = list()  

                for i in range(1, 32):
                    if wanted_days_cb_var[i].get() == 1:
                        if i not in temporary_wanted_days_list:
                            temporary_wanted_days_list.append(i)

                    elif wanted_days_cb_var[i].get() == 0:
                        if i in temporary_wanted_days_list:
                            temporary_wanted_days_list.remove(i)
                new_window_wanted_days.destroy()


            global new_window_wanted_days
            new_window_wanted_days = tk.Toplevel()
            new_window_wanted_days.geometry(f"250x240+{(screen_width-250)//2}+{(screen_height-240)//4}")
            new_window_wanted_days.resizable(width=tk.FALSE, height=tk.FALSE)

            frame1 = tk.Frame(new_window_wanted_days)
            frame1.grid()
            
            days_label = tk.Label(frame1,text="İstenilen Günleri Seçiniz")
            days_label.grid()

            frame2 = tk.Frame(new_window_wanted_days)
            frame2.grid()

            ycolumn = 0
            xrow = 1
            
            global wanted_days_cb_var 
            wanted_days_cb_var = dict()

            for i in range(1,32):
                wanted_days_cb_var[i] = tk.IntVar()  #her cb için değişken tanımlanıyor
                tk.Checkbutton(frame2, text=i, variable=wanted_days_cb_var[i]).grid(padx=4, row=xrow, column=ycolumn)
                ycolumn += 1

                if ycolumn > 4:
                    ycolumn = 0
                    xrow += 1
            
            ok_button = tk.Button(new_window_wanted_days, text="Seçimi Tamamla", command=temporary_wanted_days).grid()

        def Select_unwanted_days_checkbutton():

            def temporary_unwanted_days():  # fonk. adını değiş
                #global temporary_unwanted_days_list
                # temporary_unwanted_days_list = list()  

                for i in range(1, 32):
                    if unwanted_days_cb_var[i].get() == 1:
                        if i not in temporary_unwanted_days_list:
                            temporary_unwanted_days_list.append(i)

                    elif unwanted_days_cb_var[i].get() == 0:
                        if i in temporary_unwanted_days_list and i not in temporary_annual_days_list:  # ilgili günde yıllık izin varsa silmiyor.
                            temporary_unwanted_days_list.remove(i)

                new_window_unwanted_days.destroy()

            global new_window_unwanted_days
            new_window_unwanted_days = tk.Toplevel()
            new_window_unwanted_days.geometry(f"250x240+{(screen_width-250)//2}+{(screen_height-240)//4}")
            new_window_unwanted_days.resizable(width=tk.FALSE, height=tk.FALSE)

            frame1 = tk.Frame(new_window_unwanted_days)
            frame1.grid()
            
            days_label = tk.Label(frame1,text="İstenmeyen Günleri Seçiniz")
            days_label.grid()

            frame2 = tk.Frame(new_window_unwanted_days)
            frame2.grid()

            ycolumn = 0
            xrow = 1

            global unwanted_days_cb_var 
            unwanted_days_cb_var = dict()

            for i in range(1,32):
                unwanted_days_cb_var[i] = tk.IntVar()
                tk.Checkbutton(frame2, text=i, variable=unwanted_days_cb_var[i]).grid(padx=4, row=xrow, column=ycolumn)
                ycolumn += 1

                if ycolumn > 4:
                    ycolumn = 0
                    xrow += 1
            
            ok_button = tk.Button(new_window_unwanted_days, text="Seçimi Tamamla", command=temporary_unwanted_days).grid()

        def Select_annual_days_checkbutton():

            def temporary_annual_days():
                #global temporary_unwanted_days_list
                # global temporary_annual_days_list
                # temporary_annual_days_list = list()  

                for i in range(1, 32):
                    if annual_days_cb_var[i].get() == 1:
                        if i not in temporary_annual_days_list:
                            temporary_annual_days_list.append(i)
                            temporary_unwanted_days_list.append(i)  # istenmeyen günlere ekleniyor

                    elif annual_days_cb_var[i].get() == 0:
                        if i in temporary_annual_days_list:
                            temporary_annual_days_list.remove(i)

                max_day_of_annual = max(temporary_annual_days_list)  #yıllık iznin son gününü, istenilen günlere ekleme
                temporary_wanted_days_list.append(max_day_of_annual + 1)

                new_window_annual_days.destroy()

            global new_window_annual_days
            new_window_annual_days = tk.Toplevel()
            new_window_annual_days.geometry(f"250x240+{(screen_width-250)//2}+{(screen_height-240)//4}")
            new_window_annual_days.resizable(width=tk.FALSE, height=tk.FALSE)

            frame1 = tk.Frame(new_window_annual_days)
            frame1.grid()
            
            days_label = tk.Label(frame1,text="İzin Günlerini Seçiniz")
            days_label.grid()

            frame2 = tk.Frame(new_window_annual_days)
            frame2.grid()

            ycolumn = 0
            xrow = 1

            global annual_days_cb_var 
            annual_days_cb_var = dict()

            for i in range(1,32):
                annual_days_cb_var[i] = tk.IntVar()
                tk.Checkbutton(frame2, text=i, variable=annual_days_cb_var[i]).grid(padx=4, row=xrow, column=ycolumn)
                ycolumn += 1

                if ycolumn > 4:
                    ycolumn = 0
                    xrow += 1
            
            ok_button = tk.Button(new_window_annual_days, text="Seçimi Tamamla", command=temporary_annual_days).grid()

        def Select_days_radiobutton():

            def temporary_last_day():
                global temporary_last_day_variable
                temporary_last_day_variable = list_of_days_variable.get()

                new_window_last_days.destroy()

            global list_of_days_variable
            new_window_last_days = tk.Toplevel()
            new_window_last_days.geometry(f"250x240+{(screen_width-250)//2}+{(screen_height-240)//4}")
            new_window_last_days.resizable(width=tk.FALSE, height=tk.FALSE)

            frame1 = tk.Frame(new_window_last_days)
            frame1.grid()
            
            days_label = tk.Label(frame1,text="Günü Seçiniz")
            days_label.grid()

            frame2 = tk.Frame(new_window_last_days)
            frame2.grid()

            ycolumn = 0
            xrow = 1

            list_of_days_variable = tk.IntVar()
            #list_of_days_variable.set(None)

            for i in range(1,32):
                tk.Radiobutton(frame2, text=i, variable=list_of_days_variable, value=i).grid(padx=4, row=xrow, column=ycolumn)
                ycolumn += 1

                if ycolumn > 4:
                    ycolumn = 0
                    xrow += 1
            
            ok_button = tk.Button(new_window_last_days, text="Seçimi Tamamla", command=temporary_last_day).grid()


        def request_detail():

            global temporary_wanted_days_list
            temporary_wanted_days_list = list()
            global temporary_unwanted_days_list
            temporary_unwanted_days_list = list()
            global temporary_annual_days_list
            temporary_annual_days_list = list()
            global temporary_last_day_variable
            temporary_last_day_variable = int()
            global temporary_personnel_group
            temporary_personnel_group = "SEÇİLMEDİ"
            global annual_leave_variable
             
            global detail_window
            detail_window = tk.Toplevel()
            detail_window.update()

            detail_window.geometry(f"260x240+{(screen_width-260)//2}+{(screen_height-240)//4}")

            frame1 = tk.Frame(detail_window)
            frame1.pack(pady=5)

            wanted_days_label = tk.Label(frame1, text="İstenilen günleri seçiniz :")
            wanted_days_label.pack(side="left", padx=5)

            wanted_days_button = tk.Button(frame1, text="Günler...", command=Select_wanted_days_checkbutton)
            wanted_days_button.pack()

            frame2 =tk.Frame(detail_window)
            frame2.pack(pady=5)

            unwanted_days_label = tk.Label(frame2, text="İstenmeyen günleri seçiniz :")
            unwanted_days_label.pack(side="left", padx=5)

            unwanted_days_button = tk.Button(frame2,text="Günler...", command=Select_unwanted_days_checkbutton)
            unwanted_days_button.pack()

            frame3 = tk.Frame(detail_window)
            frame3.pack(pady=5)

            last_workday_of_last_month_label = tk.Label(frame3, text="Geçen ayki son nöbetiniz ? :")
            last_workday_of_last_month_label.pack(side="left", padx=5)

            last_workday_of_last_month_button = tk.Button(frame3, text="Günü seçiniz...", command=Select_days_radiobutton)
            last_workday_of_last_month_button.pack()

            frame4 = tk.Frame(detail_window)
            frame4.pack(pady=5)

            annual_leave_label = tk.Label(frame4, text="Yıllık izniniz var mı ? :") 
            annual_leave_label.pack(side="left", padx=5)

            annual_leave_variable = tk.IntVar()
            annual_leave_ask2 = tk.Radiobutton(frame4, text="Var", variable=annual_leave_variable, value=1, command=Select_annual_days_checkbutton)
            annual_leave_ask2.pack(side="left")
            
            annual_leave_ask = tk.Radiobutton(frame4, text="Yok", variable=annual_leave_variable, value=0)
            annual_leave_ask.pack()

            frame5 = tk.Frame(detail_window)
            frame5.pack(pady=5)

            def personnel_group_picker():
                global temporary_personnel_group
                temporary_personnel_group = personnel_group_variable.get()

            personnel_group_label = tk.Label(frame5, text="Personel Grubu ? :")
            personnel_group_label.pack(side="left")

            personnel_group_variable = tk.StringVar()
            personnel_group_variable.set("none")

            personnel_group_radiobutton1 = tk.Radiobutton(frame5, text="AABT", variable=personnel_group_variable, value="AABT", command=personnel_group_picker)
            personnel_group_radiobutton1.pack(side="left")

            personnel_group_radiobutton2 = tk.Radiobutton(frame5, text="ATT", variable=personnel_group_variable, value="ATT", command=personnel_group_picker)
            personnel_group_radiobutton2.pack(side="left")

            personnel_group_radiobutton3 = tk.Radiobutton(frame5, text="SRC", variable=personnel_group_variable, value="SRC", command=personnel_group_picker)
            personnel_group_radiobutton3.pack(side="left")

            frame6 = tk.Frame(detail_window)
            frame6.pack(pady=10)

            personel_save_button = tk.Button(frame6, text="Personeli Kaydet", fg="red", command=Personnel.save_personnel)
            personel_save_button.pack()


        self.title = tk.Label(main_window,text="NÖBET LİSTESİ HAZIRLAMA PROGRAMI", font="DejaVuSans 18 bold", fg="red")
        self.title.pack()

        self.frame1 = tk.Frame()
        self.frame1.pack(pady=8)

        self.name_label = tk.Label(self.frame1, text="Personel İsmi ?  :  ")
        self.name_label.pack(side="left")

        self.name_entry = tk.Entry(self.frame1, bg="white")
        self.name_entry.pack()

        self.frame2 = tk.Frame()
        self.frame2.pack(pady=8)

        self.personel_details = tk.Button(self.frame2, text="Personel Detayları", command=request_detail)
        self.personel_details.pack()

        self.frame3 = tk.Frame()
        self.frame3.pack(pady=8)
        
        self.select_month_label = tk.Label(self.frame3,text="Liste Hangi Ay İçin Hazırlanıyor ?  ")
        self.select_month_label.pack(side="left")

        self.select_month_button = tk.Button(self.frame3, text="Aylar...", command=select_months_radiobutton)
        self.select_month_button.pack()

        self.frame4 = tk.Frame()
        self.frame4.pack(pady=15)

        self.information_text = tk.Label(self.frame4, text="GEÇERLİ KURALLARI İŞARETLEYİNİZ !", font="DejaVuSans 13 underline", fg="red")
        self.information_text.pack()

        frame5 = tk.Frame()
        frame5.pack()

        rule_checkbutton1_variable = tk.IntVar()
        rule_checkbutton1_variable.set(1)
        rule_checkbutton2_variable = tk.IntVar()
        rule_checkbutton2_variable.set(1)
        rule_checkbutton3_variable = tk.IntVar()
        rule_checkbutton3_variable.set(1)
        rule_checkbutton4_variable = tk.IntVar()
        rule_checkbutton4_variable.set(1)

        rule_checkbutton1 = tk.Checkbutton(frame5,text="Max 9 Gün Boşluk", variable=rule_checkbutton1_variable, command=rule_picker)
        rule_checkbutton1.pack()

        rule_checkbutton2 = tk.Checkbutton(frame5,text="Günaşırı Nöbet Yasağı", variable=rule_checkbutton2_variable, command=rule_picker)
        rule_checkbutton2.pack()

        rule_checkbutton3 = tk.Checkbutton(frame5,text="Yıllık İzin Öncesi Max 3 Gün Boşluk", variable=rule_checkbutton3_variable, command=rule_picker)
        rule_checkbutton3.pack()

        rule_checkbutton4 = tk.Checkbutton(frame5,text="Yıllık İzin Alana Fazla Mesai Yasağı", variable=rule_checkbutton4_variable, command=rule_picker)
        #rule_checkbutton4.pack()

        self.frame6 = tk.Frame()
        self.frame6.pack(pady=40)

        self.create_list_button = tk.Button(self.frame6, text="Kayıtlı Personelleri\nGörüntüle", font="Veranda 11", height=2, bg="red", fg="white", command=Personnel.show_all_personnels)
        self.create_list_button.pack(side="left", padx=75)

        self.create_list_button = tk.Button(self.frame6, text="LİSTE OLUŞTUR", font="Veranda 11", height=2, bg="red", fg="white", border=3, command=WorkList.create_list)
        self.create_list_button.pack(side="right", padx=75)

        self.frame8 = tk.Frame()
        self.frame8.pack(side="bottom")

        self.exit_button = tk.Button(self.frame8, text="ÇIKIŞ", bg="red", fg="white", width=10, font="DejaVuSans 13 bold", border=3, command=main_window.destroy)
        self.exit_button.pack(pady=15)

        ### MenuBar ###
        def delete_personnel():
            name_entry_screen = tk.Toplevel()
            
            name_entry_screen.geometry(f"50x70+{(screen_width-800)//2}+{(screen_height-480)//4}")
            name_label = tk.Label(name_entry_screen, text="Silinecek İsmi Giriniz.")
            name_label.pack(anchor="nw")
            name_entry = tk.Entry(name_entry_screen, bg="white")
            name_entry.pack()

            def delete():
                deleted_name = name_entry.get()
                if deleted_name not in Personnel.all_personnels.keys():
                    tkmsg.showwarning("Hata", "Silmeye çalıştığınız personel kayıtlı değil !")
                else:
                    reply = tkmsg.showwarning("Dikkat !", deleted_name + "Silinecek, Emin misiniz ?", type="yesno")

                    if reply == "no":
                        pass
                    else:
                        Personnel.all_personnels.pop(deleted_name)
                
            delete_button = tk.Button(name_entry_screen, text="SİL", command=delete)
            delete_button.pack(side="left")
            cancel_button = tk.Button(name_entry_screen, text="VAZGEÇ", command=name_entry_screen.destroy)
            cancel_button.pack(side="right")

        menubar = tk.Menu(main_window)
        options = tk.Menu(menubar, tearoff=0)
        options.add_command(label="Personel Sil", background="red", command=delete_personnel)
        options.add_command(label="Personel Düzenle", background="red")
        options.add_command(label="Hakkında", background="red")


        menubar.add_cascade(label="Seçenekler...", menu=options)
        main_window.config(menu=menubar)

    
###################################################################################
class Personnel():
    all_personnels = dict()

    def __init__(self):
        self.name = app.name_entry.get()
        self.wanted_days = temporary_wanted_days_list
        self.unwanted_days = temporary_unwanted_days_list
        self.last_workday_of_last_month = temporary_last_day_variable
        self.annual_leave_days = temporary_annual_days_list
        self.personnel_group = temporary_personnel_group

    @classmethod
    def save_personnel(cls):
        if temporary_last_day_variable == 0:  # seçim yapılmadıysa
            tkmsg.showwarning( "HATA", "LÜTFEN GEÇEN AY SON NÖBET GÜNÜNÜ GİRİNİZ ! ")
            detail_window.focus()  # Pencereyi tekrar ön plana çıkarmak için
        else:
            per_inst = Personnel()  #instance of Personnel()
            Personnel.all_personnels[per_inst.name] = per_inst  

            detail_window.destroy()
            app.name_entry.delete(0, "end")
            tkmsg.showinfo("", per_inst.name + " Kaydedildi !")
            

            print(per_inst.name,"\nistenilen günler :", per_inst.wanted_days,
        "\nistenmeyen günler :", per_inst.unwanted_days, "\nyıllık izin :", per_inst.annual_leave_days, "\nson günü :", per_inst.last_workday_of_last_month, 
        "\npersonel grubu :", per_inst.personnel_group, "\n")

    @classmethod
    def show_all_personnels(cls):
        if not Personnel.all_personnels:
            tkmsg.showinfo("!", "Kayıtlı Personel Yok !")
            #print("Personel yok !")
        else:
            personel_window = tk.Toplevel()
            for per_inst in Personnel.all_personnels.values():
                
                personel_label = tk.Label(personel_window, text="-" * 56 + "\n" + per_inst.name + "\nistenilen günler :" + str(per_inst.annual_leave_days) +
                "\nistenmeyen günler :" + str(per_inst.unwanted_days) + "\nyıllık izin :" + str(per_inst.annual_leave_days) + "\nson günü :" + 
                str(per_inst.last_workday_of_last_month) + "\npersonel grubu :" + str(per_inst.personnel_group))

                personel_label.pack()
        
                print(per_inst.name,"\nistenilen günler :", per_inst.wanted_days,
                "\nistenmeyen günler :", per_inst.unwanted_days, "\nyıllık izin :", per_inst.annual_leave_days, "\nson günü :", per_inst.last_workday_of_last_month, 
                "\npersonel grubu :", per_inst.personnel_group)

##################################################################################
class WorkList():

    def __init__(self):
        self.current_month = current_month
        self.rule1 = temporary_rule1
        self.rule2 = temporary_rule2
        self.rule3 = temporary_rule3
        self.rule4 = temporary_rule4
        self.days = []

    def days_dict(self):
        for i in range(1, pmnod + 1):  # önceki ay listesi, ekranda görünmeyecek
            self.days.append([i, "___"])
        for i in range(1, cmnod + 1):
            self.days.append([i, "___"])
        for i in range(1, 3):
            self.days.append([i, "___"])  # son 2 günde günaşırı denetlemek için, ekranda görünmeyecek

    
    def create_list_window(self):
        list_window = tk.Toplevel()
        list_window.geometry(f"350x710+{(screen_width-350)//2}+{(screen_height-710)//3}")

        frame1 = tk.Frame(list_window)
        frame1.pack(fill="x")
        main_title = tk.Label(frame1, text=current_month + " AYI NÖBET LİSTESİ", font="Verdana 15", fg="red")
        main_title.pack(side="top")

        frame2 = tk.Frame(list_window)
        frame2.pack(fill="x")
        # x = tk.Label(frame2, text="AABT", fg="red", font="verdana 12")
        # x.grid(row=0, column=1)
        # y = tk.Label(frame2, text="ATT", fg="red", font="verdana 12")
        # y.grid(row=0, column=2)
        # z = tk.Label(frame2, text="SRC", fg="red", font="verdana 12")
        # z.grid(row=0, column=3)
        y = 1
        for i in range(pmnod, cmnod + pmnod):
            tk.Label(frame2, text=str(self.days[i][0]) + " : ").grid(row=y, column=0)
            tk.Label(frame2, text=self.days[i][1]).grid(row=y, column=1)
            y += 1

    def placing_wanted_days(self):
        for personnel in Personnel.all_personnels.values():
            for day in personnel.wanted_days:
                self.days[day + pmnod - 1][1] = personnel.name

    def placing_last_day(self):
        for personnel in Personnel.all_personnels.values():
            last_day = personnel.last_workday_of_last_month 
            self.days[last_day - 1][1] = personnel.name
    
    def max_3_days_break_before_annual_days(self): 
        if self.rule3 == 1:  # tik seçiliyse
            global tree_days_check
            tree_days_check = False
            for personnel in Personnel.all_personnels.values():
                if personnel.annual_leave_days:  #yıllık izni varsa
                    print(personnel.name, "için 3 gün taraması yapılıyor...")
                    counter = 0
                    first_day_of_annual = min(personnel.annual_leave_days)
                    y = first_day_of_annual 

                    for i in range (pmnod + y -1, (pmnod + y - 5), -1):
                        print(i-pmnod, ".gün değerlendiriliyor")
                        print(self.days[i - 1][1])

                        if self.days[i][1] == "???": # DÜZELT
                            break
                        else:
                            if self.days[pmnod + y][1] != self.days[i][1]:
                                counter += 1
                                if counter >= 4:
                                    tree_days_check = True
                                    print(self.days[i][1], " İzin Öncesi boşluk 3 Günü Aşıyor ", self.days[i][0], ".gün")
                            else:
                                break

                        
    def günaşırı_kuralı(self):
        pass
    
    def placing_random_names(self):
        personnels = list()  #random modülünü kullanabilmek için personelleri yeni bir listede topladım.
        for i in Personnel.all_personnels.keys():
            personnels.append(i)
            
        for i in range(pmnod, cmnod + pmnod):
            if self.days[i][1] == "___":
                pick = random.choice(personnels)
                pick_instance = Personnel.all_personnels[pick]

                counter_1 = 0
                counter_2 = 0

                if self.rule2 == 1:  # günaşırı yasağı varsa                 
                    while int(i - pmnod + 1) in pick_instance.unwanted_days or pick == self.days[i - 2][1] or pick == self.days[i - 1][1] or pick == self.days[i + 1][1] or pick == self.days[i + 2][1]:
                        pick = random.choice(personnels)
                        pick_instance = Personnel.all_personnels[pick]
                        counter_1 += 1

                        if counter_1 >= 10000:
                            print(counter_1, "kez denenmeye rağmen uygun kişi bulunamadı ", self.days[i][0], ".gün")                          
                            self.days[i][1] = "???"
                            break
                    counter_1 = 0

                    if self.days[i][1] == "???":
                        pass
                    else:
                        self.days[i][1] = (pick)

                else:  # günaşırı serbest
                    while int(i - pmnod + 1) in pick_instance.unwanted_days or pick == self.days[i - 1][1] or pick == self.days[i + 1][1]:
                        pick = random.choice(personnels)
                        counter_2 += 1

                        if counter_2 >= 10000:
                            print(counter_2, "kez denenmeye rağmen uygun kişi bulunamadı ", self.days[i][0], ".gün")                          
                            self.days[i][1] = "???"
                            break
                    counter_2 = 0

                    if self.days[i][1] == "???":
                        pass
                    else:
                        self.days[i][1] = (pick)
                        

    def max_9_days_break(self):  # rule-1  # random modülünün içinde çalıştır, her random atamadan sonra denetleyecek şekilde.
        if self.rule1 == 1:  # tik seçiliyse
            global nine_days_check
            nine_days_check = False
            for i in range(pmnod, cmnod + pmnod):
                break_days = 0
                for y in range(i - 1, (i - 11), -1):
                    
                    if self.days[i][1] == "???":  # randomda atama yapılamayan gün için 9 gün tarama atlanıyor
                        break
                    else:
                        if self.days[i][1] != self.days[y][1] and not Personnel.all_personnels[self.days[i][1]].annual_leave_days : 
                            break_days += 1
                            if break_days >= 10:
                                nine_days_check = True
                                print(self.days[i][1], " 9 GÜN BOŞLUĞU AŞIYOR ", self.days[i][0])  # PENCEREDE UYARI GÖSTER

                        elif Personnel.all_personnels[self.days[i][1]].annual_leave_days :
                            break
                        
                        else:
                            #print(self.days[i][1], "kişisinin, ayın", self.days[i][0], ".gününe kadar ", break_days, "gün boşluğu var")
                            break  
                  
    def caunt_work_days(self):
        global personnel_work_days
        personnel_work_days = dict()
        
        for personnel in Personnel.all_personnels.keys():
            personnel_work_days[personnel] = (sum(x.count(personnel) for x in self.days)) - 1  # geçen ayın son nöbetini çıkardım(-1)
            
        for i in personnel_work_days.items():
            print(i)
           
    # def rules(self):
    #     if self.rule1 == 1:
    #         max_9_days_break(self)

    #     if self.rule2 == 1:
    #         pass
        
    #     if self.rule3 == 1:
    #         pass

    @classmethod
    def create_list(cls):
        global nine_days_check
        global tree_days_check

        def list_maker():
            wl_inst.days_dict()
            wl_inst.placing_last_day()
            wl_inst.placing_wanted_days()
            wl_inst.placing_random_names()
            wl_inst.max_9_days_break()
            wl_inst.max_3_days_break_before_annual_days()

        if len(Personnel.all_personnels.keys()) < 3:
            tkmsg.showwarning( "HATA", "LİSTE OLUŞTURMAK İÇİN EN AZ 3 PERSONEL KAYDETMELİSİNİZ !")
        else:
            wl_inst = WorkList()
            list_maker()

            counter_9_days = 0
            counter_3_days = 0
            
            while nine_days_check == True:
                counter_9_days += 1
                if counter_9_days > 1000:
                    print("9 gün boşluk için deneme sayısı 1000'i geçti")
                    print("LÜTFEN İSTEKLERİNİZİ GÖZDEN GEÇİRİNİZ !")  # AYRI  PENCEREDE UYARI GÖSTER
                    break
                wl_inst = WorkList()
                list_maker()
            
            while tree_days_check == True:
                counter_3_days += 1
                if counter_3_days > 1000:
                    print("3 gün boşluk için deneme sayısı 1000'i geçti")
                    print("LÜTFEN İSTEKLERİNİZİ GÖZDEN GEÇİRİNİZ !")
                    break
                wl_inst = WorkList()
                list_maker()

            wl_inst.create_list_window()

            for i in wl_inst.days:
                print(i)
                
            print("\n")    
            wl_inst.caunt_work_days()
            print("\n")
            
            print("9 gün boşluk aşımı için deneme sayısı: ", counter_9_days)  #  silinecek
            print("3 gün boşluk aşımı için deneme sayısı: ", counter_3_days)  #  silinecek
    
#################################################################

### WİNDOW SETTİNGS ###
            
main_window = tk.Tk() 
main_window.tk_setPalette("#b5beff")
main_window.title("NÖBETÇİİ")
screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()
main_window.geometry(f"800x480+{(screen_width-800)//2}+{(screen_height-480)//4}")
main_window.resizable(width=tk.FALSE,height=tk.FALSE)

app = GUI()

main_window.mainloop()

#########################
# EŞİT NÖBET SAYILARI
# Yıllık izin alana fazla mesai yok kuralı
# İzin sonrası tutulması gereken nöbet sayısı ?
# personel sil, düzenle, ara.