## Python module to read a pdf and convert the contents into json format.

import json
import PyPDF2
pdf_file = open("docs/IPL 2021 SCHEDULE.pdf", 'rb')

## Extract data
def get_data(page_content):
    _retDict = []
    _dict = []
    page_content_list = page_content.splitlines()
    for idx,line in enumerate(page_content_list):
        if( idx % 5 ) == 0:
            print(idx)
            _dict += line
        else:
            _retDict += _dict
            _retDict += ','
            _dict = ''
    return _retDict

read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(0)
page_content = page.extractText()

for page in read_pdf.pages:
    # page_data = get_data(page_content)
    # json_data = json.dumps(page_data, indent=4)
    print(get_data(page_content))
