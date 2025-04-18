def list_of_100():
    import pandas as pd
    import matplotlib.pyplot as plt

    import mysql.connector
    # Read the IPL captains' data from the CSV file

    con=mysql.connector.connect(host='localhost',
                                username='root',
                                password='root',
                                database='ipl')
    cursor=con.cursor()
    cursor.execute('select * from list_of_100')
    data=cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    df=pd.DataFrame(data=data,columns=columns)

    # Select relevant columns and remove duplicate entries
    df = df[['Player', 'total hundreds', 'total runs by 100s']].drop_duplicates()

    # Filter the dataset to include only players with more than 1 hundred
    df = df[df['total hundreds'] > 1]

    # Sort the data by total runs scored from hundreds in descending order
    df = df.sort_values(by='total runs by 100s', ascending=False)

    # Prepare the data for plotting
    x = df['Player']  # Player names
    y = df['total hundreds']  # Total hundreds by players
    z = df['total runs by 100s']  # Total runs from hundreds

    # Create a bar plot
    bars = plt.bar(x, y)

    # Assign colors to the bars based on the index of each player
    colors = [plt.cm.BrBG(1 - i / len(x)) for i in range(len(x))]

    # Set the colors of the bars
    for bar, color in zip(bars, colors):
        bar.set_color(color)

    # Annotate the bars with the total runs scored by 100s
    for i, Value in enumerate(y):
        plt.text(i, Value, str(z.iloc[i]), ha='center', va='bottom')

    # Rotate the x-axis labels for better readability
    plt.xticks(rotation=45)

    # Set the title of the plot
    plt.title('Dominating the Field by Runs in Hundreds: A Player-Wise Breakdown', 
            fontdict={'fontsize': 20, 'family': 'Times New Roman'}, pad=10)

    # Set labels for the x-axis and y-axis
    plt.xlabel('Players', fontdict={'fontsize': 15, 'color': 'Green', 'family': 'Times New Roman'}, labelpad=10)
    plt.ylabel("Total No.Of 100's by Players", fontdict={'fontsize': 15, 'color': 'Green', 'family': 'Times New Roman'}, labelpad=10)

    # Adjust the layout of the plot
    plt.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.171)

    # Show the plot
    plt.show()
