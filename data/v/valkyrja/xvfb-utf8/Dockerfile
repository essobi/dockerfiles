FROM valkyrja/debian-jessie-utf8  
  
MAINTAINER Valkyrja <valkyrjasama@gmail.com>  
  
RUN apt-get update && apt-get install -y xvfb && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
ENV DISPLAY :99  
RUN Xvfb $DISPLAY -ac -screen 0 1280x1024x8 &

