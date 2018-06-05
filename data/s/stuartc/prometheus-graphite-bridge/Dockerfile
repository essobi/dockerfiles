FROM python:3-alpine  
  
WORKDIR /usr/src/app  
  
COPY requirements.txt ./  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY prometheus-graphite-bridge.py .  
  
ENTRYPOINT [ "python", "./prometheus-graphite-bridge.py" ]  
CMD [ "--help" ]  

