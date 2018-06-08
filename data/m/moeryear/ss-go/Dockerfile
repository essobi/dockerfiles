FROM golang:1.7.5-alpine3.5  
MAINTAINER sinnerliu  
  
RUN apk add --update && \  
apk add bash && \  
mkdir -p /ss  
  
ADD files/shadowsocks-server /ss/shadowsocks-server  
ADD files/config.json /ss/config.json  
ADD files/start.sh /ss/start.sh  
  
RUN chmod u+x /ss/start.sh && \  
chmod u+x /ss/shadowsocks-server  
  
EXPOSE 1024  
CMD ["/ss/start.sh"]  

