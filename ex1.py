from sys import argv

script, filename , from_file  = argv

user_name = raw_input("Please enter your name: ")

print "Welcome %s " % user_name

print " This program will add whatever you write in to the txt document %s." % filename
print "If you do not want to proceed please hit CTRL-C on your keyboard "

document1 = raw_input("Please enter line 1: ")
document2 = raw_input("Please enter line 2: ")
document3 = raw_input("Please enter line 3: ")

fulldocument = document1 ,document2 ,document3

print "Processing text........"

user_document.write(document1)
user_document.write("\n")
user_document.write(document2)
user_document.write("\n")
user_document.write(document3)
user_document.write("\n")
user_document.write("created by Calvin")

print "Working....... "

print "copy from %s " %from_file

print "Hit return to continue"

raw_input()


copyfile = open(from_file, "r")
filecontent = copyfile.read()

user_document.write(filecontent)

print "Write operation successful"

print "Please review the file"

document_review = raw_input("If you like to erase the document write yes or no: ")
if document_review == "yes":
    open(filename, "w")
    user_document.truncate()
    print "document erase"

user_document.close()
