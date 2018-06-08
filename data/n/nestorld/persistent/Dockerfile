FROM nestorld/pytest:latest  
WORKDIR /app  
  
ADD . /app  
  
RUN pip install -r requirements.txt  
  
EXPOSE 8300  
CMD ["python", "persistent_test.py"]  

