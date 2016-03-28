

#Q5. Write email addresses from Part I to csv file

with open('emails.csv', 'w') as f:
    for email in data.email.values:
        f.write('%s\n' % email)

