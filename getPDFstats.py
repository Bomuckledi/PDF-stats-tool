#!/usr/bin/env python
# coding: utf-8



import PyPDF2
import glob
import csv

def getTotalWordCount(pdf_file):
    
    # Function to get the total word count of a pdf by looping through each page
    
    totalcount = 0
    
    #open the PDF file in read
    with open(pdf_file, 'rb') as pdfFileObj:

        #create a PdfFileReader object for PyPDF2 to work with
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        #start a for loop that will run over each page of the PDF
        for x in range(pdfReader.numPages - 1):

            #extract the text from each page
            text = pdfReader.getPage(x).extractText()
            # create a list containing each word on the page
            wordlist = text.split()
            #add the number of words on the page to the total count
            totalcount += len(wordlist)

        return totalcount


def getPageCount(pdf_file):
    
    with open(pdf_file, 'rb') as pdfFileObj:
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        pages = pdfReader.numPages
        return pages

#set up three lists to hold the data - file names (using glob to find all
# ... PDFs in directory, page count, word count
file_list = [f for f in glob.glob("*.pdf")]
pagecount_list = []
wordcount_list = []

#iterate over each file, obtain the page and word counts and append to lists
for n in file_list:
    pagecount_list.append(getPageCount(n))
    wordcount_list.append(getTotalWordCount(n))

# write lists to results CSV file
with open("results.csv", 'w', newline = "") as file:
    writer = csv.writer(file, dialect="excel")
    writer.writerow(file_list)
    writer.writerow(pagecount_list)
    writer.writerow(wordcount_list)


#end
