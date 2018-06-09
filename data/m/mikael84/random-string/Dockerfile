FROM python:2.7.13-alpine  
  
RUN pip install web.py  
  
ADD webserver.py /  
  
EXPOSE 8080  
ENTRYPOINT python /webserver.py  

