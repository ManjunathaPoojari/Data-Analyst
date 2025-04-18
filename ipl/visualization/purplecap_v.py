def purplecap():
    import pandas as pd
    import matplotlib.pyplot as plt

    import mysql.connector
    # Read the IPL captains' data from the CSV file

    con=mysql.connector.connect(host='localhost',
                                username='root',
                                password='root',
                                database='ipl')
    cursor=con.cursor()
    cursor.execute('select * from purplecap')
    data=cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    df=pd.DataFrame(data=data,columns=columns)

    # Step 2: Group Data and Prepare for Visualization
    # Group the data by 'Winner' column and count the number of occurrences (times won by each player)
    df1 = df.groupby(by='Winner')['Winner'].count().reset_index(name='Times Won')

    # Step 3: Prepare Data for Plotting
    # Extract the winner names and the count of wins into variables
    x = df1['Winner']  # Umpire names (winners)
    y = df1['Times Won']  # Number of times each player has won the Purple Cap

    # Step 4: Generate Colors for Visualization
    # Create a color map using 'tab20' colormap, which will assign unique colors for each winner
    unique_winners = df1['Winner'].unique()
    colors = plt.cm.tab20(range(len(unique_winners)))
    color_map = dict(zip(unique_winners, colors))  # Map winner names to corresponding colors

    # Step 5: Create a Figure with Two Subplots (Pie Chart and Table)
    # Create a figure with two subplots, one for the pie chart and one for the table
    fig, (ax1, ax2) = plt.subplots(1, 2)

    # Step 6: Plot Pie Chart
    # Create a pie chart on ax1 to show the distribution of Purple Cap wins
    ax1.pie(y, startangle=90, autopct='%1.1f%%',  # Format the pie chart labels to show percentage
            wedgeprops={'width': 0.4, 'edgecolor': 'white'},  # Customizing wedge properties
            colors=[color_map[winner] for winner in x],  # Assign colors based on winner
            rotatelabels=30, pctdistance=0.8)  # Customize label rotation and position

    # Add a white circle in the middle of the pie chart to make it look like a donut chart
    circle = plt.Circle((0, 0), 0.40, fc='white')
    ax1.add_artist(circle)

    # Add a legend to the pie chart showing the winner names
    ax1.legend(labels=[i for i in x], bbox_to_anchor=(0, 0, 0, 0.8), title="Players")

    # Step 7: Create Table on the Second Subplot
    # Create a table on ax2 to show the number of wins for each player
    table_data = df1.values
    table = ax2.table(cellText=table_data, colLabels=df1.columns, loc='center')

    # Customize the table appearance
    table.auto_set_font_size(False)  # Disable auto font size
    table.set_fontsize(10)  # Set font size for the table
    # Color each row in the table according to the corresponding winner's color
    for i in range(len(x)):
        winner_name = x.iloc[i]
        table[(i + 1, 0)].set_facecolor(color_map[winner_name])  # Color the 'Winner' column
        table[(i + 1, 1)].set_facecolor(color_map[winner_name])  # Color the 'Times Won' column

    # Step 8: Customize and Display the Plot
    # Hide the axes of the table subplot (ax2)
    ax2.axis('off')

    # Add a title to the entire figure
    fig.suptitle("Dominating the wickets: purple Cap Champions of IPL", y=0.95, fontsize=14)

    # Adjust layout for better spacing
    plt.tight_layout()

    # Adjust subplot margins for better presentation
    plt.subplots_adjust(left=0.2, bottom=0.1, top=0.9, right=0.89)

    # Step 9: Show the Plot
    # Display the plot
    plt.show()
