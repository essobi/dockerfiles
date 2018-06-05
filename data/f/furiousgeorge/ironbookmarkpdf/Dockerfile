FROM furiousgeorge/ironbasechrome:latest  
  
WORKDIR /app  
ADD ./app/ /app  
RUN pip install --no-cache-dir -r requirements.txt  
  
ENTRYPOINT ["python", "worker.py"]  

