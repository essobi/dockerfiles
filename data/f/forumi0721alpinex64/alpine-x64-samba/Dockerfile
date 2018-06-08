FROM forumi0721/alpine-x64-base:latest  
  
MAINTAINER stonecold <forumi0721@gmail.com>  
  
COPY local/. /usr/local/  
  
#RUN ["docker-build-start"]  
RUN ["docker-init"]  
  
#RUN ["docker-build-end"]  
ENTRYPOINT ["docker-run"]  
  
EXPOSE 137/udp 138/udp 139/tcp 139/tcp 445/tcp  
  

