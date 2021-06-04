import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set(rc={'axes.facecolor': '#c6d5d8', 'figure.facecolor': '#ebe6e5'})


def statsOptions(option):
    """
    1. Total Birth Count by Child Gender and Year
    2. Total Monthly Birth Count in 2016 by Child Gender
    3. Total Monthly Birth Count in 2017 by Child Gender
    4. Total Monthly Birth Count in 2018 by Child Gender
    5. Total Birth Count Percentage by Child Gender
    6. Total Birth Count Percentage by Mother's Race
    7. Total Birth Count by Mother's Race and Child Gender
    8. Total Birth Count by Mother's Age Group
    9. Total Birth Count by Mother's Age Group and Race
    10. Total Birth Count by Mother's Age Group and Year
    """

    # Read CSV file
    df = pd.read_csv('CSV\live-births-by-ethnic-group-age-group-of-mother-and-child-gender.csv')

    if option == 1:  # Total Birth Count By Child Gender over the years

        df['year'] = pd.DatetimeIndex(df['month']).year
        df.head()

        df_grp = df.groupby(['year', 'child_gender'])['birth_count'].sum()

        # To Populate CellText
        myList = df_grp.values.tolist()
        parts = 3
        newList = [myList[(i * len(myList)) // parts:((i + 1) * len(myList)) // parts] for i in range(parts)]

        # Set Line Colour
        mycolor = ['#957DAD', '#6891C3']

        # Plot Graph
        ax = df_grp.unstack('child_gender').fillna(0).plot(kind='line',
                                                           stacked=False,
                                                           marker='o',
                                                           color=mycolor)

        the_table = plt.table(cellText=newList,
                              loc='center left',
                              rowLabels=[' 2016 ', ' 2017 ', ' 2018 '],
                              rowColours=['#b4bad4', '#b4bad4', '#b4bad4'],
                              colLabels=['Female', 'Male'],
                              colColours=['#d2c1ce', '#d2c1ce'],
                              bbox=[1.3, 0.2, 0.4, 0.4])  # [left, bottom, width, height]

        # Set x-axis label
        plt.xticks(np.arange(2016, 2019, 1))

        # Set y-axis label
        plt.yticks(np.arange(0, 24000, 2000))
        plt.ylim([0, 22000])

        plt.subplots_adjust(left=0.3, bottom=0.2)
        plt.legend(title='Child Gender', bbox_to_anchor=(1.0, 1), loc='upper left')
        plt.ylabel('Birth Count')
        plt.xlabel('Year')
        fig = plt.gcf()
        fig.set_size_inches(11, 5)
        plt.title("Total Birth Count by Child Gender and Year")
        plt.autoscale(enable=False)
        plt.tight_layout()
        plt.show()

    elif option == 2:  # Total birth count in 2016 By Child Gender

        # Extract year from date
        df['year'] = pd.to_datetime(df['month']).dt.year
        df.head()

        # Filter 2016
        df = df[df['year'] == 2016]

        # Extract month number from date
        df['month'] = pd.to_datetime(df['month'])
        # Convert month number to month name
        df['month_name'] = df['month'].dt.strftime('%b')
        df.head()

        # Group data by month name and child gender
        df_grp = df.groupby(['month_name', 'child_gender'], sort=False)['birth_count'].sum()

        # Set Line Colour
        mycolor = ['#957DAD', '#6891C3']

        # Plot Graph
        ax = df_grp.unstack('child_gender').fillna(0).plot(
            kind='line',
            stacked=False,
            marker='o',
            color=mycolor)

        # To Populate CellText
        myList = df_grp.values.tolist()
        parts = 12
        newList = [myList[(i * len(myList)) // parts:((i + 1) * len(myList)) // parts] for i in range(parts)]

        the_table = plt.table(cellText=newList,
                              loc='center left',
                              rowLabels=[' Jan ', ' Feb ', ' Mar ', ' Apr ', ' May ', ' Jun ', ' Jul ', ' Aug ',
                                         ' Sep ', ' Oct ', ' Nov ', ' Dec '],
                              rowColours=['#b4bad4', '#b4bad4', '#b4bad4', '#b4bad4', '#b4bad4', '#b4bad4', '#b4bad4',
                                          '#b4bad4', '#b4bad4', '#b4bad4', '#b4bad4', '#b4bad4'],
                              colLabels=['Female', 'Male'],
                              colColours=['#d2c1ce', '#d2c1ce'],
                              bbox=[1.3, 0.1, 0.4, 0.7])  # [left, bottom, width, height]

        # Set x-axis months label
        month = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
        ax.set_xticks(np.arange(0, 12))
        ax.set_xticklabels(month)

        # Set y-axis label
        plt.yticks(np.arange(0, 2500, 250))
        plt.ylim([0, 2000])

        plt.subplots_adjust(left=0.3, bottom=0.2)
        plt.legend(title='Child Gender', bbox_to_anchor=(1.0, 1), loc='upper left')
        plt.ylabel('Birth Count')
        plt.xlabel('Month')
        plt.title("Total Monthly Birth Count in 2016 by Child Gender")
        plt.autoscale(enable=False)
        fig = plt.gcf()
        fig.set_size_inches(11, 5)
        plt.tight_layout()
        plt.show()

    elif option == 3:  # Total birth count in 2017 By Child Gender

        # Extract year from date
        df['year'] = pd.to_datetime(df['month']).dt.year
        df.head()

        # Filter 2018
        df = df[df['year'] == 2017]

        # Extract month number from date
        df['month'] = pd.to_datetime(df['month'])
        # Convert month number to month name
        df['month_name'] = df['month'].dt.strftime('%b')
        df.head()

        # Group data by month name and child gender
        df_grp = df.groupby(['month_name', 'child_gender'], sort=False)['birth_count'].sum()

        # Set line colour
        mycolor = ['#957DAD', '#6891C3']

        # Plot Graph
        ax = df_grp.unstack('child_gender').fillna(0).plot(
            kind='line',
            stacked=False,
            marker='o',
            color=mycolor)

        # To Populate CellText
        myList = df_grp.values.tolist()
        parts = 12
        newList = [myList[(i * len(myList)) // parts:((i + 1) * len(myList)) // parts] for i in range(parts)]

        the_table = plt.table(cellText=newList,
                              loc='center left',
                              rowLabels=[' Jan ', ' Feb ', ' Mar ', ' Apr ', ' May ', ' Jun ', ' Jul ', ' Aug ',
                                         ' Sep ', ' Oct ', ' Nov ', ' Dec '],
                              rowColours=['#b4bad4', '#b4bad4', '#b4bad4', '#b4bad4', '#b4bad4', '#b4bad4', '#b4bad4',
                                          '#b4bad4', '#b4bad4', '#b4bad4', '#b4bad4', '#b4bad4'],
                              colLabels=['Female', 'Male'],
                              colColours=['#d2c1ce', '#d2c1ce'],
                              bbox=[1.3, 0.1, 0.4, 0.7])  # [left, bottom, width, height]

        # Set x-axis months label
        month = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
        ax.set_xticks(np.arange(0, 12))
        ax.set_xticklabels(month)

        # Set y-axis label
        plt.yticks(np.arange(0, 2500, 250))
        plt.ylim([0, 2000])

        plt.subplots_adjust(left=0.3, bottom=0.2)
        plt.legend(title='Child Gender', bbox_to_anchor=(1.0, 1), loc='upper left')
        plt.ylabel('Birth Count')
        plt.xlabel('Month')
        plt.title("Total Monthly Birth Count in 2017 by Child Gender")
        plt.autoscale(enable=False)
        fig = plt.gcf()
        fig.set_size_inches(11, 5)
        plt.tight_layout()
        plt.show()

    elif option == 4:  # Total birth count in 2018 By Child Gender

        # Extract year from date
        df['year'] = pd.to_datetime(df['month']).dt.year
        df.head()

        # Filter 2018
        df = df[df['year'] == 2018]

        # Extract month number from date
        df['month'] = pd.to_datetime(df['month'])
        # Convert month number to month name
        df['month_name'] = df['month'].dt.strftime('%b')
        df.head()

        # Group data by month name and child gender
        df_grp = df.groupby(['month_name', 'child_gender'], sort=False)['birth_count'].sum()

        # Set line colour
        mycolor = ['#957DAD', '#6891C3']

        # Plot Graph
        ax = df_grp.unstack('child_gender').fillna(0).plot(kind='line',
                                                           stacked=False,
                                                           marker='o',
                                                           color=mycolor)

        # To Populate CellText
        myList = df_grp.values.tolist()
        parts = 12
        newList = [myList[(i * len(myList)) // parts:((i + 1) * len(myList)) // parts] for i in range(parts)]

        the_table = plt.table(cellText=newList,
                              loc='center left',
                              rowLabels=[' Jan ', ' Feb ', ' Mar ', ' Apr ', ' May ', ' Jun ', ' Jul ', ' Aug ',
                                         ' Sep ', ' Oct ', ' Nov ', ' Dec '],
                              rowColours=['#b4bad4', '#b4bad4', '#b4bad4', '#b4bad4', '#b4bad4', '#b4bad4', '#b4bad4',
                                          '#b4bad4', '#b4bad4', '#b4bad4', '#b4bad4', '#b4bad4'],
                              colLabels=['Female', 'Male'],
                              colColours=['#d2c1ce', '#d2c1ce'],
                              bbox=[1.3, 0.1, 0.4, 0.7])  # [left, bottom, width, height]

        # Set x-axis months label
        month = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
        ax.set_xticks(np.arange(0, 12))
        ax.set_xticklabels(month)

        # Set y-axis label
        plt.yticks(np.arange(0, 2500, 250))
        plt.ylim([0, 2000])

        plt.subplots_adjust(left=0.3, bottom=0.2)
        plt.legend(title='Child Gender', bbox_to_anchor=(1.0, 1), loc='upper left')
        plt.ylabel('Birth Count')
        plt.xlabel('Month')
        plt.title("Total Monthly Birth Count in 2018 by Child Gender")
        plt.autoscale(enable=False)
        fig = plt.gcf()
        fig.set_size_inches(11, 5)
        plt.tight_layout()
        plt.show()

    elif option == 5:  # Total Birth Count % by Child Gender
        labels = ['Female', 'Male']
        colors = ['#dab5D2', '#AFC0E3']

        # Group data by Child Gender
        df_grp = df.groupby('child_gender')['birth_count'].sum()

        # Plot Graph
        ax = df_grp.plot(kind='pie', labels=labels, autopct='%1.1f%%', colors=colors, shadow=True)

        # To Populate CellText
        myList = df_grp.values.tolist()
        parts = 1
        newList = [myList[(i * len(myList)) // parts:((i + 1) * len(myList)) // parts] for i in range(parts)]

        the_table = plt.table(cellText=newList,
                              loc='center left',
                              rowLabels=['Birth Count'],
                              rowColours=['#b4bad4'],
                              colLabels=['Female', 'Male'],
                              colColours=['#d2c1ce', '#d2c1ce'],
                              bbox=[0.0, -0.1, 1, 0.12])  # [left, bottom, width, height]

        plt.ylabel("")
        fig = plt.gcf()
        fig.set_size_inches(11, 5)
        plt.title("Total Birth Count Percentage by Child Gender")
        plt.show()

    elif option == 6:  # Total Birth Count % by Mother's Race
        labels = ["Chinese", "Indians", "Malays", "Others"]
        colors = ['#C7CEEA', '#FFDAC1', '#FF9AA2', '#B5EAD7']

        df_grp = df.groupby('mrace')['birth_count'].sum()
        ax = df_grp.plot(kind='pie', labels=labels, autopct='%1.1f%%', colors=colors, shadow=True)

        # To Populate CellText
        myList = df_grp.values.tolist()
        parts = 1
        newList = [myList[(i * len(myList)) // parts:((i + 1) * len(myList)) // parts] for i in range(parts)]

        the_table = plt.table(cellText=newList,
                              loc='center left',
                              rowLabels=['Birth Count'],
                              rowColours=['#b4bad4'],
                              colLabels=['Chinese', 'Indians', 'Malays', 'Others'],
                              colColours=['#d2c1ce', '#d2c1ce', '#d2c1ce', '#d2c1ce'],
                              bbox=[0.0, -0.1, 1, 0.12])  # [left, bottom, width, height]

        plt.ylabel("")
        fig = plt.gcf()
        fig.set_size_inches(11, 5)
        plt.title("Birth Count Percentage by Mother's Race")
        plt.show()

    elif option == 7:  # Total Birth Count By Child Gender based on Mother Race

        df_grp = df.groupby(['mrace', 'child_gender'])['birth_count'].sum()

        # Set line colour
        mycolor = ['#957DAD', '#6891C3']

        ax = df_grp.unstack('child_gender').fillna(0).plot(kind='line',
                                                           stacked=False,
                                                           marker='o',
                                                           color=mycolor)

        # To Populate CellText
        myList = df_grp.values.tolist()
        parts = 4
        newList = [myList[(i * len(myList)) // parts:((i + 1) * len(myList)) // parts] for i in range(parts)]

        the_table = plt.table(cellText=newList,
                              loc='center left',
                              rowLabels=['Chinese', 'Indians', 'Malays', 'Others'],
                              rowColours=['#b4bad4', '#b4bad4', '#b4bad4', '#b4bad4'],
                              colLabels=['Female', 'Male'],
                              colColours=['#d2c1ce', '#d2c1ce'],
                              bbox=[1.4, 0.2, 0.4, 0.5])  # [left, bottom, width, height]

        # Set x-axis months label
        race = ('Chinese', 'Indians', 'Malays', 'Others')
        ax.set_xticks(np.arange(0, 4))
        ax.set_xticklabels(race)

        # Set y-axis label
        plt.yticks(np.arange(0, 40000, 5000))
        plt.ylim([0, 38000])

        plt.subplots_adjust(left=0.3, bottom=0.2)
        plt.legend(title='Child Gender', bbox_to_anchor=(1.0, 1), loc='upper left')
        plt.ylabel('Birth Count')
        plt.xlabel("Mother's Race")
        plt.title("Total Birth Count by Mother's Race and Child Gender")
        plt.autoscale(enable=False)
        fig = plt.gcf()
        fig.set_size_inches(11, 5)
        plt.tight_layout()
        plt.show()

    elif option == 8:  # Total Birth Count By Mother's Age Group

        df_grp = df.groupby(['mage'])['birth_count'].sum()

        # Plot Graph
        ax = df_grp.fillna(0).plot(kind='line',
                                   marker='o',
                                   color='#6891C3')

        # To Populate CellText
        myList = df_grp.values.tolist()
        parts = 1
        newList = [myList[(i * len(myList)) // parts:((i + 1) * len(myList)) // parts] for i in range(parts)]

        the_table = plt.table(cellText=newList,
                              loc='center left',
                              rowLabels=['Birth Count'],
                              rowColours=['#b4bad4'],
                              colLabels=['15 - 19', '20 - 24', '25 - 29', '30 - 34', '35 - 39', '40 - 44', '40 - 45',
                                         '50 - 54', '55 - 59', 'Under 15'],
                              colColours=['#d2c1ce', '#d2c1ce', '#d2c1ce', '#d2c1ce', '#d2c1ce', '#d2c1ce', '#d2c1ce',
                                          '#d2c1ce', '#d2c1ce', '#d2c1ce'],
                              bbox=[0.0, -0.4, 1, 0.12])  # [left, bottom, width, height]

        # Set x-axis months label
        age_grp = ('15 - 19', '20 - 24', '25 - 29', '30 - 34', '35 - 39', '40 - 44', '40 - 45', '50 - 54', '55 - 59',
                   'Under 15')
        ax.set_xticks(np.arange(0, 10))
        ax.set_xticklabels(age_grp)

        # Set y-axis label
        plt.yticks(np.arange(0, 55000, 5000))

        plt.xticks(rotation=35, horizontalalignment="right")
        plt.ylabel('Birth Count')
        plt.xlabel("Mother's Age")
        plt.title("Total Birth Count by Mother's Age Group")
        plt.autoscale(enable=False)
        fig = plt.gcf()
        fig.set_size_inches(10, 6)
        plt.tight_layout()
        plt.show()

    elif option == 9:  # Total Birth Count By Mother's Age Group and Race

        df_grp = df.groupby(['mrace', 'mage'])['birth_count'].sum()

        # Set Bar Colour
        mycolor = ['#58949c', '#f2d7b4', '#df9881', '#6891C3']

        # Plot Graph
        ax = df_grp.unstack('mrace').fillna(0).plot(kind='bar',
                                                    color=mycolor)

        # To Populate CellText
        myList = df_grp.values.tolist()
        myList.insert(18, 0)
        myList.insert(27, 0)
        myList.insert(28, 0)
        myList.insert(-1, 0)
        parts = 4
        newList = [myList[(i * len(myList)) // parts:((i + 1) * len(myList)) // parts] for i in range(parts)]

        the_table = plt.table(cellText=newList,
                              loc='center left',
                              rowLabels=['Chinese', 'Indians', 'Malays', 'Others'],
                              rowColours=['#b4bad4', '#b4bad4', '#b4bad4', '#b4bad4'],
                              colLabels=['15 - 19', '20 - 24', '25 - 29', '30 - 34', '35 - 39', '40 - 44', '45 - 49',
                                         '50 - 54', '55  -  59', 'Under 15'],
                              colColours=['#d2c1ce', '#d2c1ce', '#d2c1ce', '#d2c1ce', '#d2c1ce', '#d2c1ce', '#d2c1ce',
                                          '#d2c1ce', '#d2c1ce', '#d2c1ce'],
                              bbox=[0.0, -0.55, 1, 0.3])  # [left, bottom, width, height]

        plt.xticks(rotation=35, horizontalalignment="right")
        plt.legend(title="Mother's Race", bbox_to_anchor=(1.0, 1), loc='upper left')
        plt.ylabel('Birth Count')
        plt.xlabel("Mother's Age")
        plt.title("Total Birth Count by Mother's Age Group and Race")
        fig = plt.gcf()
        fig.set_size_inches(10, 8)
        plt.autoscale(enable=False)
        plt.tight_layout()
        plt.show()

    elif option == 10:  # Total Birth Count By Year and Mother's Age Group

        # Extract Year from date
        df['year'] = pd.DatetimeIndex(df['month']).year
        df.head()

        df_grp = df.groupby(['year', 'mage'])['birth_count'].sum()

        # Set Bar colour
        mycolor = ['#58949c', '#E0BBE4', '#f2d7b4', '#957DAD', '#df9881', '#D291BC', '#6891C3', '#EBDED1', '#F8B9C5',
                   '#FF9AA2']

        ax = df_grp.unstack('mage').fillna(0).plot(kind='bar', stacked=False, color=mycolor)

        # To Populate CellText
        myList = df_grp.values.tolist()
        myList.insert(18, 0)
        myList.insert(-1, 0)
        parts = 3
        newList = [myList[(i * len(myList)) // parts:((i + 1) * len(myList)) // parts] for i in range(parts)]

        the_table = plt.table(cellText=newList,
                              loc='left',
                              colLabels=['15 - 19', '20 - 24', '25 - 29', '30 - 34', '35 - 39', '40 - 44', '45 - 49',
                                         '50 - 54', '55  -  59', 'Under 15'],
                              colColours=['#d2c1ce', '#d2c1ce', '#d2c1ce', '#d2c1ce', '#d2c1ce', '#d2c1ce', '#d2c1ce',
                                          '#d2c1ce', '#d2c1ce', '#d2c1ce'],
                              rowLabels=['2016', '2017', '2018'],
                              rowColours=['#b4bad4', '#b4bad4', '#b4bad4'],
                              bbox=[0.0, -0.55, 1, 0.3])  # [left, bottom, width, height]

        plt.xticks(rotation=0, horizontalalignment="right")
        plt.legend(title='Age Group', bbox_to_anchor=(1.0, 1), loc='upper left')
        plt.ylabel('Birth Count')
        plt.xlabel('Year')
        plt.title("Total Birth Count by Mother's Age Group and Year")
        plt.autoscale(enable=False)
        fig = plt.gcf()
        fig.set_size_inches(10, 8)
        plt.tight_layout()
        plt.show()


