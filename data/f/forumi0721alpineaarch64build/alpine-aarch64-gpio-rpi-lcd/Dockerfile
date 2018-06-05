FROM forumi0721alpineaarch64build/alpine-aarch64-gpio-rpi:latest  
  
MAINTAINER stonecold <forumi0721@gmail.com>  
  
COPY local/. /usr/local/  
  
RUN ["docker-build-start"]  
  
RUN ["docker-init"]  
  
RUN ["docker-build-end"]  
  
ENTRYPOINT ["docker-run"]  
  

