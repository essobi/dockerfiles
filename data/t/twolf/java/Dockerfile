FROM twolf/alpine2:latest  
MAINTAINER Thomas Boerger <thomas@webhippie.de>  
  
RUN apk add --update \  
nss \  
openjdk7 && \  
rm -rf /var/cache/apk/*  
  
ADD rootfs /  
  
RUN mkdir /app  
WORKDIR /app  
CMD ["bash"]  

