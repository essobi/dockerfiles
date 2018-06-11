FROM jsurf/rpi-raspbian:latest  
RUN [ "cross-build-start" ]  
RUN apt-get update && apt-get install -y \  
libjpeg62 \  
libtiff4 \  
libjasper1 \  
libilmbase6 \  
libopenexr6 \  
libgtk2.0-0 \  
libdc1394-22 \  
libv4l-0 && apt-get clean && rm -rf /var/lib/apt/lists/*  
COPY lib /lib  
CMD ["/bin/bash"]  

