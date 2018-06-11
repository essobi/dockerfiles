FROM tweyand/ubuntu:xenial  
MAINTAINER Tim Weyand <tim.weyand@klambt.de>  
  
ENV VARNISH_CONFIG default \  
VCL_CONFIG /etc/varnish/default.vcl \  
CACHE_SIZE 64m \  
VARNISHD_PARAMS -a :80 -T :6082 -p default_ttl=3600 -p default_grace=3600 -p
default_grace=180 -p feature=+esi_disable_xml_check -S /etc/varnish/secret \  
BACKEND_SERVER webserver \  
BACKEND_STYLE default  
  
COPY ./scripts/* /usr/local/bin/  
ADD ./conf/ /root/varnish-conf/  
  
RUN chmod +x /usr/local/bin/klambt_docker_*.sh \  
&& klambt_docker_varnish_install.sh  
  
EXPOSE 80 6082 6081  
CMD klambt_docker_varnish_start.sh  

