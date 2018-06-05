# Create an Nginx instance that acts as an http load balancer.  
FROM ubuntu:14.04  
MAINTAINER Boyd Hemphill <boyd@stackengine.com>  
  
#  
# Install os packages  
#  
# Install supervisor and nginx  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y \  
python-setuptools \  
nginx  
  
#  
# Install and configure `supervisord`  
#  
ADD \  
supervisord/supervisord.conf \  
/etc/supervisord.conf  
  
RUN \  
easy_install supervisor  
  
ADD \  
supervisord/supervisord.conf \  
/etc/supervisord.conf  
  
#  
# Install and configure confd  
#  
ADD \  
confd/confd \  
/usr/bin/confd  
  
RUN \  
chmod +x /usr/bin/confd && \  
mkdir -p /etc/confd/conf.d && \  
mkdir -p /etc/confd/templates  
  
ADD \  
confd/confd.sh \  
/usr/bin/confd.sh  
  
RUN \  
chmod +x /usr/bin/confd.sh  
  
ADD \  
nginx/nginx.toml.template \  
/etc/confd/conf.d/nginx.toml.template  
  
ADD \  
nginx/nginx.conf.template \  
/etc/confd/templates/nginx.conf.template  
  
ENTRYPOINT /usr/local/bin/supervisord -c /etc/supervisord.conf  
  

