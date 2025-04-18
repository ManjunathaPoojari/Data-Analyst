def total_players():
    import pandas as pd
    import matplotlib.pyplot as plt

    # Load the data
    import mysql.connector
    # Read the IPL captains' data from the CSV file

    con=mysql.connector.connect(host='localhost',
                                username='root',
                                password='root',
                                database='ipl')
    cursor=con.cursor()
    cursor.execute('select * from total_players')
    data=cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    df=pd.DataFrame(data=data,columns=columns)

    # Create the figure
    fig, ax1 = plt.subplots(figsize=(10, 6))  # Adjust figure size if needed

    # Data for the pie chart
    x = df['Year']
    y = df['Total Players']

    # Function to format the pie chart labels
    def func(pct, allvals):
        absolute = int(pct / 100. * sum(allvals))
        return f'{absolute}\n({pct:.1f}%)'

    # Create a pie chart
    ax1.pie(y, labels=x, autopct=lambda pct: func(pct, y), startangle=140, colors=plt.cm.tab10.colors)

    # Add a title
    plt.title('Proportion of Total Players in IPL by Year',
            fontdict={'fontsize': 18, 'color': 'darkcyan', 'family': 'Times New Roman'}, pad=20)

    # Show the plot
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.tight_layout()
    plt.show()