FROM forumi0721/alpine-armhf-base:latest  
  
MAINTAINER janwer <mail@janwerner.de>  
  
COPY local/. /usr/local/  
  
RUN ["docker-build-start"]  
  
RUN ["docker-init"]  
  
RUN ["docker-build-end"]  
  
ENTRYPOINT ["docker-run"]  
  
EXPOSE 4000/tcp  
  

