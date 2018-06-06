FROM jsurf/rpi-raspbian:latest  
RUN [ "cross-build-start" ]  
RUN mkdir -p /capture_and_server  
RUN mkdir -p /lib  
RUN apt-get update && apt-get install -y \  
libjpeg62 \  
libtiff5 \  
libjasper1 \  
libilmbase6 \  
libopenexr6 \  
libgtk2.0-0 \  
libdc1394-22 \  
libv4l-0 && apt-get clean && rm -rf /var/lib/apt/lists/*  
COPY capture_and_server /capture_and_server  
COPY lib /lib  
WORKDIR /capture_and_server  
CMD [ "sh", "capture_and_server.sh" ]  

