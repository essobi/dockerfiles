# Based on resin/rpi-raspbian, added qemu for Crossbuild in Docker Hub  
FROM playgali/raspbian-qemu  
MAINTAINER Galileo Martinez "playgali@gmail.com"  
ENV REFRESHED_AT 2017-Aug-18  
RUN [ "cross-build-start" ]  
  
RUN apt-get update && apt-get install -y calibre && apt-get clean  
  
RUN [ "cross-build-end" ]  
  
VOLUME ["/calibre"]  
  
EXPOSE 8080  
ENTRYPOINT ["calibre-server"]  
CMD ["--with-library=/calibre"]  

