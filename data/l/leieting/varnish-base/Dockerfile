FROM alpine:3.4  
MAINTAINER Thomas S. Nielsen <thomas@leieting.no>  
  
RUN apk update && \  
apk upgrade && \  
apk add varnish  
  
COPY start.sh /start.sh  
  
ENV VCL_CONFIG /etc/varnish/default.vcl  
ENV CACHE_SIZE 64m  
ENV VARNISHD_PARAMS -p default_ttl=3600 -p default_grace=3600  
  
CMD /start.sh  
EXPOSE 80  

