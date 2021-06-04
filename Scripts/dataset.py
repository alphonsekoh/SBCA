import pandas as pd
from tkinter import *
from tkinter import filedialog, messagebox
from pandastable import Table

data = pd.read_csv('CSV\live-births-by-ethnic-group-age-group-of-mother-and-child-gender.csv')
pd.set_option('mode.chained_assignment', None)

# filter the data passed from "show dataset" button
def data_filter(year,month,minBirthCount,maxBirthCount,motherAge,childGen,motherRace,check_gen):
    data_list = []

    data['Year'] = pd.DatetimeIndex(data['month']).year
    data['Month'] = pd.DatetimeIndex(data['month']).month

    # Filter Year and month
    year_list = data["Year"].unique()
    year_input = []
    for i in range(len(year)):
        if year[i]:
            year_input.append(year_list[i])

    month_list = data["Month"].unique()
    month_input = []
    for i in range(len(month)):
        if month[i]:
            month_input.append(month_list[i])
    year_month_data = data[data["Year"].isin(year_input) & data["Month"].isin(month_input)]
    # Create a dataframe for year and month column
    df_yearandmonth = pd.DataFrame(year_month_data, columns=["Year", "Month"])
    data_list.append(df_yearandmonth)

    # Filter optional columns
    if motherAge != None:
        data["Mother age"] = data["mage"]
        agelist = data["Mother age"].unique()
        get_MotherAgeRange_sort = sorted(agelist)
        arrange_MotherAgeRanger = get_MotherAgeRange_sort[-1:] + get_MotherAgeRange_sort[:-1]
        filter_input = []
        for num in range(len(motherAge)):
            if motherAge[num]:
                filter_input.append(arrange_MotherAgeRanger[num])
        motherAge_data = data[data["Mother age"].isin(filter_input)]
        # Create a dataframe for Mother age column
        df_montherAge = pd.DataFrame(motherAge_data, columns=["Mother age"])
        data_list.append(df_montherAge)

    if childGen != None:
        data["Child Gender"] = data['child_gender']
        childFilter = []
        childGenList = ['M', 'F']
        for i in range(2):
            if childGen[i] == 1:
                childFilter.append(childGenList[i])
        do = data[data['Child Gender'].isin(childFilter)]
        # Create a dataframe for Child Gender column
        df_childgender = pd.DataFrame(do, columns=['Child Gender'])
        data_list.append(df_childgender)

    if motherRace != None:
        data["Mother Race"] = data['mrace']
        motherFilter = []
        motherRaceList = ['CHINESE', 'MALAYS', 'INDIANS', 'OTHERS']
        for i in range(4):
            if motherRace[i] == 1:
                motherFilter.append(motherRaceList[i])
        do = data[data['Mother Race'].isin(motherFilter)]
        # Create a dataframe for Mother Race column
        df_motherRace = pd.DataFrame(do, columns=['Mother Race'])
        data_list.append(df_motherRace)

    data["Birth Count"] = data["birth_count"]
    min_count = int(minBirthCount)
    max_count = int(maxBirthCount)
    filtered_data = data[data["Birth Count"].between(min_count, max_count)]
    # Create a dataframe for Birth Count column
    df_birthcount = pd.DataFrame(filtered_data, columns=["Birth Count"])
    data_list.append(df_birthcount)

    # Combine all the dataframe together
    df_final = pd.concat(data_list, axis=1)
    # Remove Nan inside the dataframe
    df_display = df_final.dropna(axis=0)
    # Prevent the value of in the column from converting Int to float
    df_display["Year"] = df_display["Year"].astype(int)
    df_display["Month"] = df_display["Month"].astype(int)
    df_display["Birth Count"] = df_display["Birth Count"].astype(int)

    # Return the final dataframe
    if df_display.empty:
        return "No records found"
    else:
        return df_display

# validate whether all checkboxes are unchecked 
def Validation_input(input_list):
    if sum(input_list) == 0:
        return True

# export the dataset as csv file
def exportCSV(df):
    try:
        export_file_path = filedialog.asksaveasfilename(defaultextension=".csv",filetypes=[("CSV (Comma delimited)","*.csv")])
        saved = df.to_csv(export_file_path, index = False, header=True)
        # if the csv file is created, it will return None
        # if it is not created, it will return an empty string and raise FileNotFoundError
        if saved == None:
            messagebox.showinfo(title=None, message="The dataset was saved successfully")
    except FileNotFoundError:
        messagebox.showwarning(title=None, message="The dataset has NOT been saved")

# show the dataset selected in a pop-up window
def dataset_popup(df):
    # pop-up window setting
    root = Tk()
    root.title('Dataset')
    root.geometry("600x400") # define width x height
    
    # position the window in the center of the page
    positionRight = int(root.winfo_screenwidth()/2 - 600/2)
    positionDown = int(root.winfo_screenheight()/2 - 400/2)
    root.geometry("+%d+%d" % (positionRight, positionDown))

    # use pandastable to show the dataset
    frame = Frame(root)
    frame.pack(fill='both', expand=True)
    pt = Table(frame,dataframe=df,editable=False)
    pt.show()

    button = Button(root, text='Export CSV', command=lambda: exportCSV(df))
    button.pack()
    root.mainloop()