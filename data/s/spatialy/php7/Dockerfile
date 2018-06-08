FROM spatialy/apache:latest  
MAINTAINER Yulian Diaz <yulian.diaz@ubiquos.io>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -qy && \  
apt-get install -qy \  
libapache2-mod-php \  
&& \  
apt-get autoremove -qy --purge && \  
apt-get clean -qy && \  
rm -rf /tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
  
RUN a2dismod mpm_event && \  
a2enmod mpm_prefork  

