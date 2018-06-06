FROM ubuntu:16.04  
MAINTAINER Mike Chernev <mike@mikechernev.com>  
  
RUN apt-get update && apt-get install -y timidity ffmpeg  
ADD convert /usr/bin  
  
CMD ["convert"]  
  

