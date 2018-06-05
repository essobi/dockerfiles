FROM alpine  
MAINTAINER Ciel <me@ciel.im>  
  
RUN apk --update add \  
bash aria2  
  
VOLUME /data  
EXPOSE 6800  
COPY run.sh /run.sh  
CMD ["bash", "/run.sh"]  

