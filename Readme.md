# PDF INFORMATION PARSER:
    1.  In this project I have used pdfplumber and fitz for reading data page by page from PDF.
    2.  Using regex and string operations for data mining
    
### PROJECT FOLDER STRUTUE
    PDFDataMining
        > PDFs
        PARSER.py
        main.py
        Result.json
        Readme.md
        requirements.txt
        
    1. The main script is in the "PARSER.py" file.
    2. "main.py" will be used for running.
    3. "requirements.txt" is use for packages Installation.
    4. Output will be stored in "Result.json".
    
### PACKAGES INSTALLATION:
    1. cd to "PDFDataMining" directory and open cmd or terminal and type .
    "pip install -r requirements.txt" by doing this required packages will be installed.
    
### RUN THE SCRIPT:
    1. Open main.py in any text editor and change 'path' to your folder path where you placed pdf files or open main.ipynb file in jupyter notebook and change path and run.
    2. It will save all the results in Result.json file which will exists in PDFDataMining directory.