#  
# Define base image and maintainer  
#  
FROM phusion/baseimage:0.9.15  
MAINTAINER Deny Dias <deny@macpress.com.br>  
  
#  
# Start baseimage-docker's init system  
#  
CMD ["/sbin/my_init"]  
  
#  
# Define Metadata  
#  
ARG BUILD_DATE  
ARG VCS_REF  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.docker.dockerfile="/Dockerfile" \  
org.label-schema.license="GPLv3" \  
org.label-schema.name="BYOW Baseimage" \  
org.label-schema.url="https://hub.docker.com/r/denydias/byow-baseimage/" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-type="Git" \  
org.label-schema.vcs-url="https://github.com/denydias/byow-baseimage"  
#  
# Set default environment  
#  
ENV DEBIAN_FRONTEND=noninteractive \  
DEF_RUNAS_USER=www-data \  
DEF_RUNAS_UID=33 \  
DEF_RUNAS_GROUP=users \  
DEF_NGINX_MAX_WORKER_PROCESSES=8 \  
DEF_NGINX_UPLOAD_MAX_SIZE=50M \  
DEF_TIMEZONE="America/Sao_Paulo" \  
DEF_WP_RT=development \  
TERM=linux \  
WWW_DIR=/opt/www  
  
#  
# Install nginx and php-fpm with extensions for WordPress  
#  
RUN add-apt-repository -y ppa:nginx/stable \  
&& apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y --no-install-recommends \  
git \  
htop \  
memcached \  
nginx \  
php-pear \  
php5 \  
php5-cli \  
php5-fpm \  
php5-curl \  
php5-gd \  
php5-imagick \  
php5-imap \  
php5-intl \  
php5-mcrypt \  
php5-memcache \  
php5-ming \  
php5-mysql \  
php5-ps \  
php5-pspell \  
php5-recode \  
php5-sqlite \  
php5-tidy \  
php5-xmlrpc \  
php5-xsl \  
pwgen \  
tree \  
wget \  
&& apt-get clean \  
&& rm -rf /etc/nginx \  
/var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/* \  
&& mkdir -p /var/log/nginx \  
/var/cache/nginx  
  
#  
# Install WP-CLI  
#  
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar \  
&& chmod +x wp-cli.phar \  
&& mv wp-cli.phar /usr/local/bin/wp  
  
#  
# Copy and set permissions for configuration and initialization scripts  
#  
COPY etc /etc  
RUN chmod 750 /etc/my_init.d/*.sh \  
&& chmod 750 /etc/service/*/run  
  
#  
# Open ports  
#  
EXPOSE 80

