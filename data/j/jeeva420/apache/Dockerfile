FROM jeeva420/xenial-base  
MAINTAINER Jeeva Kailasam <kjeeva@ymail.com>  
  
# Set correct environment variables  
ARG BASE_APTLIST="apache2 php7.0 libapache2-mod-php7.0 lynx-cur openssl"  
ARG DEBIAN_FRONTEND="noninteractive"  
ARG APACHE_MODULES="php7.0 rewrite ssl proxy proxy_http proxy_ajp deflate
headers proxy_balancer proxy_connect proxy_html xml2enc"  
# install main packages  
RUN apt-get update -q && \  
apt-get install $BASE_APTLIST -qy && \  
# cleanup  
apt-get autoremove -y && \  
apt-get clean -y && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# add some files  
RUN echo "copying folders and files from the project"  
ADD defaults/ /defaults/  
ADD etc/cont-init.d/ /etc/cont-init.d/  
ADD etc/services.d/ /etc/services.d/  
#ADD etc/fix-attrs.d/ /etc/fix-attrs.d/  
RUN chmod -v +x /etc/services.d/*/run /etc/cont-init.d/*.sh && \  
# enable apache mods  
mv /defaults/envvars /etc/apache2/envvars && \  
sed -i "s#/var/www#/config/www#g" /etc/apache2/apache2.conf && \  
sed -i "s#IncludeOptional sites-enabled#IncludeOptional /config/apache/site-
confs#g" /etc/apache2/apache2.conf && \  
a2enmod $APACHE_MODULES  
  
# expose ports  
EXPOSE 80 443  
# set volumes  
VOLUME /config  

