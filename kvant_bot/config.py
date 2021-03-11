import os

token = "1411084539:AAEQa6SoEGPtrvwC_Kp_1g-PK2MLLxr1_y8"
feed = 'http://kvantorium.iroso.ru/feed'

joinedFile = open('joined.txt', 'r')
joinedUsers = set()
for line in joinedFile:
	joinedUsers.add(line.strip())
joinedFile.close()
