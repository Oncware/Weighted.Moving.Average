# IMPORTANT!! : Add entries and exits in chronological order!!

This code implements a simple stock tracking application using a graphical user interface (GUI). The user can enter the initial quantity and unit price, add entry and exit movements, calculate the results based on stock movements, view the results, and save them to a CSV file.

Usage steps:

Enter the initial quantity and unit price in the "Initial Quantity (kg)" and "Initial Unit Price" fields, respectively.
To add an entry movement, enter the "Entry Date (DD.MM)" field, "Entry Quantity (kg)", and "Entry Unit Price" fields. Then, click the "Add Entry" button.
To add an exit movement, enter the "Exit Date (DD.MM)" field, "Exit Quantity (kg)", and "Exit Unit Price" fields. Then, click the "Add Exit" button.
After adding all entry and exit movements, click the "Calculate" button. This will perform calculations based on the stock movements and store the results in a data frame.
Click the "Show Results" button to view the results in a new window. The results will be displayed in a tree view.
To save the results, you can use the "Save Results" button. This will save the results to a CSV file. After the saving process, a successful message will be displayed.
Note: This code snippet uses the Pandas and Tkinter libraries. Make sure these libraries are installed. Also, remember to enter the entry and exit dates in the "DD.MM" format.
