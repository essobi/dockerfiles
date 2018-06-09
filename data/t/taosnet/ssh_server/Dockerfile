FROM alpine  
MAINTAINER Chris Batis <clbatis@taosnet.com>  
  
RUN apk --no-cache add dropbear dropbear-scp  
EXPOSE 22  
ENTRYPOINT /docker-dropbear.sh  
COPY docker-dropbear.sh /docker-dropbear.sh  
COPY setupUser.sh /usr/sbin/setupUser.sh  

