

#Tharinda Nimnajith Rajapaksha
#SLIIT

#AIE Machine Learning & Image Processing Course
#Final Project

#Topic : Hotel Room Availability Prediction using Machine Learning

#Machine Learning Algorithm : Linear Regression Algorithm

#Used Technologies :
    #Python 3.6
    #Tkinter Library for GUI
    #Other necessary python libraries such as pandas, numpy, pickle, scikit-learn, ctypes, dateutil and matplotlib etc.

#Date Created  : 19.06.2019
#Last Modified : 25.08.2019



#Reading the data from the csv file

import pandas as pd

#Read data from csv file
hotel_data = pd.read_csv(r'E:\SLIIT\Machine Learning (ML) & Image Processing (IP)\ML Project\final.csv')
#print(hotel_data)



##Trying to use the group by clause to get average room occupancy for a given date
##
##Load data from csv file
##df = pd.DataFrame(hotel_data)
##print(df)
##
##
##Convert date from string to date times
##
##import dateutil
##
##df['Date'] = df['Date'].apply(dateutil.parser.parse, dayfirst = True)
##print(df)
##
##
##Group by clause
##
##df.groupby(['Date']).groups.keys()
##
##print(df.groupby(['Date']).groups.keys())
##Prints all dates of the data set in a alphebetic order
##
##print(len(df.groupby(['Date']).groups.keys()))
##365
##
##
##Getting average / mean
##
##df.groupby('Date')[['Count']].mean()
##print(df.groupby('Date')[['Count']].mean())
##
##final_data = df.groupby('Date')[['Count']].mean()
##print(final_data)
##
##
##final_data = pd.DataFrame(final_data)
##print(final_data)
##
##
##hotel_data = final_data
##
##
##Trying to remove the index
##
##data1 = pd.DataFrame(final_data, columns = ['Date'])
##data1.set_index('Date', inplace = True)
##print(data1)
##
##data2 = pd.DataFrame(final_data, columns = ['Count'])
##data2.set_index('Count', inplace = True)
##print(data2)
##
##
##dates1 = data1.index.values
##print(dates1)
##
##count1 = data2.index.values
##print(count1)



df1 = pd.DataFrame(hotel_data, columns = ['Date'])
df1.set_index('Date', inplace = True)
#print(df1)

df2 = pd.DataFrame(hotel_data, columns = ['Count'])
df2.set_index('Count', inplace = True)
#print(df2)



##Trying to remove the index
##
##hotel_data = pd.read_csv(r'E:\SLIIT\Machine Learning (ML) & Image Processing (IP)\ML Project\final.csv', index_col = False)
##print(hotel_data)
##
##df = pd.DataFrame(hotel_data, columns = ['Date', 'Count'])
##df.reset_index(drop = True, inplace = True)
##print(df)



##Reading the data from the excel file
##
##import pandas as pd
##
##hotel_data = pd.read_excel(r'E:\SLIIT\Machine Learning (ML) & Image Processing (IP)\ML Project\final.xlsx')
##print(hotel_data)
##
##df = pd.DataFrame(hotel_data, columns = ['Date', 'Count'])
##print(df)



#Assigning the data in each column to variables

##dates = df['Date']
##print(dates)
##
##count = hotel_data['Count']
##print(count)

dates = df1.index.values
#print(dates)

count = df2.index.values
#print(count)



#Storing the data in pickle files

import pickle

#open files
train_data_file = open('train_data.pickle', 'wb')
train_target_file = open('train_target.pickle', 'wb')
#wb = write in bytes

#write data in files
pickle.dump(dates, train_data_file)
pickle.dump(count, train_target_file)
#dump = write

#close the opened files after writing
train_data_file.close()
train_target_file.close()



#Reading data from the pickle files

#import pickle

#open files
data_file = open('train_data.pickle', 'rb')
target_file = open('train_target.pickle', 'rb')
#rb = read in bytes

#read data from files
data = pickle.load(data_file)
target = pickle.load(target_file)
#load = read

#close the opened files after writing
train_data_file.close()
train_target_file.close()


##print(data)
##print(target)
##
##print(len(data))
##print(len(target))



#Drawing the reserved hotel rooms scatter graph from the data

def button1_pressed():
    
    from matplotlib import pyplot as plt

    #print(dates)
    #print(count)

    #plt.plot(dates, count, 'r')
    plt.scatter(dates, count, label = 'Room Count')
    #Date of the year to x-axis
    #The number of rooms reserved to y-axis


    ##Trying to solve the x-axis overcrowding issue
    ##
    ##dates = pd.to_datetime(dates)
    ##
    ##xlabels = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    ##
    ##xlabelsnew = []
    ##
    ##for i in xlabels:
    ##    xlabelsnew.append(i)
    ##
    ##plt.xticks(range(0, 12), xlabelsnew, rotation = 45)


    #Formatting and displaying the scatter graph

    plt.xticks(rotation = 90)

    plt.xlabel('Date')
    plt.ylabel('Room Count')

    plt.legend()
    plt.title('Hotel Rooms Reservation')
    plt.savefig('Hotel Rooms Reservation.png')
    plt.show()



#Drawing the available hotel rooms scatter graph from the data

def button2_pressed():
    
    from matplotlib import pyplot as plt

    total_rooms = 48
    #Total number of rooms in the hotel = 48

    #plt.plot(dates, count, 'b')
    plt.scatter(dates, total_rooms - count, label = 'Room Count')
    #Date of the year to x-axis
    #The number of rooms available to y-axis


    ##Trying to solve the x-axis overcrowding issue
    ##
    ##dates = pd.to_datetime(dates)
    ##
    ##xlabels = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    ##
    ##xlabelsnew = []
    ##
    ##for i in xlabels:
    ##    xlabelsnew.append(i)
    ##
    ##plt.xticks(range(0, 12), xlabelsnew, rotation = 45)


    #Formatting and displaying the scatter graph

    plt.xticks(rotation = 90)

    plt.xlabel('Date')
    plt.ylabel('Room Count')

    plt.legend()
    plt.title('Hotel Rooms Availability')
    plt.savefig('Hotel Rooms Availability.png')
    plt.show()



#Predict results for room reservations

def predict():
    
    month = combo1.get()
    #print(month)

    day = combo2.get()
    #print(day)


    #Checking if the entered date is valid or not

    
    #Checking for any run time exceptions and if any then exception handling

    try:

        #if invalid
        
        if((day == '30' and month == 'February') or
           (day == '31' and (month == 'February' or month == 'April' or month == 'June' or month == 'September' or month == 'November')) or
           (int(day) > 31) or
           (month != 'January' and month != 'February' and month != 'March' and month != 'April' and month != 'May' and month != 'June' and month != 'July' and
            month != 'August' and month != 'September' and month != 'October' and month != 'November' and month != 'December')):

                #Display the error in the python shell
                print()
                print('Invalid Date! Please Check and Enter a Valid Date and Try Again')
                print()

                #Display the error in a message box
                import ctypes   
                ctypes.windll.user32.MessageBoxW(0, 'Invalid Date! Please Check and Enter a Valid Date and Try Again', 'ERROR!', 1)


        #if valid
            
        else:
            
            #Getting the first 3 letters of month names
            month = month[:3]


            #Converting date to correct format
            
            day_no = str(day) + '-' + month
            #print(day_no)


            #Converting month and date into integer values
            
            month_name = day_no[-3:]
            #print(month_name)

            
            date_month_without_white_space = ''.join(day_no.split())
            #print(date_month_without_white_space)
            
            date_month_without_last_four_characters = date_month_without_white_space[:-4]
            #print(date_month_without_last_four_characters)
            
            date_number = int(date_month_without_last_four_characters)
            #print(date_number)


            if(month_name == 'Jan'):
                date_index = date_number
                
            elif(month_name == 'Feb'):
                date_index = date_number + 31
                
            elif(month_name == 'Mar'):
                date_index = date_number + 59
                
            elif(month_name == 'Apr'):
                date_index = date_number + 90
                
            elif(month_name == 'May'):
                date_index = date_number + 120
                
            elif(month_name == 'Jun'):
                date_index = date_number + 151
                
            elif(month_name == 'Jul'):
                date_index = date_number + 181
                
            elif(month_name == 'Aug'):
                date_index = date_number + 212
                
            elif(month_name == 'Sep'):
                date_index = date_number + 243
                
            elif(month_name == 'Oct'):
                date_index = date_number + 273
                
            elif(month_name == 'Nov'):
                date_index = date_number + 304
                
            elif(month_name == 'Dec'):
                date_index = date_number + 334

            else:
                print('Invalid Month Name')

                
            #print(date_index)


            #Predicting results
            result = classifier.predict([[date_index]])
            #print(result)

            
            #Rounding to the nearest integer
            result = np.round(result)
            #print(result)


            #Formatting the result
            
            result = str(result)
            #print(result)

            result_without_white_space = ''.join(result.split())
            #print(result_without_white_space)
            
            result_without_last_two_characters = result_without_white_space[:-2]
            #print(result_without_last_two_characters)

            result_without_first_character = result_without_last_two_characters[1:]
            #print(result_without_first_character)

            result = result_without_first_character

            
            #Printing the result in the label
            label_predict.config(text = result)


    #Handling if any exception occurs   
        
    except ValueError:
        
        #Display the error in the python shell
        print()
        print('Value Error! Please Check and Enter a Valid Date and Try Again')
        print()

        #Display the error in a message box
        import ctypes   
        ctypes.windll.user32.MessageBoxW(0, 'Value Error! Please Check and Enter a Valid Date and Try Again', 'ERROR!', 1)

                    
    except TypeError:
        
        #Display the error in the python shell
        print()
        print('Type Error! Please Check and Enter a Valid Date and Try Again')
        print()

        #Display the error in a message box
        import ctypes   
        ctypes.windll.user32.MessageBoxW(0, 'Type Error! Please Check and Enter a Valid Date and Try Again', 'ERROR!', 1)    


    except UnboundLocalError:
        
        #Display the error in the python shell
        print()
        print('Unbound Local Error! Please Check and Enter a Valid Date and Try Again')
        print()

        #Display the error in a message box
        import ctypes   
        ctypes.windll.user32.MessageBoxW(0, 'Unbound Local Error! Please Check and Enter a Valid Date and Try Again', 'ERROR!', 1)


    except:

        #To catch unexpected errors or hiddden programming mistakes
        
        #Display the error in the python shell
        print()
        print('Error! Please Check and Enter a Valid Date and Try Again')
        print()

        #Display the error in a message box
        import ctypes   
        ctypes.windll.user32.MessageBoxW(0, 'Error! Please Check and Enter a Valid Date and Try Again', 'ERROR!', 1)



#Predict results for room availability

def predict2():

    tot_rooms = 48
    
    
    month = combo1.get()
    #print(month)

    day = combo2.get()
    #print(day)


    #Checking if the entered date is valid or not

    
    #Checking for any run time exceptions and if any then exception handling

    try:

        #if invalid
        
        if((day == '30' and month == 'February') or
           (day == '31' and (month == 'February' or month == 'April' or month == 'June' or month == 'September' or month == 'November')) or
           (int(day) > 31) or
           (month != 'January' and month != 'February' and month != 'March' and month != 'April' and month != 'May' and month != 'June' and month != 'July' and
            month != 'August' and month != 'September' and month != 'October' and month != 'November' and month != 'December')):

                #Display the error in the python shell
                print()
                print('Invalid Date! Please Check and Enter a Valid Date and Try Again')
                print()

                #Display the error in a message box
                import ctypes   
                ctypes.windll.user32.MessageBoxW(0, 'Invalid Date! Please Check and Enter a Valid Date and Try Again', 'ERROR!', 1)


        #if valid
            
        else:
            
            #Getting the first 3 letters of month names
            month = month[:3]


            #Converting date to correct format
            
            day_no = str(day) + '-' + month
            #print(day_no)


            #Converting month and date into integer values
            
            month_name = day_no[-3:]
            #print(month_name)

            
            date_month_without_white_space = ''.join(day_no.split())
            #print(date_month_without_white_space)
            
            date_month_without_last_four_characters = date_month_without_white_space[:-4]
            #print(date_month_without_last_four_characters)
            
            date_number = int(date_month_without_last_four_characters)
            #print(date_number)


            if(month_name == 'Jan'):
                date_index = date_number
                
            elif(month_name == 'Feb'):
                date_index = date_number + 31
                
            elif(month_name == 'Mar'):
                date_index = date_number + 59
                
            elif(month_name == 'Apr'):
                date_index = date_number + 90
                
            elif(month_name == 'May'):
                date_index = date_number + 120
                
            elif(month_name == 'Jun'):
                date_index = date_number + 151
                
            elif(month_name == 'Jul'):
                date_index = date_number + 181
                
            elif(month_name == 'Aug'):
                date_index = date_number + 212
                
            elif(month_name == 'Sep'):
                date_index = date_number + 243
                
            elif(month_name == 'Oct'):
                date_index = date_number + 273
                
            elif(month_name == 'Nov'):
                date_index = date_number + 304
                
            elif(month_name == 'Dec'):
                date_index = date_number + 334

            else:
                print('Invalid Month Name')

                
            #print(date_index)


            #Predicting results
            result = classifier.predict([[date_index]])
            #print(result)


            #Finding the room avaiability
            result = tot_rooms - result;
            #print(result)
    
            
            #Rounding to the nearest integer
            result = np.round(result)
            #print(result)


            #Formatting the result
            
            result = str(result)
            #print(result)

            result_without_white_space = ''.join(result.split())
            #print(result_without_white_space)
            
            result_without_last_two_characters = result_without_white_space[:-2]
            #print(result_without_last_two_characters)

            result_without_first_character = result_without_last_two_characters[1:]
            #print(result_without_first_character)

            result = result_without_first_character

            
            #Printing the result in the label
            label_predict.config(text = result)


    #Handling if any exception occurs   
        
    except ValueError:
        
        #Display the error in the python shell
        print()
        print('Value Error! Please Check and Enter a Valid Date and Try Again')
        print()

        #Display the error in a message box
        import ctypes   
        ctypes.windll.user32.MessageBoxW(0, 'Value Error! Please Check and Enter a Valid Date and Try Again', 'ERROR!', 1)

                    
    except TypeError:
        
        #Display the error in the python shell
        print()
        print('Type Error! Please Check and Enter a Valid Date and Try Again')
        print()

        #Display the error in a message box
        import ctypes   
        ctypes.windll.user32.MessageBoxW(0, 'Type Error! Please Check and Enter a Valid Date and Try Again', 'ERROR!', 1)    


    except UnboundLocalError:
        
        #Display the error in the python shell
        print()
        print('Unbound Local Error! Please Check and Enter a Valid Date and Try Again')
        print()

        #Display the error in a message box
        import ctypes   
        ctypes.windll.user32.MessageBoxW(0, 'Unbound Local Error! Please Check and Enter a Valid Date and Try Again', 'ERROR!', 1)


    except:

        #To catch unexpected errors or hiddden programming mistakes
        
        #Display the error in the python shell
        print()
        print('Error! Please Check and Enter a Valid Date and Try Again')
        print()

        #Display the error in a message box
        import ctypes   
        ctypes.windll.user32.MessageBoxW(0, 'Error! Please Check and Enter a Valid Date and Try Again', 'ERROR!', 1)

        

#Converting to numpy arrays

import numpy as np

data = np.array(data)
target = np.array(target)

##print('\n Data : ', data)
##print('\n Targets : ', target)
##
##print('\nNumber of Data : ', len(data))
##print('Number of Targets : ', len(target))



#Converting month and date into integer values

cnt = 0
length = len(data)

day_index = [0 for x in range(length)]


for date_month in data:
    
    #print(date_month)

    month_name = date_month[-3:]
    #print(month_name)

    
    date_month_without_white_space = ''.join(date_month.split())
    #print(date_month_without_white_space)
    
    date_month_without_last_four_characters = date_month_without_white_space[:-4]
    #print(date_month_without_last_four_characters)
    
    date_number = int(date_month_without_last_four_characters)
    #print(date_number)


    if(month_name == 'Jan'):
        date_index = date_number
        
    elif(month_name == 'Feb'):
        date_index = date_number + 31
        
    elif(month_name == 'Mar'):
        date_index = date_number + 59
        
    elif(month_name == 'Apr'):
        date_index = date_number + 90
        
    elif(month_name == 'May'):
        date_index = date_number + 120
        
    elif(month_name == 'Jun'):
        date_index = date_number + 151
        
    elif(month_name == 'Jul'):
        date_index = date_number + 181
        
    elif(month_name == 'Aug'):
        date_index = date_number + 212
        
    elif(month_name == 'Sep'):
        date_index = date_number + 243
        
    elif(month_name == 'Oct'):
        date_index = date_number + 273
        
    elif(month_name == 'Nov'):
        date_index = date_number + 304
        
    elif(month_name == 'Dec'):
        date_index = date_number + 334

    else:
        print('Invalid Month Name')

        
    #print(date_index)
    

    day_index[cnt] = date_index


    cnt = cnt + 1
    #print(count)


#print(count)
#print(day_index)    



#Train Data & Train Targets & Converting to numpy Arrays

#import numpy as np

train_data = [0 for x in range(length)]
train_target = [0 for x in range(length)]

train_data = np.array(day_index)
train_target = np.array(target)

##print('\nTrain Data : ', train_data)
##print('\nTrain Targets : ', train_target)
##
##print('\nNumber of Training Data : ', len(train_data))
##print('Number of Train Targets : ', len(train_target))


train_data = np.array(train_data.reshape(-1, 1))
train_target = np.array(train_target)

##print('\nTrain Data : ', train_data)
##print('\nTrain Targets : ', train_target)
##
##print('\nNumber of Train Data : ', len(train_data))
##print('Number of Train Targets : ', len(train_target))



#Machine Learning Algorithm

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

#from scipy.optimize import curve_fit

classifier = LinearRegression()
classifier.fit(train_data, train_target)

m = classifier.coef_[0]
#coefficient / gradient(m)

c = classifier.intercept_
#intercept(c)

x = np.arange(0, 366, 4)

y = m * x + c



#Plotting the line graph (best fit line) for reserved rooms

def button3_pressed():

    from matplotlib import pyplot as plt

    #Plotting the actual data
    plt.scatter(train_data, train_target, label = 'Room Count')

    #Plotting the best fit line
    plt.plot(x, y, 'r', label = 'Best Fit Line')

    plt.legend()
    plt.title('Reserved Rooms with Best Fit Line Graph')
    plt.savefig('Reserved Rooms with Best Fit Line Graph.png')
    plt.show()



#Plotting the line graph (best fit line) for available rooms

def button4_pressed():

    from matplotlib import pyplot as plt

    total_rooms = 48

    #Plotting the actual data
    plt.scatter(train_data, total_rooms - train_target, label = 'Room Count')

    #Plotting the best fit line
    plt.plot(x, total_rooms - y, 'r', label = 'Best Fit Line')

    plt.legend()
    plt.title('Available Rooms with Best Fit Line Graph')
    plt.savefig('Available Rooms with Best Fit Line Graph.png')
    plt.show()



#GUI for the application

import tkinter as tk

window = tk.Tk()

font1 = 'Helvetica 15 bold'


button1 = tk.Button(window, text = 'Rooms Reserved Graph', bg = 'blue', fg = 'white', font = font1, command = button1_pressed)
button1.grid(row = 1, column = 0, pady = 20, padx = 20)

button2 = tk.Button(window, text = 'Room Availability Graph', bg = 'green', fg = 'white', font = font1, command = button2_pressed)
button2.grid(row = 2, column = 0, pady = 20, padx = 20)


button3 = tk.Button(window, text = 'Rooms Reserved Graph with Best Fit Line', bg = 'light blue', fg = 'white', font = font1, command = button3_pressed)
button3.grid(row = 3, column = 0, pady = 20, padx = 20)

button4 = tk.Button(window, text = 'Room Availability Graph with Best Fit Line', bg = 'light green', fg = 'white', font = font1, command = button4_pressed)
button4.grid(row = 4, column = 0, pady = 20, padx = 20)


label1 = tk.Label(window, text = 'DATE : ', bg = 'gray80', font = font1)
label1.grid(row = 2, column = 1, pady = 10, padx = 20)


from tkinter import ttk

#The tkinter.ttk module provides access to the Tk themed widget set

#from pprint import pprint
#The pprint module provides a capability to “pretty-print” arbitrary Python data structures in a form which can be used as input to the interpreter


combo1 = ttk.Combobox(window, values = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
#pprint(dict(combo1))

combo1.grid(row = 2, column = 2, pady = 10, padx = 20)
combo1.current(0)
#print(combo1.current(), combo1.get())


combo2 = ttk.Combobox(window, values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])
#pprint(dict(combo2))

combo2.grid(row = 2, column = 3, pady = 10, padx = 20)
combo2.current(0)
#print(combo2.current(), combo2.get())


button_predict = tk.Button(window, text = 'Predict Number of Reserved Rooms', bg = 'black', fg = 'white', font = font1, command = predict)
button_predict.grid(row = 3, column = 1, pady = 5, padx = 20, columnspan = 3)

button_predict2 = tk.Button(window, text = 'Predict Number of Available Rooms', bg = 'gray40', fg = 'white', font = font1, command = predict2)
button_predict2.grid(row = 4, column = 1, pady = 5, padx = 20, columnspan = 3)


label_predict = tk.Label(window, text = 'NONE', bg = 'gray80', font = font1)
label_predict.grid(row = 5, column = 1, pady = 10, padx = 20, columnspan = 3)


button_exit = tk.Button(window, text = 'Exit', bg = 'red', fg = 'white', font = font1, command = window.destroy)
button_exit.grid(row = 5, column = 0, pady = 20, padx = 20)

