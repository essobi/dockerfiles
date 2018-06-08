FROM python:alpine  
  
RUN pip install --no-cache-dir --upgrade setuptools flexget  
  
VOLUME ["/root/.flexget"]  
  
EXPOSE 5050  
CMD ["flexget", "daemon", "start", "--autoreload-config"]  

