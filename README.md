# Campus Lost & Found Management System

## Project Overview
Campus Lost & Found is a menu-driven Python application that helps students report and search for belongings lost or found around a college campus. It provides a simple way to keep reports organized instead of depending only on verbal announcements or scattered messages.

## Real-Life Problem
Students may misplace items such as ID cards, notebooks, water bottles, chargers, and other belongings. It can be difficult to find the owner of an item or discover whether someone has reported it. This project keeps lost and found reports in one searchable place.

## Main Features
1. Report a lost item.
2. Report a found item.
3. View all reports.
4. Filter lost and found reports separately.
5. Search by item name, category, location, or description.
6. Suggest possible matches between lost and found reports.
7. Mark a report as resolved after the item is returned.
8. Save data in a JSON file so reports remain available after closing the program.

## Technologies Used
- Python 3
- JSON file handling
- Lists and dictionaries
- Functions and loops
- Conditional statements
- Exception handling
- `datetime` and `pathlib` modules

## How to Run
1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

   ```bash
   python main.py
   ```

5. Follow the numbered menu.

## Files
- `main.py` — application source code.
- `campus_items.json` — created automatically when the first report is saved.
- `.gitignore` — prevents local data and cache files from being uploaded.
- `README.md` — project documentation.

## Important Note
Possible matches are only suggestions based on item name or category. A person should verify the item's identifying details before claiming it. For a public demonstration, use sample contact details rather than real personal information.

## Future Improvements
- Add a graphical user interface.
- Add password-protected administrator access.
- Add photo uploads for item reports.
- Add email notifications when a possible match is found.

## Author
Add your name and class details here.
