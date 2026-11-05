"""
Campus Lost & Found Management System
A beginner-friendly Python project for managing lost and found items on campus.
"""

import json
from pathlib import Path
from datetime import datetime

DATA_FILE = Path("campus_items.json")


def load_items():
    """Load item records from the JSON file."""
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read saved records. Starting with an empty list.")
        return []


def save_items(items):
    """Save all item records to the JSON file."""
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(items, file, indent=4)


def next_item_id(items):
    """Generate a simple unique ID for each report."""
    return max((item["id"] for item in items), default=1000) + 1


def report_item(items, status):
    """Add a lost or found item report."""
    print(f"\n--- Report a {status.title()} Item ---")
    name = input("Item name: ").strip()
    category = input("Category (ID Card/Books/Electronics/Accessories/Other): ").strip()
    location = input("Where was it lost/found? ").strip()
    description = input("Description (colour, brand, identifying details): ").strip()
    contact = input("Contact detail (email or phone): ").strip()

    if not all([name, category, location, description, contact]):
        print("All fields are required. Report was not saved.")
        return

    item = {
        "id": next_item_id(items),
        "status": status,
        "name": name,
        "category": category,
        "location": location,
        "description": description,
        "contact": contact,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    items.append(item)
    save_items(items)
    print(f"\nReport saved! Your report ID is LF-{item['id']}.")


def display_item(item):
    """Print one item in a readable format."""
    print("-" * 58)
    print(f"Report ID   : LF-{item['id']}")
    print(f"Status      : {item['status'].upper()}")
    print(f"Item        : {item['name']}")
    print(f"Category    : {item['category']}")
    print(f"Location    : {item['location']}")
    print(f"Description : {item['description']}")
    print(f"Contact     : {item['contact']}")
    print(f"Reported on : {item['date']}")


def view_items(items, status=None):
    """Display all reports or reports of one status."""
    selected = items if status is None else [
        item for item in items if item["status"] == status
    ]

    if not selected:
        print("\nNo matching reports found.")
        return

    print(f"\n--- {status.title() if status else 'All'} Reports ---")
    for item in selected:
        display_item(item)
    print("-" * 58)


def search_items(items):
    """Search reports using an item name, category, or location."""
    keyword = input("\nEnter item name, category, or location to search: ").strip().lower()

    if not keyword:
        print("Please enter a search term.")
        return

    results = [
        item for item in items
        if keyword in item["name"].lower()
        or keyword in item["category"].lower()
        or keyword in item["location"].lower()
        or keyword in item["description"].lower()
    ]

    if results:
        print(f"\nFound {len(results)} matching report(s):")
        for item in results:
            display_item(item)
    else:
        print("\nNo reports matched your search.")


def find_possible_matches(items):
    """Suggest possible lost/found matches based on shared keywords."""
    lost_items = [item for item in items if item["status"] == "lost"]
    found_items = [item for item in items if item["status"] == "found"]
    matches = []

    for lost in lost_items:
        for found in found_items:
            same_name = lost["name"].strip().lower() == found["name"].strip().lower()
            same_category = lost["category"].strip().lower() == found["category"].strip().lower()
            if same_name or same_category:
                matches.append((lost, found))

    if not matches:
        print("\nNo possible matches found yet.")
        return

    print("\n--- Possible Lost & Found Matches ---")
    for lost, found in matches:
        print(f"\nLost report: LF-{lost['id']} - {lost['name']} ({lost['category']})")
        print(f"Found report: LF-{found['id']} - {found['name']} ({found['category']})")
        print("Please compare descriptions and contact the reporter to verify ownership.")
    print("\nNote: These are suggestions, not confirmed matches.")


def mark_resolved(items):
    """Remove a report after the item has been returned or collected."""
    try:
        report_id = int(input("Enter report ID number (e.g. 1001): ").strip())
    except ValueError:
        print("Please enter a numeric report ID.")
        return

    for item in items:
        if item["id"] == report_id:
            confirmation = input(
                f"Mark '{item['name']}' as resolved and remove its report? (yes/no): "
            ).strip().lower()
            if confirmation == "yes":
                items.remove(item)
                save_items(items)
                print("Report marked as resolved.")
            else:
                print("No changes made.")
            return

    print("Report ID not found.")


def main():
    items = load_items()

    while True:
        print("\n" + "=" * 48)
        print("       CAMPUS LOST & FOUND MANAGEMENT")
        print("=" * 48)
        print("1. Report a lost item")
        print("2. Report a found item")
        print("3. View all reports")
        print("4. View only lost items")
        print("5. View only found items")
        print("6. Search for an item")
        print("7. Find possible lost/found matches")
        print("8. Mark an item as resolved")
        print("9. Exit")
        print("=" * 48)

        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            report_item(items, "lost")
        elif choice == "2":
            report_item(items, "found")
        elif choice == "3":
            view_items(items)
        elif choice == "4":
            view_items(items, "lost")
        elif choice == "5":
            view_items(items, "found")
        elif choice == "6":
            search_items(items)
        elif choice == "7":
            find_possible_matches(items)
        elif choice == "8":
            mark_resolved(items)
        elif choice == "9":
            print("Thank you for using Campus Lost & Found!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 9.")


if __name__ == "__main__":
    main()
