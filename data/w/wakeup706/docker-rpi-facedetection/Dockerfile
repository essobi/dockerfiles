FROM jsurf/rpi-raspbian:latest  
RUN [ "cross-build-start" ]  
RUN mkdir -p /faceDetection  
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
COPY faceDetection /faceDetection  
COPY lib /lib  
WORKDIR /faceDetection  
CMD [ "sh", "faceDetection.sh" ]  

