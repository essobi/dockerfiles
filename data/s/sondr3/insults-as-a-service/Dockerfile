FROM python:stretch  
  
WORKDIR /usr/src/insults  
  
COPY requirements.txt ./  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY . .  
  
EXPOSE 5432  
RUN python -m spacy download en  
CMD python insults.py  

