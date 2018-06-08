FROM python:2.7-alpine  
  
RUN pip install b2  
  
RUN adduser -S -s /bin/false -u 1000 -D b2  
USER b2  
  
ENTRYPOINT [ "b2" ]  

