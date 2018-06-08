FROM python:2.7  
MAINTAINER dan.leehr@duke.edu  
  
ADD src /src  
WORKDIR /src  
  
RUN pip install -r /src/requirements.txt  
  
RUN chmod +x /src/overrepresented_sequence_extract.py  
ENV PATH /src/:$PATH  

