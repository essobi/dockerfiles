FROM alpine  
MAINTAINER Ciel <me@ciel.im>  
  
RUN apk --update add \  
bash python py-pip && pip install shadowsocks  
  
EXPOSE 8388  
COPY run.sh /run.sh  
CMD ["bash", "/run.sh"]  

