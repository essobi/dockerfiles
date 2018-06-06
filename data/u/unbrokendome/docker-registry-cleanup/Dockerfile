FROM python:3.5.1-alpine  
  
RUN mkdir -p /usr/src/app  
  
COPY requirements.txt /usr/src/app  
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt  
  
COPY src /usr/src/app  
  
EXPOSE 5000  
WORKDIR /usr/src/app  
CMD [ "python", "-m", "registry_cleanup.main" ]  

