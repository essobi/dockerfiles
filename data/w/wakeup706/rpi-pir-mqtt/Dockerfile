FROM wakeup706/rpi-python  
  
RUN mkdir -p /pir-mqtt  
COPY pir-mqtt /pir-mqtt  
RUN pip install gpiozero \  
paho-mqtt  
  
WORKDIR /pir-mqtt  
CMD [ "python", "pir_mqtt.py" ]  

