FROM python:3.4.6-slim  
  
WORKDIR /usr/src/app/  
COPY requirements.txt ./  
RUN pip install -r requirements.txt  
COPY src/ .  
COPY scripts/runserver.sh .  
RUN mkdir -p /var/nl  
  
EXPOSE 8000  
CMD ["/bin/sh", "runserver.sh"]  

