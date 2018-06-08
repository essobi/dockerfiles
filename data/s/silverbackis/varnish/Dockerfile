FROM alpine  
  
ENV VARNISH_PORT 80  
ENV VARNISH_HOST nginx  
ENV VARNISH_BACKEND_PORT 80  
ENV VARNISH_BAN_CONTAINER api  
ENV ACCEPT_COOKIES zzz  
  
RUN apk add --no-cache varnish  
  
COPY default.vcl /etc/varnish/default.vcl  
COPY start.sh /usr/local/bin/start  
RUN chmod +x /usr/local/bin/start  
  
EXPOSE ${VARNISH_PORT}  
VOLUME ["/var/lib/varnish", "/etc/varnish"]  
  
CMD ["start"]  

