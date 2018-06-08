FROM python:3.6  
WORKDIR /usr/src/app  
  
COPY requirements.txt ./  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY bridge.py ./  
COPY Reader.py ./  
COPY list_devices.py ./  
  
CMD [ "python", "-u", "./bridge.py" ]  

