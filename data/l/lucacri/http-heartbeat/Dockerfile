FROM lucacri/alpine-base:latest  
MAINTAINER "Luca Critelli" <lucacri@gmail.com>  
  
  
RUN apk --no-cache add \  
curl \  
nano \  
bzip2 \  
bash  
  
ADD rootfs /  
  
EXPOSE 3128  
ENV NOTIFY_URL "http://urlhere"  
ENV NOTIFY_EVERY_SECONDS 20

