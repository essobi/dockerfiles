FROM alpine:latest  
  
EXPOSE 8118  
VOLUME /config  
  
RUN apk --update add privoxy tor runit  
  
RUN mkdir /etc/service/privoxy /etc/service/tor  
COPY runit/privoxy /etc/service/privoxy/run  
COPY patch/privoxy /etc/service/privoxy/patch  
COPY runit/tor /etc/service/tor/run  
COPY patch/tor /etc/service/tor/patch  
RUN chmod 755 /etc/service/privoxy/run /etc/service/tor/run  
  
CMD ["/sbin/runsvdir", "/etc/service"]  

