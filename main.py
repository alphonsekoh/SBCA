from tkinter import *
from tkinter import ttk, messagebox, font
# import functions from "Scripts" folder
import sys
sys.path.append('.\Scripts')
import dataset
import birth_count_stats

# group checkboxs in one line
class Checkbar(Frame):
    def __init__(self, parent=None, items=[], side=LEFT, anchor=W):
        Frame.__init__(self, parent)
        self.vars = []
        for item in items:
            var = IntVar(value=1) # value=1 means checkbox is checked by default
            chk = Checkbutton(self, text=item, variable=var)
            chk['background'] = '#e5eef4'
            chk.pack(side=side, anchor=anchor, expand=NO)
            self.vars.append(var)
    # return checkbox values in a list
    def value(self):
        return list(map((lambda var: var.get()), self.vars))

# create a checkcombobox (for month and mother age)
class CheckComboBox(Frame):
    def __init__(self, parent=None, items=[]):
        Frame.__init__(self,parent)
        self.vars = []
        self.text = items[0] # the name of checkcombobox
        items.remove(items[0])  # remove the name from the list
        self.mb=  Menubutton(tab2, text=self.text, relief=RAISED)
        self.mb.menu = Menu(self.mb, tearoff=0)
        self.mb["menu"] = self.mb.menu
        self.mb['background'] = "#c0d6e4"
        self.mb['activebackground'] = "#d2e2ec"
        self.mb.menu['background'] = "#f8fafc"
        for item in items:
            var = IntVar(value=1) # value=1 means checkbox is checked by default
            self.mb.menu.add_checkbutton (label=item, variable=var)
            self.vars.append(var)
    # show the checkcombobox
    def show(self):     
        if self.text=="Age Group":
            self.mb.place(x=185,y=200)
        if self.text=="Month(s) Selected":
            self.mb.place(x=185,y=120)
    # hide the checkcombobox
    def hide(self):
        self.mb.place_forget()
    # return checkcombobox values in a list
    def value(self):
        return list(map((lambda var: var.get()), self.vars))

# show and hide options when user select/unselect the optional columns
def show_hide_option():
    # show or hide mother age options
    if var_age.get() == 1:
        chk_age_option.show()
    if var_age.get() == 0:
        chk_age_option.hide()
    # show or hide child gender options
    if var_gen.get() == 1:
        chk_gen_option.place(x=180,y=240)
    if var_gen.get() == 0:
        chk_gen_option.place_forget()
    # show or hide mother race options
    if var_race.get() == 1:
        chk_race_option.place(x=180,y=280)
    if var_race.get() == 0:
        chk_race_option.place_forget()

# define all the error messages for data filtering
def errorLabel():
    tab2colour = "#e5eef4"
    fontcolour = "#c72626"
    global yr_error, mth_error, bcnt_error1, bcnt_error2, bcnt_error3, age_error, gen_error, race_error
    yr_error = Label(tab2errorframe, text="Please select at least one year", bg=tab2colour, fg=fontcolour)
    mth_error = Label(tab2errorframe, text="Please select at least one month", bg=tab2colour, fg=fontcolour)
    bcnt_error1 = Label(tab2errorframe, text="Minimum and maximum birth count must be more than 0", bg=tab2colour, fg=fontcolour)
    bcnt_error2 = Label(tab2errorframe, text="Minimum birth count cannot be more than maximum birth count", bg=tab2colour, fg=fontcolour)
    bcnt_error3 = Label(tab2errorframe, text="Please enter integer for birth count", bg=tab2colour, fg=fontcolour)
    age_error = Label(tab2errorframe, text="Please select at least one mother age group", bg=tab2colour, fg=fontcolour)
    gen_error = Label(tab2errorframe, text="Please select at least one child gender", bg=tab2colour, fg=fontcolour)
    race_error = Label(tab2errorframe, text="Please select at least one mother race", bg=tab2colour, fg=fontcolour)

# process and show the data passed from "show dataset" button
def dataset_selected():
    # clear all the error messages
    for element in tab2errorframe.winfo_children():
        element.destroy()
    errorLabel()

    try:
        # Get all the filter value
        year = chk_year.value()
        month = chk_mth.value()
        minBirthCount = int(min_bcnt.get())
        maxBirthCount = int(max_bcnt.get())

        # Set the optional variable to None
        motherAge = childGen = motherRace = None
        success = True

        # Validate Year
        error = dataset.Validation_input(year)
        if error:
            success = False
            yr_error.place(x=20,y=0)    # show error message

        # Validate Month
        error = dataset.Validation_input(month)
        if error:
            success = False
            mth_error.place(x=0,y=40)   # show error message

        # Validate birth count
        if minBirthCount <= 0 or maxBirthCount <= 0:
            success = False
            bcnt_error1.place(x=0,y=80) # show error message
        elif minBirthCount > maxBirthCount:
            success = False
            bcnt_error2.place(x=0,y=80) # show error message

        # Validate optional column
        if var_age.get() == 1:
            error = dataset.Validation_input(chk_age_option.value())
            if error:
                success = False
                age_error.place(x=0,y=120)  # show error message
            else:
                motherAge = chk_age_option.value()
        if var_gen.get() == 1:
            error = dataset.Validation_input(chk_gen_option.value())
            if error:
                success = False
                gen_error.place(x=0,y=160)  # show error message
            else:
                childGen = chk_gen_option.value()
        if var_race.get() == 1:
            error = dataset.Validation_input(chk_race_option.value())
            if error:
                success = False
                race_error.place(x=130,y=200)   # show error message
            else:
                motherRace = chk_race_option.value()

        if success:
            # Get the data after all the filtering
            data = dataset.data_filter(year, month, minBirthCount, maxBirthCount, motherAge, childGen, motherRace,
                                        var_gen.get())
            # Check Whether there is a records in the data
            if type(data) == str:
                messagebox.showerror(data, data)
            else:
                dataset.dataset_popup(data)

    except ValueError:
        bcnt_error3.place(x=0,y=80) # show error message

    except KeyboardInterrupt:
        print("Program ended due to keyboard interrupt")
   

# process and show the data passed from "show statistic" button
def statistics_selected():
    birth_count_stats.statsOptions(int(stats_selected.get()))

# main starts here
if __name__ == '__main__':
    try:
        # setup GUI
        gui = Tk()
        gui.title("Singapore Birth Count Analysis (SBCA)")
        gui.geometry("750x480") # define width x height
        gui['background'] = "white"

        # position the GUI in the center of the page
        positionRight = int(gui.winfo_screenwidth()/2 - 750/2)
        positionDown = int(gui.winfo_screenheight()/2 - 500/2)
        gui.geometry("+%d+%d" % (positionRight, positionDown))

        # define the style and background colour of tabs
        style = ttk.Style()
        style.theme_create( "tabstyle", parent="alt", settings={
            "TNotebook": {"configure": {"tabmargins": [2, 2, 2, 0],"background": "white" } },
            "TNotebook.Tab": {
            "configure": {"padding": [10, 1], "background": "#f7f4ec"},
            "map":       {"background": [("selected", "white")],
                          "expand": [("selected", [1, 1, 1, 0])] } } } )
        style.theme_use("tabstyle")
        tab1colour = "#e2eee5"
        tab2colour = "#e5eef4"
        tab3colour = "#e6e6fa"

        # define all tabs (Home, Data Filter and Statistics)
        note = ttk.Notebook(gui)
        tab1 = Frame(note)
        tab2 = Frame(note)
        tab2errorframe = Frame(tab2)    # this frame is for the error messages
        tab3 = Frame(note)      
        note.add(tab1, text = "Home", compound=TOP)
        note.add(tab2, text = "Data Filter")
        note.add(tab3, text = "Statistics")
        tab1['bg'] = tab1colour
        tab2['bg'] = tab2colour
        tab3['bg'] = tab3colour
        note.pack(fill=BOTH, expand=True)
        
        ######################## tab 1 ###########################

        # labels for introduction
        Label(tab1,  text="Our Program", bg=tab1colour, font=('Helvetica', 14, 'bold')).place(x=300,y=30)
        Label(tab1,  text="SBCA is a program that provides data analysis and data visualisation of live-births by mother’s ethnic group, age group", bg=tab1colour).place(x=50,y=70)
        Label(tab1,  text="and child’s gender in Singapore. With this program, users are able to visualise and export the data as well as to make a ", bg=tab1colour).place(x=50,y=90)
        Label(tab1,  text="wise decision from the data they visualised and exported.", bg=tab1colour).place(x=50,y=110)
        
        # labels for features
        Label(tab1,  text="Our Features", bg=tab1colour, font=('Helvetica', 14, 'bold')).place(x=300,y=150)
        # labels for features - data filtering
        lblframe1 = LabelFrame(tab1, text="Data Filtering", width=650, height=110, bg=tab1colour, font=('Helvetica', 10, 'bold'), labelanchor="n")
        lblframe1.place(x=40,y=190)
        Label(lblframe1,  text="In the \"Data Filter\" tab, every columns and their corresponding values are checked by default to show all dataset.",bg=tab1colour).place(x=20,y=10)
        Label(lblframe1,  text="Users can uncheck them according to their preferences. The filtered dataset will be shown in a pop-up window",bg=tab1colour).place(x=20,y=30)
        Label(lblframe1,  text="with a \"Export CSV\" button. Users can click this button to save the filtered dataset to any destination folder.",bg=tab1colour).place(x=20,y=50)
        # labels for features - statistics
        lblframe2 = LabelFrame(tab1, text="Statistics", width=650, height=110, padx=2, pady=2, bg=tab1colour, font=('Helvetica', 10, 'bold'), labelanchor="n")
        lblframe2.place(x=40,y=310)
        Label(lblframe2,  text="In the \"Statistics\" tab, there are 10 predefined statistic options for users to select. Similar to \"Data Filter\" tab, the", bg=tab1colour).place(x=20,y=10)
        Label(lblframe2,  text="statistic selected will be shown in a pop-up window. Users can click the save icon at the bottom of the pop-up", bg=tab1colour).place(x=20,y=30)
        Label(lblframe2,  text="window to save the result as PNG file to any destination folder.", bg=tab1colour).place(x=20,y=50)

        ######################## tab 2 ###########################

        Label(tab2,  text="Everything is checked by default to show all dataset.",bg=tab2colour).place(x=40,y=20)
        Label(tab2,  text="You may modify the filter settings below according to your needs.",bg=tab2colour).place(x=40,y=40)
        
        # place the tab2errorframe to display error message
        tab2errorframe = Frame(tab2, height = 250, width = 400,bg=tab2colour)
        tab2errorframe.place(x=340,y=80)

        # line 1: year
        lbl_year = Label(tab2, text="Year", bg=tab2colour)
        lbl_year.place(x=60,y=80)   # place at this location
        chk_year = Checkbar(tab2, [2016, 2017, 2018])
        chk_year.place(x=180,y=80)
        
        # line 2: month
        lbl_mth = Label(tab2, text="Month", bg=tab2colour)
        lbl_mth.place(x=60,y=120)
        chk_mth = CheckComboBox(tab2, ["Month(s) Selected","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
        chk_mth.show()

        # line 3: birth count
        lbl_bcnt = Label(tab2, text="Birth Count", bg=tab2colour)
        lbl_bcnt.place(x=60,y=160)
        # define default value for min and max
        min_bcnt_default = StringVar()
        min_bcnt_default.set("1")   # default min value = 1
        max_bcnt_default = StringVar()
        max_bcnt_default.set("518") # default max value = 518
        # create spinbox for min and max
        min_bcnt = Spinbox(tab2, from_=1, to=517,width=5,textvariable=min_bcnt_default)
        dash_bcnt = Label(tab2, text="-")
        max_bcnt = Spinbox(tab2, from_=1, to=518,width=5,textvariable=max_bcnt_default)
        # show spinbox in the location defined
        min_bcnt.place(x=185,y=160)
        dash_bcnt.place(x=235,y=160)
        max_bcnt.place(x=253,y=160)

        # line 4: mother age
        # allow user to choose whether want to view mother age column
        var_age = IntVar(value=1)   # value=1 means checkbox is checked by default
        chk_age= Checkbutton(tab2,  text="Mother Age", bg=tab2colour, variable=var_age,
                        onvalue=1, offvalue=0, command=show_hide_option)
        chk_age.place(x=40,y=200)
        # define default value for min and max
        chk_age_option = CheckComboBox(tab2, ["Age Group","Under 15","15-19","20-24","25-29","30-34","35-39","40-44","45-49","50-54","55-59"])
        chk_age_option.show()

        # line 5: child gender
        # allow user to choose whether want to view child gender column
        var_gen = IntVar(value=1)   # value=1 means checkbox is checked by default
        chk_gen= Checkbutton(tab2, text="Child Gender", bg=tab2colour, variable=var_gen,
                        onvalue=1, offvalue=0,command=show_hide_option)
        chk_gen.place(x=40,y=240)
        # create checkbar for the option and show it at the location defined
        chk_gen_option = Checkbar(tab2, ["Male","Female"])
        chk_gen_option.place(x=180,y=240)
        
        # line 6: mother race
        # allow user to choose whether want to view mother race column
        var_race = IntVar(value=1)   # value=1 means checkbox is checked by default
        chk_race= Checkbutton(tab2, text="Mother Race", bg=tab2colour, variable=var_race,
                        onvalue=1, offvalue=0,command=show_hide_option)
        chk_race.place(x=40,y=280)
        # create checkbar for the option and show it at the location defined
        chk_race_option = Checkbar(tab2, ["Chinese","Malays","Indians","Others"])
        chk_race_option.place(x=180,y=280)
        
        # pass the values in this tab to dataset_selected()
        Button(tab2, text='Show Dataset', command=dataset_selected, bg="#acc0cd", padx=5, pady=5).place(x=600,y=370)
        
        ####################### tab 3 #########################

        Label(tab3,  text="Which statistic you want to view?", bg=tab3colour).place(x=40,y=20)
        stats_selected = StringVar(tab3, "1")    # 1 means the first option is selected by default

        # store the option with corresponding value in a dict
        stat_dict = {"Total Birth Count by Child Gender and Year": "1",
                     "Total Monthly Birth Count in 2016 by Child Gender": "2",
                     "Total Monthly Birth Count in 2017 by Child Gender": "3",
                     "Total Monthly Birth Count in 2018 by Child Gender": "4",
                     "Total Birth Count Percentage by Child Gender": "5",
                     "Total Birth Count Percentage by Mother's Race": "6",
                     "Total Birth Count by Mother's Race and Child Gender": "7",
                     "Total Birth Count by Mother's Age Group": "8",
                     "Total Birth Count by Mother's Age Group and Race": "9",
                     "Total Birth Count by Mother's Age Group and Year": "10"}
        x_value = 40
        y_value = 60

        # use for loop to create radiobutton for each option in the dict
        for (key, value) in stat_dict.items(): 
            Radiobutton(tab3, text = key, bg=tab3colour, variable = stats_selected,  
                value = value).place(x=x_value,y=y_value) 
            y_value += 30   
        
        # pass the values in this tab to statistics_selected()
        Button(tab3, text='Show Statistic', command=statistics_selected, bg="#b1b1dc", padx=5, pady=5).place(x=600,y=370)
        
        gui.mainloop()

    except KeyboardInterrupt:
        print("Program ended due to keyboard interrupt")