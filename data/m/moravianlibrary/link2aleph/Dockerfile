FROM python:2.7  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
RUN pip install --no-cache-dir Flask Flask-AutoIndex  
ADD link2aleph-service.py /usr/src/app  
  
CMD [ "python", "./link2aleph-service.py" ]  

