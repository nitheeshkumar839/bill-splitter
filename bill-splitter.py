import math
import time

def split_evenly(total_bill, num_people, names):
    """Split bill evenly among all participants."""
    amount_each = round(total_bill / num_people, 2)
    result = {}
    for name in names:
        result[name] = amount_each
    return result


def split_by_percentage(total_bill, names):
    """Split bill based on custom percentages."""
    percentages = []
    print("\nEnter each person's contribution percentage:")

    for name in names:
        while True:
            try:
                percent = float(input(f"  {name}'s percentage: "))
                if percent < 0:
                    print("❌ Percentage cannot be negative.")
                else:
                    percentages.append(percent)
                    break
            except ValueError:
                print("❌ Please enter a valid number.")

    # Validate total percentage
    total_percent = sum(percentages)
    if round(total_percent, 2) != 100.0:
        print(f"\n⚠️ Error: Total percentage is {total_percent}%. It must equal 100%.")
        return None

    # Calculate contribution for each person
    result = {}
    for i, name in enumerate(names):
        result[name] = round(total_bill * (percentages[i] / 100), 2)
    return result


def export_to_file(results, total_bill):
    """Save results to a text file."""
    filename = f"bill_split_{int(time.time())}.txt"
    with open(filename, "w") as file:
        file.write("===== Bill Split Summary =====\n")
        file.write(f"Total Bill: ${total_bill:.2f}\n\n")
        for name, amount in results.items():
            file.write(f"{name}: ${amount:.2f}\n")
        file.write("\n===============================\n")
    print(f"\n💾 Results saved to {filename}")


def main():
    print("===================================")
    print(" 💸 Bill Splitter for Groups 💸")
    print("===================================")

    while True:
        try:
            total_bill = float(input("\nEnter the total bill amount: $"))
            if total_bill <= 0:
                print("❌ Total bill must be greater than zero.")
                continue
            num_people = int(input("Enter the number of people: "))
            if num_people <= 0:
                print("❌ Number of people must be greater than zero.")
                continue
        except ValueError:
            print("❌ Please enter valid numeric values.")
            continue

        # Get participant names
        names = []
        print("\nEnter names of each person:")
        for i in range(num_people):
            name = input(f"  Person {i+1} name: ").strip()
            if not name:
                name = f"Person_{i+1}"
            names.append(name)

        # Choose split type
        print("\nHow would you like to split the bill?")
        print("1️⃣ Evenly")
        print("2️⃣ By percentage")
        choice = input("Choose 1 or 2: ")

        if choice == "1":
            results = split_evenly(total_bill, num_people, names)
        elif choice == "2":
            results = split_by_percentage(total_bill, names)
            if results is None:
                continue
        else:
            print("❌ Invalid choice. Try again.")
            continue

        # Display results
        print("\n===== Split Summary =====")
        for name, amount in results.items():
            print(f"{name}: ${amount:.2f}")
        print("=========================")

        # Optional: Export results
        save_choice = input("\nWould you like to save the results to a .txt file? (y/n): ").lower()
        if save_choice == "y":
            export_to_file(results, total_bill)

        # Multiple splits in one session
        again = input("\nDo you want to perform another split? (y/n): ").lower()
        if again != "y":
            print("\n✅ Thank you for using Bill Splitter! Goodbye.")
            break
        time.sleep(1)


if __name__ == "__main__":
    main()
