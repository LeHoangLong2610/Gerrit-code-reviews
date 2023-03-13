import json
import requests
import pandas as pd
import os.path
import matplotlib.pyplot as plt
import os
from tkinter import messagebox


def get_code_review(date1, date2):
    #Get code review with API
    g_url = 'https://android-review.googlesource.com/changes/?q=after:' + date1 + '+' 'before:' + date2
    start = 0
    size = 2000
    all_reviews = []
    while True:
        #Construct the API request to get more than 2000 reviews
        url = g_url + "&S={}".format(size* start)
        respons = requests.get(url)
        if respons.status_code == 200:
            current_reviews = json.loads(respons.content[5:-1])
        
            #If it return an empty dict then break the loop
            if not current_reviews:
                break

            # Add the current reviews to all_reviews
            all_reviews.extend(current_reviews)
            start += 1
    
        else:
            #In case if the request fails!
            messagebox.showinfo("Error", f"Request failed with status code {respons.status_code}!")
    
    #Write it to a json file
    with open("android_review.json", "w") as savefile:
        json.dump(all_reviews, savefile)

        

def process_json_function(file_name = "android_review.json"):
    #Check if the json exist
    # file_name = "android_review.json"
    if os.path.isfile(file_name):
        with open(file_name, 'r') as file:
            file_data_string = json.load(file)
            #If the file is empty
            if file_data_string == []:
                return {}
            else:
                #Convert json to dict
                file_data_dict = pd.DataFrame(file_data_string).to_dict(orient="list")
                return file_data_dict
    else:
        return {}

def export_pdf(file_name = "android_review.json"):
    #Check if the JSON file exists and is not empty
    if not os.path.exists(file_name):
        messagebox.showinfo("Error!!", "No data to export yet!")
    else:
        #load the JSON data
        with open(file_name, 'r') as file:
            file_data_string = json.load(file)
            #If the file is empty
            if file_data_string == []:
                messagebox.showinfo("Error!!", "No data to export yet!")
            else:
                #Load the JSON data
                data = pd.read_json(file_name)

                # create a subplot for the two plots
                fig, (plot1, plot2) = plt.subplots(2, 1, figsize=(8, 8))

                #plot 1: number of code reviews based on status
                #count code reviews based on their status
                counts_status = data['status'].value_counts()

                #Create plot 1
                plot1.bar(counts_status.index, counts_status.values)
                plot1.set_title('Code Reviews by Status')
                plot1.set_xlabel('Status')
                plot1.set_ylabel('Number of Reviews')

                #plot 2: number of code reviews updated per hours or days
                #convert the update_time column to datetime
                data['updated'] = pd.to_datetime(data['updated'], format='%Y-%m-%d %H:%M:%S')

                #calculate the start and end dates of the data
                after_date = data['updated'].min().date()
                before_date = data['updated'].max().date()

                #if the time interval is one day, count reviews per hour
                if (before_date - after_date).days == 0:
                    counts_hours_days = data.groupby(data['updated'].dt.hour).size()
                    x_ticks = range(24)
                    x_label = 'Hour of the Day'
                    title = 'Android Code Reviews in Gerrit by Hour'
                #if the time interval is more than one days, count reviews per day
                elif (before_date - after_date).days >= 1:
                    counts_hours_days = data.groupby(data['updated'].dt.date).size()
                    x_ticks = counts_hours_days.index
                    x_label = 'Date'
                    title = 'Android Code Reviews in Gerrit by Day'

                #create the plot 2
                plot2.bar(x_ticks, counts_hours_days.values)
                plot2.set_title(title)
                plot2.set_xlabel(x_label)
                plot2.set_ylabel('Number of Reviews')
                plt.xticks(rotation=15, ticks=x_ticks)


                #adjust space between two plots
                fig.subplots_adjust(hspace=0.5)

                #save the plot as pdf file
                plt.savefig('Androids_reviews.pdf', bbox_inches='tight')
                os.system("start Androids_reviews.pdf")




