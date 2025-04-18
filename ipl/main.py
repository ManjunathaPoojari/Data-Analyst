from visualization.total_player_v import total_players
from visualization.purplecap_v import purplecap
from visualization.orangecap_v import orangecap
from visualization.list_of_100_v import list_of_100
from visualization.captains_v import captains
from visualization.captains_win_loss_v import captain_win_los
from visualization.year_v import year

def display_menu():
    print("\n" + "="*60)
    print("IPL DATA ANALYTICS DASHBOARD".center(60))
    print("="*60)
    print("Please choose one of the following options:\n")
    print("  1. Captain Statistics")
    print("  2. Captain Win/Loss Analysis (with Visualization)")
    print("  3. List of Centuries (100s)")
    print("  4. Orange Cap Holder Data")
    print("  5. Purple Cap Holder Data")
    print("  6. Total Players (2008–2024)")
    print("  7.Yearly winnings")
    print("  8. Exit\n")

while True:
    display_menu()
    user_choice = input("Enter your choice (1–7): ").strip()

    if user_choice == "1":
        captains()
    elif user_choice == "2":
        captain_win_los()
    elif user_choice == "3":
        list_of_100()
    elif user_choice == "4":
        orangecap()
    elif user_choice == "5":
        purplecap()
    elif user_choice == "6":
        total_players()
    elif user_choice == "7":
        year()
    elif user_choice == "8":
        print("\nThank you for using the IPL Analytics Dashboard.")
        break
    else:
        print(" Invalid selection. Please enter a number between 1 and 7.")
