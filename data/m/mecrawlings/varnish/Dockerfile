FROM alpine:latest  
  
ENV VARNISH_BACKEND_ADDRESS 127.0.0.1  
ENV VARNISH_MEMORY 100M  
ENV VARNISH_BACKEND_PORT 80  
EXPOSE 8080  
RUN apk update && \  
apk upgrade && \  
apk add varnish  
  
COPY varnish.sh /varnish.sh  
  
RUN chown root:root /varnish.sh && chmod o+x /varnish.sh  
  
CMD ["/varnish.sh"]  

