FROM alpine:latest  
  
RUN apk update && \  
apk add --no-cache murmur qt-mysql netcat-openbsd wget bash  
RUN wget --no-check-certificate -O /usr/bin/dumb-init
https://github.com/Yelp/dumb-init/releases/download/v1.0.1/dumb-
init_1.0.1_amd64  
  
COPY murmur.conf /etc/murmur.conf  
COPY init.sh /usr/bin/init.sh  
  
RUN chmod +x /usr/bin/dumb-init && \  
chmod +r /etc/murmur.conf  
  
VOLUME ["/data"]  
EXPOSE 64738 64738/udp  
  
CMD ["/usr/bin/dumb-init","/usr/bin/init.sh"]  

