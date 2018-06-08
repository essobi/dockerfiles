FROM ubuntu:12.04  
MAINTAINER Michael Twomey <mick@twomeylee.name>  
  
RUN echo "deb http://repo.varnish-cache.org/ubuntu/ precise varnish-4.0" >
/etc/apt/sources.list.d/varnish.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 60E7C096C4DEFFEB  
  
RUN apt-get -y update && \  
apt-get -y install \  
varnish \  
&& apt-get autoclean \  
&& apt-get clean  
  
VOLUME ["/varnish/config"]  
  
VOLUME ["/varnish/logs"]  
  
ADD default.vcl /varnish/config/default.vcl  
ADD varnish.sh /varnish/varnish.sh  
RUN chmod 755 /varnish/varnish.sh  
  
EXPOSE 6081  
CMD []  
ENTRYPOINT ["/varnish/varnish.sh"]  

