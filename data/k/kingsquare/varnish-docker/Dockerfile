FROM alpine:3.3  
MAINTAINER Kingsquare <docker@kingsquare.nl>  
  
ENV VARNISH_VCL_CONF /etc/varnish/default.vcl  
ENV VARNISH_LISTEN_ADDRESS 0.0.0.0  
ENV VARNISH_LISTEN_PORT 80  
ENV VARNISH_ADMIN_LISTEN_ADDRESS 0.0.0.0  
ENV VARNISH_ADMIN_LISTEN_PORT 6082  
ENV VARNISH_MIN_THREADS 1  
ENV VARNISH_MAX_THREADS 1000  
ENV VARNISH_THREAD_TIMEOUT 120  
ENV VARNISH_SECRET_FILE /etc/varnish/secret  
ENV VARNISH_STORAGE_PATH /varnish_storage  
ENV VARNISH_STORAGE_FILE $VARNISH_STORAGE_PATH/varnish_storage.bin  
ENV VARNISH_STORAGE_SIZE 100M  
#ENV VARNISH_STORAGE file,$VARNISH_STORAGE_FILE,$VARNISH_STORAGE_SIZE  
ENV VARNISH_STORAGE malloc,$VARNISH_STORAGE_SIZE  
ENV VARNISH_TTL 120  
ENV VARNISH_NCSA_LOGFORMAT "%h %l %u %t %D \"%r\" %s %b %{Varnish:hitmiss}x
\"%{User-agent}i\""  
RUN apk --no-cache add supervisor bash varnish  
  
COPY supervisord.conf /etc/supervisor.d/supervisord.ini  
COPY default.vcl $VARNISH_VCL_CONF  
  
COPY setup.sh /setup.sh  
COPY start.sh /start.sh  
RUN chmod 0755 /start.sh /setup.sh  
  
EXPOSE $VARNISH_LISTEN_PORT $VARNISH_ADMIN_LISTEN_PORT  
  
CMD ["/start.sh"]  

