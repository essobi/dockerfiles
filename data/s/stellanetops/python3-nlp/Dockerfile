FROM python:3.5.3  
RUN apt-get update -y  
RUN apt-get install -y build-essential  
  
COPY requirements.txt .  
RUN pip install -r requirements.txt  
RUN python -m spacy download en  

