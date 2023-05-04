#!/bin/bash

# Create a new user account named "johndoe" with a password "password123"
sudo useradd johndoe -m -p password123

# Assign the user account "johndoe" to the group "developers"
sudo usermod -a -G developers johndoe

# Verify that the user account "johndoe" has been created and is a member of the group "developers"
id johndoe
groups johndoe

# Change the permissions of a file named "file.txt" to allow the owner to read, write, and execute, and allow the group and other users to only read
sudo chmod 744 file.txt

# Create a folder name “backup” and copy a file named "file1.txt" to a directory named "backup"
mkdir backup
cp file1.txt backup/

#งานนี้ได้รับจาก chatgpt เนื่องจากไม่เคยเขียน linux ครับ TT
