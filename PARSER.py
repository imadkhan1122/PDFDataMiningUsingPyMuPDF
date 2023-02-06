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
    def GET_TEXT(self, path): 
        # Read pdf into list of DataFrame
        PDF =  pdfplumber.open(path)
        doc = fitz.open(path)
        PAGES = PDF.pages
        All_Pages = []
        for p in range(len(PAGES)):
            partitioned_lst=[]
            try: 
                page = PAGES[p]
                Table = page.extract_words()
                
                procedure = [text['x0'] for text in Table if text['text'] == 'Procedures']
                procedure_value = []
                for text in Table:
                    if text['x0'] > procedure[0]-1 and text['x1'] < procedure[0]+30:
                        if text['text'] != []:
                            procedure_value.append(text['text'])
                    
                text = doc[p].get_text()   
                txt = text.split('\n')                
                try:
                    for e, p in enumerate(procedure_value):
                        partitioned_lst.append(txt[txt.index(procedure_value[e]):txt.index(procedure_value[e+1])])
                except:
                    partitioned_lst.append(txt[txt.index(procedure_value[e]):])
                
                All_Pages.append(partitioned_lst)
            except:
                pass
        return All_Pages
    
    def Text_Cleaning(self, path):
        TEXT = self.GET_TEXT(path)
        RAW = self.GET_TEXT(path)
        All_Pages = []
        for page in TEXT:
            page_partitions = []
            for part in page:
                del part[1]
                page_partitions.append(part)
            All_Pages.append(page_partitions)
        
        All_pages_row = []
        for page in All_Pages:
            ctxt = []
            for row in page:
                txt = []
                text = ''
                txt.append(row[0])
                for s in row[1:]:
                    if '.' in s or s.isalnum() == True and s.isdigit() == False:
                        text += ' '+s
                    elif s != '':
                        txt.append(s)
                txt.append(text)
                ctxt.append(txt)
            All_pages_row.append(ctxt)
        Dic = []
        for e, page in enumerate(All_pages_row):
            pages = []
            for rows in page:
                procedures = {}
                row = [s.replace('NDC: ', '') for s in rows if 'NDC' in s]
                if row != []:
                    procedure = rows[0]
                    num = [s for s in rows if s.isnumeric() == True and len(s) < 3]
                    Units = ''
                    try:
                        if num != []:
                            Units = num[0]
                        elif num == []:
                            for p in RAW:
                                for r in p:
                                    if r[0] == rows[0]:
                                        if r[1][-1].isnumeric() == True:
                                            Units = r[1][-1]
                    except:
                        pass
                    M1 = ''
                    M2 = ''
                    M3 = ''
                    M4 = ''
                    Diagnosis = rows[-1]
                    NDC = row[0]
                
                    procedures.update({'procedure':procedure, 'Units':Units, 
                                      'M1':M1, 'M2':M2, 'M3':M3, 'M4':M4, 
                                      'Diagnosis Code': Diagnosis, 'NDC': NDC})
                    
                elif row == []:
                    procedure = rows[0]
                    num = [s for s in rows if s.isnumeric() == True and len(s) < 3]
                    Units = ''
                    try:
                        if num != []:
                            Units = num[0]
                        elif num == []:
                            for p in RAW:
                                for r in p:
                                    if r[0] == rows[0]:
                                        if r[1][-1].isnumeric() == True:
                                            Units = r[1][-1]
                    except:
                        pass
                    M1 = ''
                    M2 = ''
                    M3 = ''
                    M4 = ''
                    Diagnosis = rows[-1]
                    
                    procedures.update({'procedure':procedure, 'Units':Units, 
                                      'M1':M1, 'M2':M2, 'M3':M3, 'M4':M4, 
                                      'Diagnosis Code': Diagnosis})
                pages.append(procedures)
            Dic.append({'procedures': pages})
            
        return Dic
    
    def main(self):
        path = self.path
        dic = self.Text_Cleaning(path)
        with open('Result.json', 'w') as out:
            json.dump(dic , out,  indent=2)
            
        return print('Parsing Completed')
