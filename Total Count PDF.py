#!/usr/bin/env python
# coding: utf-8

# In[1]:


import PyPDF2

def getTotalWordCount(pdf_file):
    
    # Function to get the total word count of a pdf by looping through each page
    
    totalcount = 0
    
    #open the PDF file in read
    pdfFileObj = open(pdf_file, 'rb')
    
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


# In[ ]:




