# Gerrit-code-reviews
- This is a Python program designed to extract code review data from Gerrit, and save it to a JSON file. The program can also display the review data in a table and export it as a PDF file.

#Installation
- You need to first download and extract the .zip file. 
- To run this program you need to have Python installed on your device.
- You can download and install Python from this website https://www.python.org/downloads/.
- Then navigate to the directory where the requ file is located using the 'cd' command. For example "cd C:\Users\Documents\pythonGerrit"
- Then you need to run this command 'pip install -r requirements.txt' in your terminal or command prompt, so that the program can run smoothly.

#How to run the program
- Then open a terminal or command prompt on your device.
- Navigate to the directory where the GUI.py file is located using the 'cd' command. For example "cd C:\Users\Documents\pythonGerrit"
- Then you can run the GUI.py file using this command "python GUI.py"

#Usage
- To use the program, you need to run the file GUI.py
- The 'uppdates' button is used to get data from Gerrit, but before using it you need to put data in the day 'before' and 'after' first. 
- The 'show' button is used to display the data that we get from Gerrit.
- The 'export' button is to export the plots of data as a .pdf file.
- Don't change anything in the 'android_review.json' or it will cause the program to crash. 


#Description
- All the main function is located in the file 'main.py', it has 3 main functions in it: 
+ 'get_code_review()': send API requests and save the data to 'android_review.json' file.
+ 'process_json_function()': it takes data from 'android_review.json' file and converts it to a dict, and returning it so that it can be displayed in a table in the GUI.
+ 'export_pdf()': it exports the data as a plot as a .pdf file. 

- GUI's function is located in the file 'GUI.py', it's nothing special here other than it just takes the functions from the 'main.py' file and displays the results.
