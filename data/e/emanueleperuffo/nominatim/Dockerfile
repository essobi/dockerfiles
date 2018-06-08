FROM emanueleperuffo/baseimage-debian:latest  
MAINTAINER Emanuele Peruffo <info@emanueleperuffo.com>  
  
ENV HOME /root  
ADD . /build  
  
ENV POSTGRES_VERSION 9.4  
ENV POSTGIS_VERSION 2.1  
ENV PGHOST 127.0.0.1  
ENV PGUSER nominatim  
ENV NOMINATIM_DEBUG false  
ENV NOMINATIM_DOMAIN www.example.com  
ENV NOMINATIM_SETUP_CACHE 1024  
ENV SPECIALPHRASES_COUNTRIES false  
ENV SPECIALPHRASES_WIKI false  
ENV OSM_FILE http://www.example.com/xxx.pbf  
ENV NGINX_HTTP true  
ENV NGINX_HTTPS false  
  
RUN /build/prepare.sh && \  
/build/services.sh && \  
/build/cleanup.sh  
  
VOLUME ["/etc/nginx", "/var/www", "/var/nominatim"]  
  
EXPOSE 80 443  
CMD ["/sbin/my_init"]

