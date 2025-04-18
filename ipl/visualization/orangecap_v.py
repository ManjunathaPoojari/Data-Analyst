def orangecap():
    import pandas as pd
    import matplotlib.pyplot as plt

    import mysql.connector
    # Read the IPL captains' data from the CSV file

    con=mysql.connector.connect(host='localhost',
                                username='root',
                                password='root',
                                database='ipl')
    cursor=con.cursor()
    cursor.execute('select * from orangecap')
    data=cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    df=pd.DataFrame(data=data,columns=columns)

    # Grouping data by 'Winners' and counting the number of times each winner has won
    df1 = df.groupby(by='Winners')['Winners'].count().reset_index(name='Times Won')

    # Extracting the winner names and the count of wins
    x = df1['Winners']
    y = df1['Times Won']

    # Get the unique winners for coloring the pie chart
    unique_winners = df1['Winners'].unique()

    # Generate a list of colors using a colormap
    colors = plt.cm.tab20c(range(len(unique_winners)))

    # Create a mapping of winner names to colors
    color_map = dict(zip(unique_winners, colors))

    # Create a figure with two subplots (ax1 for the table, ax2 for the pie chart)
    fig, (ax1, ax2) = plt.subplots(1, 2)

    # Pie chart for the number of wins of each winner
    ax2.pie(y, startangle=90, autopct='%1.1f%%', 
            wedgeprops={'width': 0.4, 'edgecolor': 'white'},  # Customizing wedge properties
            colors=[color_map[winner] for winner in x],  # Assign colors based on winner
            rotatelabels=30, pctdistance=0.8)  # Customize label rotation and position

    # Add a white circle in the middle of the pie chart to make it look like a donut chart
    circle = plt.Circle((0, 0), 0.40, fc='white')
    ax2.add_artist(circle)

    # Add a legend to the pie chart showing the winner names
    ax2.legend(labels=[i for i in x], bbox_to_anchor=(1, 0, 0, 0.8), title="Players")

    # Create a table in the first subplot with the grouped data (winner and times won)
    table_data = df1.values
    table = ax1.table(cellText=table_data, colLabels=df1.columns, loc='center')

    # Customize the table font size and scale
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(0.9, 0.9)

    # Color each row in the table according to the corresponding winner's color
    for i in range(len(x)):
        winner_name = x.iloc[i]
        table[(i + 1, 0)].set_facecolor(color_map[winner_name])  # Color the 'Winner' column
        table[(i + 1, 1)].set_facecolor(color_map[winner_name])  # Color the 'Times Won' column

    # Hide the axes of the table subplot (ax1)
    ax1.axis('off')

    # Set the title of the entire figure
    fig.suptitle("Dominating the Runs: Orange Cap Champions of IPL", y=0.95, fontsize=14)

    # Adjust the layout for better spacing and display the plot
    plt.tight_layout()
    plt.show()
