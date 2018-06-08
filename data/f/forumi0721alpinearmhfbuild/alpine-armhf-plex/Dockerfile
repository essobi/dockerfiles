FROM forumi0721alpinearmhf/alpine-armhf-glibc:latest  
  
MAINTAINER stonecold <forumi0721@gmail.com>  
  
COPY local/. /usr/local/  
  
RUN ["docker-build-start"]  
  
RUN ["docker-init"]  
  
RUN ["docker-build-end"]  
  
ENTRYPOINT ["docker-run"]  
  
EXPOSE 32400/tcp 3005/tcp 8324/tcp 32469/tcp 1900/udp 32410/udp 32412/udp
32413/udp 32414/udp  
  

