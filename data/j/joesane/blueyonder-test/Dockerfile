FROM continuumio/anaconda3  
  
RUN mkdir /app  
WORKDIR /app  
  
COPY bin bin  
COPY conf conf  
COPY static static  
COPY logs logs  
COPY requirements.txt ./  
  
RUN pip install -r requirements.txt  
  
CMD python bin/main.py

