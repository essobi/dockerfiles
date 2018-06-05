FROM python:3  
WORKDIR /usr/src/app  
RUN pip install --no-cache-dir paho-mqtt PyYAML  
  
COPY app.py config.yml /usr/src/app/  
  
CMD [ "python", "./app.py" ]  

