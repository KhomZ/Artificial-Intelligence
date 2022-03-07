import csv
#import the pandas library
import pandas as pd

# #read a data with the Purchase Address column having commas
# # pd.read_csv('sample data.csv', quotechar='"').head()

# # file1 =pd.read_csv(r'C:\Users\ACER\Desktop\Artificial Intelligence\Lab1\AI\csvChallenge\file.csv')
# # file2 = pd.read_csv(r'C:\Users\ACER\Desktop\Artificial Intelligence\Lab1\AI\csvChallenge\file.csv')
# file1 = open(r'C:\Users\ACER\Desktop\Artificial Intelligence\Lab1\AI\csvChallenge\file.csv')
# file2 = open(r'C:\Users\ACER\Desktop\Artificial Intelligence\Lab1\AI\csvChallenge\file.csv')

# # file1 = open(file.csv, 'rb')
# # file2 = open(file.csv, 'wb')
# reader = csv.reader(file1)
# writer = csv.writer(file2)
# for row in reader:
#    if row[2] == 'Test':
#       writer.writerow( row[0], row[1], '123')




# Do the reading
file1 = open(r'C:\Users\ACER\Desktop\Artificial Intelligence\Lab1\AI\csvChallenge\file.csv', 'r+')
reader = csv.reader(file1)
new_rows_list = []
for row in reader:
   if row[2] == 'Test':
      new_row = [row[0], row[1], 'Somevalue']
      new_rows_list.append(new_row)
file1.close()   # <---IMPORTANT

# Do the writing
file2 = open(r'C:\Users\ACER\Desktop\Artificial Intelligence\Lab1\AI\csvChallenge\file.csv', 'w+')
writer = csv.writer(file2)
writer.writerows(new_rows_list)
file2.close()