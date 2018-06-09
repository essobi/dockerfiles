FROM jsurf/rpi-raspbian:latest  
RUN [ "cross-build-start" ]  
RUN mkdir -p /temperature-mqtt  
COPY temperature-mqtt /temperature-mqtt  
RUN apt-get update && apt-get install -y \  
mosquitto \  
mosquitto-clients \  
libusb-dev \  
libusb-1.0-0-dev && apt-get clean && rm -rf /var/lib/apt/lists/*  
  
WORKDIR /temperature-mqtt  
CMD [ "sh", "run.sh" ]  

