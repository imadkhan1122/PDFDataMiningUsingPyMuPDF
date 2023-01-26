#------------------------import important packages-----------------------------#
import pdfplumber
import os
import fitz
import json
#------------------------CLASS PDF PARSER-----------------------------#

class PDF_PARSER:
    def __init__(self, pth):
        self.path = pth
        self.main()
    #------------------------LOADING FILES-----------------------------#
    def load_pdfs(self, path):
        return os.listdir(path)
        
    #------------------------GET PDF BASIC INFO------------------------#
    def GET_TEXT(self, path = 'PDFs/The Glorious Quran Word-to-Word Translation by Shehnaz Shaikh Kausar Khatri (z-lib.org).pdf'): 
        # Read pdf into list of DataFrame
        PDF =  pdfplumber.open(path)
        doc = fitz.open(path)
        PAGES = PDF.pages
        
        Text = doc[11].get_text()
        
        
        
        
        
        
        
    def Text_Cleaning(self, path):
                    
        return 
    
    def main(self):
        path = self.path
        dic = self.Text_Cleaning(path)
        with open('Result.json', 'w') as out:
            json.dump(dic , out,  indent=2)
            
        return print('Parsing Completed')
