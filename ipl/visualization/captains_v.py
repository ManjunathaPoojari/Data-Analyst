def captains(): 
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

    # Filter the DataFrame for players who have played more than 45 matches and sort by 'Mat' in ascending order
    df = df[df['Mat'] > 45].sort_values(by='Mat', ascending=True)

    # Extract the 'Player', 'Mat', 'Won', and 'Lost' columns
    x = df['Player']
    y = df['Mat']
    z = df['Won']
    w = df['Lost']

    # Set the bar width for horizontal bars
    barwidth = 0.3

    # Set the positions of the bars
    index = np.arange(len(x))

    # Plot horizontal bars for 'Mat', 'Won', and 'Lost'
    plt.barh(index, y, barwidth, label='Matches', color='red')
    plt.barh(index + barwidth, z, barwidth, label='Won', color='yellow')
    plt.barh(index + 2 * barwidth, w, barwidth, label='Lost', color='green')

    # Add text labels for 'Mat' values
    for i, value in enumerate(y):
        plt.text(value + 0.5, i, str(y.iloc[i]), ha='left', va='center', fontdict={'fontsize': 8})

    # Add text labels for 'Won' values
    for i, value in enumerate(z):
        plt.text(value + 0.5, i + barwidth, str(z.iloc[i]), ha='left', va='center', fontdict={'fontsize': 8})

    # Add text labels for 'Lost' values
    for i, value in enumerate(w):
        plt.text(value + 0.5, i + 2 * barwidth, str(w.iloc[i]), ha='left', va='center', fontdict={'fontsize': 8})

    # Set labels and title for the plot
    plt.xlabel('No.of Matches, Won, Lost', fontdict={'fontsize': 15, 'family': 'Times New Roman', 'color': 'green'}, labelpad=10)
    plt.ylabel('Players', fontdict={'fontsize': 15, 'family': 'Times New Roman', 'color': 'green'}, labelpad=10)

    # Set y-tick labels to be player names
    plt.yticks(index + barwidth, x)

    # Set the title for the plot
    plt.title('Leading from the Front: Performance of IPL Captains in Matches Won and Lost', fontdict={'fontsize': 20, 'family': 'Times New Roman'})

    # Add a legend
    plt.legend()

    # Adjust the plot layout for better display
    plt.subplots_adjust(left=0.11, bottom=0.08, top=0.94, right=0.92)

    # Show the plot
    plt.show()
