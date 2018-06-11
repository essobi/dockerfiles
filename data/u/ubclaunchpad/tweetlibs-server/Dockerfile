FROM continuumio/miniconda3  
  
ADD server/requirements.txt /env/requirements.txt  
RUN pip install -r /env/requirements.txt  
  
RUN python -m textblob.download_corpora  
ADD server /app  
WORKDIR /app  
  
ENTRYPOINT ["python3", "app.py"]  

