FROM ubuntu:17.10  
MAINTAINER Herbert Shin  
  
# dependencies  
RUN apt-get update && \  
apt-get build-dep -y ffmpeg && \  
apt-get install -y ffmpeg  
  
WORKDIR /downloads  
  
ENTRYPOINT ["/usr/bin/ffmpeg"]  
CMD ["-h"]  
# b90dd9cf7d653d05aea7625cd03e05f4 -  

