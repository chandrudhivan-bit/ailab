
# Waste Classification and Management System

import datetime

# Store classification history
waste_history = []

# Waste categories and their items
waste_data = {
    "Biodegradable": [
        "food waste", "vegetable peels", "fruit peels",
        "leaves", "flowers", "egg shells", "tea leaves",
        "grass", "leftover food"
    ],
    "Recyclable": [
        "plastic bottle", "glass bottle", "newspaper",
        "cardboard", "metal can", "aluminium can",
        "paper", "plastic container", "steel can"
    ],
    "Hazardous": [
        "battery", "paint", "chemical", "pesticide",
        "medical waste", "bulb", "tube light",
        "expired medicine", "cleaning chemical"
    ],
    "Non-Recyclable": [
        "thermocol", "chip packet", "diaper",
        "sanitary waste", "ceramic", "used tissue",
        "broken mirror", "dirty plastic wrapper"
    ],
    "Electronic Waste": [
        "mobile phone", "computer", "keyboard",
        "mouse", "charger", "television",
        "printer", "earphones", "laptop"
    ]
}

# Disposal suggestions
disposal_tips = {
    "Biodegradable": "Use a compost bin to produce natural manure.",
    "Recyclable": "Clean and place the item in the appropriate recycling bin.",
    "Hazardous": "Take it to an authorized hazardous waste collection centre.",
    "Non-Recyclable": "Follow local waste disposal guidelines.",
    "Electronic Waste": "Send it to an authorized e-waste collection centre."
}


def classify_waste(item):
    item = item.lower().strip()

    for category, items in waste_data.items():
        if item in items:
            return category

    return "Unknown"


def add_waste():
    print("\n--- WASTE CLASSIFICATION ---")
    item = input("Enter the waste item name: ").strip()

    if not item:
        print("Error: Waste item cannot be empty.")
        return

    category = classify_waste(item)

    if category == "Unknown":
        suggestion = "Check local waste management guidelines."
    else:
        suggestion = disposal_tips[category]

    record = {
        "item": item.title(),
        "category": category,
        "suggestion": suggestion,
        "date": datetime.datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )
    }

    waste_history.append(record)

    print("\nClassification Result")
    print("---------------------")
    print("Waste Item :", record["item"])
    print("Category   :", record["category"])
    print("Suggestion :", record["suggestion"])
    print("Date       :", record["date"])


def display_categories():
    print("\n--- AVAILABLE WASTE CATEGORIES ---")

    for category, items in waste_data.items():
        print("\n" + category + " Waste")
        print("-" * 30)

        for item in items:
            print("  -", item.title())


def view_history():
    print("\n--- WASTE CLASSIFICATION HISTORY ---")

    if not waste_history:
        print("No waste items have been classified yet.")
        return

    for number, record in enumerate(waste_history, start=1):
        print("\nRecord", number)
        print("Item       :", record["item"])
        print("Category   :", record["category"])
        print("Suggestion :", record["suggestion"])
        print("Date       :", record["date"])


def show_statistics():
    print("\n--- WASTE STATISTICS ---")

    if not waste_history:
        print("No statistics available. Classify waste first.")
        return

    total = len(waste_history)
    counts = {}

    for record in waste_history:
        category = record["category"]
        counts[category] = counts.get(category, 0) + 1

    print("Total Items Classified:", total)

    for category, count in counts.items():
        percentage = (count / total) * 100
        print(
            category + ":",
            count,
            "item(s) -",
            round(percentage, 2),
            "%"
        )


def search_waste():
    print("\n--- SEARCH WASTE ITEM ---")
    keyword = input("Enter item name to search: ").strip().lower()

    if not keyword:
        print("Please enter a search keyword.")
        return

    found = False

    for category, items in waste_data.items():
        for item in items:
            if keyword in item:
                print(item.title(), "->", category)
                found = True

    if not found:
        print("No matching item found in the database.")


def classify_multiple():
    print("\n--- MULTIPLE WASTE CLASSIFICATION ---")

    try:
        number = int(input("How many items do you want to enter? "))

        if number <= 0:
            print("Enter a positive number.")
            return

    except ValueError:
        print("Invalid input. Enter a whole number.")
        return

    for i in range(number):
        print("\nItem", i + 1)
        item = input("Enter waste item: ").strip()

        if not item:
            print("Empty item skipped.")
            continue

        category = classify_waste(item)

        record = {
            "item": item.title(),
            "category": category,
            "suggestion": disposal_tips.get(
                category,
                "Check local waste management guidelines."
            ),
            "date": datetime.datetime.now().strftime(
                "%d-%m-%Y %H:%M:%S"
            )
        }

        waste_history.append(record)

        print("Classification:", category)


def main():
    while True:
        print("\n" + "=" * 48)
        print("       WASTE CLASSIFICATION SYSTEM")
        print("=" * 48)
        print("1. Classify a Waste Item")
        print("2. Display Waste Categories")
        print("3. View Classification History")
        print("4. Show Waste Statistics")
        print("5. Search Waste Items")
        print("6. Classify Multiple Items")
        print("7. Exit")
        print("=" * 48)

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_waste()
        elif choice == "2":
            display_categories()
        elif choice == "3":
            view_history()
        elif choice == "4":
            show_statistics()
        elif choice == "5":
            search_waste()
        elif choice == "6":
            classify_multiple()
        elif choice == "7":
            print("\nThank you for using the system!")
            print("Keep your environment clean and green.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()