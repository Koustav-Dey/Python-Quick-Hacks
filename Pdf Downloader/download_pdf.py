import urllib.request

url = input("Enter Pdf Url : ")
name = input("Enter Name of PDF : ")

pdf_name = name+".pdf"
urllib.request.urlretrieve(url,pdf_name)

#Save in Local Folder