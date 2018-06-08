FROM alpine  
MAINTAINER gowness "biga05@gmail.com"  
ADD bootstrap.sh /tmp/  
RUN chmod +x /tmp/bootstrap.sh && sleep 1 && /tmp/bootstrap.sh  
  
RUN adduser -D znc  
ADD start-znc /usr/local/bin/  
ADD znc.conf.default /src/  
RUN chmod 644 /src/znc.conf.default  
  
EXPOSE 6667  
ENTRYPOINT ["/usr/local/bin/start-znc"]  
CMD [""]  

