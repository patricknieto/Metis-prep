

#Q5. Write email addresses from Part I to csv file

with open('emails.csv', 'w') as fp:
    for email in data.email.values:
        fp.write('%s\n' % email)

