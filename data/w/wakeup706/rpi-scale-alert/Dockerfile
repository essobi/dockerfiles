FROM wakeup706/rpi-python-mqtt  
  
ADD intrusion-alert.py /data  
  
ENV BROKER=192.168.0.99  
ENV TOPIC=iot-1/d/#  
WORKDIR /data  
CMD [ "python", "intrusion-alert.py" ]  

