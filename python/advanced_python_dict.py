

#Part III - Dictionary


#Q6. Create a dictionary in the below format:

faculty_dict = {}
for index, row in data.iterrows():
    faculty_dict[row['name'].split()[-1]] = row.degree, row.title, row.email
faculty_dict

#Q7. The previous dictionary does not have the best design for keys. 
#Create a new dictionary with keys as:

faculty_dict = {}
for index, row in data.iterrows():
    faculty_dict[row['name'].split()[0], row['name'].split()[-1]] = row.degree, row.title, row.email
faculty_dict


#Q8. It looks like the current dictionary is printing by first name. 
#Sort by last name and print the first 3 key and value pairs.



faculty_dict = {}
for index, row in data.iterrows():
    faculty_dict[row['name'].split()[0], row['name'].split()[-1]] = row.degree, row.title, row.email

sorted(faculty_dict.items(), key=lambda key: key[0][1])

