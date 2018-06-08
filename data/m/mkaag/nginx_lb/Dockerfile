FROM mkaag/baseimage:latest  
MAINTAINER Maurice Kaag <mkaag@me.com>  
  
#
-----------------------------------------------------------------------------  
# Environment variables  
#
-----------------------------------------------------------------------------  
ENV NEWRELIC_LICENSE false  
ENV NEWRELIC_APP false  
ENV CONFD_VERSION 0.9.0  
#
-----------------------------------------------------------------------------  
# Pre-install  
#
-----------------------------------------------------------------------------  
RUN \  
sed -i 's/^# \\(.*-backports\s\\)/\1/g' /etc/apt/sources.list && \  
wget -O - http://nginx.org/keys/nginx_signing.key | apt-key add - && \  
wget -O - https://download.newrelic.com/548C16BF.gpg | apt-key add - && \  
echo "deb http://nginx.org/packages/ubuntu/ trusty nginx" >
/etc/apt/sources.list.d/nginx.list && \  
echo "deb-src http://nginx.org/packages/ubuntu/ trusty nginx" >>
/etc/apt/sources.list.d/nginx.list && \  
echo "deb http://apt.newrelic.com/debian/ newrelic non-free" >
/etc/apt/sources.list.d/newrelic.list && \  
apt-get update -qqy  
  
#
-----------------------------------------------------------------------------  
# Install  
#
-----------------------------------------------------------------------------  
RUN \  
apt-get install -qqy \  
nginx-common \  
nginx-extras \  
nginx-nr-agent \  
newrelic-sysmond  
  
RUN \  
curl -s -L
https://github.com/kelseyhightower/confd/releases/download/v$CONFD_VERSION/confd-$CONFD_VERSION-
linux-amd64 -o /usr/local/bin/confd && \  
chmod +x /usr/local/bin/confd  
  
#
-----------------------------------------------------------------------------  
# Post-install  
#
-----------------------------------------------------------------------------  
ADD build/newrelic.sh /etc/my_init.d/10_setup_newrelic.sh  
ADD build/confd-watch /usr/local/bin/confd-watch  
ADD build/nginx.toml /etc/confd/conf.d/nginx.toml  
ADD build/nginx.tmpl /etc/confd/templates/nginx.tmpl  
ADD build/nginx.conf /etc/nginx/nginx.conf  
ADD build/status.conf /etc/nginx/conf.d/status.conf  
ADD build/ee_fastcgi_params /etc/nginx/ee_fastcgi_params  
  
RUN \  
chmod +x /usr/local/bin/confd-watch; \  
chmod +x /etc/my_init.d/10_setup_newrelic.sh; \  
rm /etc/nginx/sites-enabled/default  
  
EXPOSE 80 443  
VOLUME ["/var/www"]  
  
CMD ["/sbin/my_init"]  
  
#
-----------------------------------------------------------------------------  
# Clean up  
#
-----------------------------------------------------------------------------  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

