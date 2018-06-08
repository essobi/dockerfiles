FROM python:3.5.2  
RUN mkdir -p /app/log/  
ADD requirements.txt /app/  
WORKDIR /app/  
RUN pip install -r requirements.txt  
  
ADD worker.py /app/  
  
EXPOSE 8080  
CMD ["python", "worker.py"]

