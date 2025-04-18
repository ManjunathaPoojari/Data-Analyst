def year():
    import mysql.connector
    import matplotlib.pyplot as plt
    import pandas as pd

    # Connect to MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="ipl"
    )

    # Query: Fetch title winners by year
    query = "SELECT year, winner FROM teamstitles"
    df = pd.read_sql(query, conn)

    # Close connection
    conn.close()
    df['team'] = df['winner'].apply(lambda x: ''.join([word[0].upper() for word in x.split()]))
    # Group by winner and count titles
    title_counts = df['team'].value_counts()
    title_years = df.sort_values(by='year')

    # Visualization with subplots
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # 1. Bar plot: Total titles per team
    axes[0].bar(title_counts.index, title_counts.values, color='skyblue')
    axes[0].set_title('Total IPL Titles by Team')
    axes[0].set_xlabel('Team')
    axes[0].set_ylabel('Titles')
    axes[0].tick_params(axis='x', rotation=45)

    # 2. Line plot: Title winner per year
    axes[1].plot(title_years['year'], title_years['winner'], marker='o', linestyle='-')
    axes[1].set_title('IPL Title Winners Over the Years')
    axes[1].set_xlabel('Year')
    axes[1].set_ylabel('Winner')
    axes[1].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    plt.show()
