# TenderPro modperl Dockerfile  
# See https://github.com/TenderPro/dockerfile-modperl  
FROM debian:wheezy  
  
MAINTAINER Alexey Kovrizhkin <lekovr+docker@gmail.com>  
  
ENV CONSUP_UBUNTU_CODENAME wheezy  
  
ENV DOCKERFILE_VERSION 180314  
#COPY 02proxy /etc/apt/apt.conf.d/  
#
-------------------------------------------------------------------------------  
# **** base ****  
#
-------------------------------------------------------------------------------  
ENV DEBIAN_FRONTEND noninteractive  
ENV INITRD No  
  
#
-------------------------------------------------------------------------------  
# Run custom setup scripts  
ADD setup_*.sh /tmp/  
  
# Loop does not cache every step  
#RUN for f in /tmp/setup_*.sh ; do >&2 echo ">>>> $f" ; . $f ; rm $f ; done  
RUN set -x \  
&& bash /tmp/setup_0backports.sh \  
&& bash /tmp/setup_1pkg.sh \  
&& bash /tmp/setup_2pgdg.sh \  
&& bash /tmp/setup_gosu.sh \  
&& bash /tmp/setup_lang.sh \  
&& bash /tmp/setup_nginx.sh \  
&& bash /tmp/setup_perl.sh \  
&& bash /tmp/setup_perllib_debian.sh \  
&& bash /tmp/setup_pg_client.sh  
  
#
-------------------------------------------------------------------------------  
# Setup primary lang  
ENV LANG en_US.UTF-8  
#
-------------------------------------------------------------------------------  
# user op  
RUN useradd -m -r -s /bin/bash -Gwww-data -gusers -gsudo op  
  
#
-------------------------------------------------------------------------------  
# **** modperl ****  
#
-------------------------------------------------------------------------------  
# Install apache-1.3.42 & mod_perl-1.31  
COPY asset-apache/*.deb /opt/apache/  
  
RUN set -x \  
&& cd /opt/apache \  
&& dpkg -i *.deb \  
&& mkdir -p /usr/local/apache/logs \  
&& mkdir /usr/local/apache/perl \  
&& mkdir /usr/local/apache/conf.d \  
&& mkdir /usr/local/apache/lib \  
&& sed -i 's/User nobody/User op/' /usr/local/apache/conf/httpd.conf \  
&& sed -i 's/Port 80/Port 3000/' /usr/local/apache/conf/httpd.conf \  
&& echo 'Include conf.d/*.conf' >> /usr/local/apache/conf/httpd.conf \  
&& mkdir -p /data/www  
  
COPY asset-apache/test.pl /usr/local/apache/perl/test.pl  
  
#
-------------------------------------------------------------------------------  
# nginx config files  
ADD fastcgi_params /etc/nginx/  
ADD proxy_params /etc/nginx/  
  
#
-------------------------------------------------------------------------------  
# supervisord config files  
COPY supervisor.d/*.conf /etc/supervisor/conf.d/  
  
# startup scripts  
COPY init.d /init.d  
  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
# Create user on start, see init.d/user.sh  
ENV APP_USER op  
  
# path to init script, see init.d/z-app.sh  
ENV APP_ROOT /data  
  
# expose ports for nginx - 80  
EXPOSE 80  
CMD ["server"]  

