FROM jsurf/rpi-raspbian:latest  
RUN [ "cross-build-start" ]  
RUN mkdir -p /detection_and_mqtt  
RUN mkdir -p /lib  
RUN apt-get update && apt-get install -y \  
libjpeg62 \  
libtiff5 \  
libjasper1 \  
libilmbase6 \  
libopenexr6 \  
libgtk2.0-0 \  
libdc1394-22 \  
libv4l-0 \  
mosquitto \  
mosquitto-clients && apt-get clean && rm -rf /var/lib/apt/lists/*  
COPY detection_and_mqtt /detection_and_mqtt  
COPY lib /lib  
WORKDIR /detection_and_mqtt  
CMD [ "sh", "faceDetection_and_mqtt.sh" ]  

