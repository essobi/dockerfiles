FROM java:7-alpine  
MAINTAINER Manuel (https://github.com/TeNNoX/)  
  
ENV REVISION "latest"  
# Install openssl and git  
RUN apk add --no-cache openssl git bash  
  
# Add script  
COPY build.sh /root/build.sh  
RUN chmod +x /root/build.sh  
  
RUN mkdir /build  
VOLUME /build  
WORKDIR /build  
  
CMD ["bash", "/root/build.sh"]  

