FROM python:3.6-alpine  
  
COPY ./* /app/  
  
RUN pip install requests && \  
chmod -R 755 /app  
  
WORKDIR /app  
  
CMD ["/bin/sh", "run.sh"]  

