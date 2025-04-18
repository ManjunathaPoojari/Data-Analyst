def captain_win_los():
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    import mysql.connector
    # Read the IPL captains' data from the CSV file

    con=mysql.connector.connect(host='localhost',
                                username='root',
                                password='root',
                                database='ipl')
    cursor=con.cursor()
    cursor.execute('select * from captains')
    data=cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    df=pd.DataFrame(data=data,columns=columns)
    # Filter the DataFrame for players who have played more than 45 matches and sort by 'Mat' in descending order
    df = df[df['Mat'] > 45].sort_values(by='Mat', ascending=False)

    # Extract the 'Player' and 'Won%' columns as x and y values
    x = df['Player']
    y = df['Won%']
    w = df['Lost%']

    # Set explode parameter to highlight the top player in the pie charts
    explode = [0] * len(df['Player'])
    explode[0] = 0.07  # Highlight the first player with a small explosion

    # Create labels for percentages with '%' symbol for 'Won%' and 'Lost%'
    label1 = [f'{i}%' for i in y]
    label2 = [f'{i}%' for i in w]

    # Create two subplots: one for win percentage, one for loss percentage
    fig, (ax1, ax2) = plt.subplots(1, 2)

    # Plot the pie chart for 'Won%' with labels, rotation, and exploded slices
    ax1.pie(y, labels=label1, rotatelabels=30, labeldistance=0.7, explode=explode, startangle=90)

    # Add a legend for the pie chart showing the players' names
    ax1.legend([i for i in x], bbox_to_anchor=(0.95, 0, 0, 0.8), title="Captain's", frameon=False)

    # Plot the pie chart for 'Lost%' with labels, rotation, and exploded slices
    ax2.pie(y, labels=label2, rotatelabels=30, labeldistance=0.7, explode=explode, startangle=90)

    # Add a title for the overall figure
    plt.suptitle("Winning Leadership: Exploring Captains' Win Percentages & Loss Percentages", color='seagreen')

    # Display the plot
    plt.show()
