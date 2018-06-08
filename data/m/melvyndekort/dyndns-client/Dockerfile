FROM python:alpine  
  
RUN pip install --no-cache-dir schedule  
  
COPY job.py /  
  
CMD ["python", "-u", "/job.py"]  

