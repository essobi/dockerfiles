FROM python:2-slim  
  
COPY requirements.txt /usr/src/app/requirements.txt  
WORKDIR /usr/src/app  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY job.py .  
  
CMD ["./job.py"]  

