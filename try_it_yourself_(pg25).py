#Try It Yourself Tasks (pg25)
#2-3
name = "harry potter"
title = "the boy who lived"
message = f'{name.title()} is known as "{title.title()}".'
print(message)

#2-4
print(name.upper())
print(name.lower())
print(name.title())

#2-5
name_2 = "hagrid"
phrase = "you're a wizard Harry"
message_2 = f'{name_2.title()} once told a boy, "{phrase}."'
print(message_2)

#2-6 (skipped)

#2-7
name_3 = "' harry potter '"
print(name_3.lstrip())
print(name.rstrip())
print(name.strip())

#2-8
filename = "python_notes.txt"
simple_filename = filename.removesuffix(".txt")
print(simple_filename)