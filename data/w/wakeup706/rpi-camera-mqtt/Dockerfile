FROM wakeup706/rpi-python-opencv:with-mqtt  
  
ADD image-mqtt.py /data  
  
ENV BROKER=192.168.0.99  
ENV TOPIC=image  
  
WORKDIR /data  
CMD [ "python", "image-mqtt.py" ]  
  

