#you will generate a syntax error if single and double quotes are not carefully utulized
message = "It's a wonderful day today"
print (message)

#single quotes can be used within double quotes without a problem. However, you cannot simply use single quotes to create a string and still have apostrophes or single quotes within that same value
message = 'It's a wonderful day today'
print (message)
# the computer now thinks that the string ends after the apostrophe rather than after the word today. Keeping strings defined with double quotes rather than single keeps things simple when coding
