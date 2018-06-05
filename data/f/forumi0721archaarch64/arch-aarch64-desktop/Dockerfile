FROM forumi0721archaarch64/arch-aarch64-dev:latest  
  
MAINTAINER stonecold <forumi0721@gmail.com>  
  
COPY local/. /usr/local/  
  
RUN ["docker-build-start"]  
  
RUN ["docker-init"]  
  
RUN ["docker-build-end"]  
  
ENTRYPOINT ["docker-run"]  
  
EXPOSE 5900/tcp  
  

