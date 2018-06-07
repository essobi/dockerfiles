FROM python:3.3  
MAINTAINER Research Data Service at Illinois databank@library.illinois.edu  
  
WORKDIR /usr/src/app  
  
ADD https://raw.githubusercontent.com/medusa-project/databank-
client/master/illinois_data_bank_datafile.py ./  
  
RUN pip install --no-cache-dir docopt requests urllib3[secure]  
  
CMD ["echo", "This image supports uploading a file to a draft dataset in
Illinois Data Bank, a public access repository for publishing research data
from the University of Illinois at Urbana-Champaign. For more information, see
https://databank.illinois.edu/help#api or contact the Research Data Service at
databank@library.illinois.edu."]  

