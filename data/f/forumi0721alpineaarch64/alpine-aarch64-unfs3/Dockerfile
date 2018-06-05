FROM forumi0721/alpine-aarch64-base:latest  
  
MAINTAINER stonecold <forumi0721@gmail.com>  
  
COPY local/. /usr/local/  
  
RUN ["docker-build-start"]  
  
RUN ["docker-init"]  
  
RUN ["docker-build-end"]  
  
ENTRYPOINT ["docker-run"]  
  
EXPOSE 111/tcp 111/udp 2049/tcp 2049/udp  
  

