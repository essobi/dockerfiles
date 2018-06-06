FROM ubuntu:14.04  
MAINTAINER CREATIVE AREA  
  
ENV DEBIAN_FRONTEND noninteractive  
  
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
#ENV VARNISH_STORAGE file,$VARNISH_STORAGE_FILE,1G  
ENV VARNISH_STORAGE malloc,100M  
ENV VARNISH_TTL 120  
ENV VARNISH_NCSA_LOGFORMAT "%h %l %u %t %D \"%r\" %s %b %{Varnish:hitmiss}x
\"%{User-agent}i\""  
RUN apt-get -qq update && apt-get install -y curl apt-transport-https
supervisor  
  
RUN \  
curl -sL https://repo.varnish-cache.org/GPG-key.txt | apt-key add - && \  
echo "deb https://repo.varnish-cache.org/ubuntu/ trusty varnish-4.1" >>
/etc/apt/sources.list.d/varnish-cache.list && \  
apt-get -qq update && \  
apt-get install -y varnish  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY default.vcl $VARNISH_VCL_CONF  
  
COPY setup.sh /setup.sh  
COPY start.sh /start.sh  
RUN chmod 0755 /start.sh /setup.sh  
  
VOLUME $VARNISH_STORAGE_PATH  
  
EXPOSE $VARNISH_LISTEN_PORT $VARNISH_ADMIN_LISTEN_PORT  
  
CMD ["/start.sh"]  

