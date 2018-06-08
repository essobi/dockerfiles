FROM ubuntu:14.04  
  
MAINTAINER developers <developers@studioskylab.com>  
  
ENV SITE_NAME dev  
ENV APACHE_LOG_DIR /var/log/website  
  
# Timezone  
ENV TIMEZONE Etc/UTC  
  
# Copy install scripts into place  
ENV SCRIPT_DIR /tmp/install  
COPY ./install ${SCRIPT_DIR}  
  
# Update OS and grab system deps  
# Ensure system is fully up-to-date  
RUN apt-get update \  
# Install system dependencies  
&& apt-get install -y --no-install-recommends \  
wget \  
curl \  
vim \  
build-essential \  
apache2 \  
libapache2-mod-php5 \  
openssl \  
openssh-client \  
php5 \  
php5-cli \  
php5-curl \  
php5-apcu \  
php5-gd \  
php5-imagick \  
php5-intl \  
php5-mcrypt \  
php5-xmlrpc \  
php5-mysql \  
php5-sybase \  
htop \  
git \  
php5-xdebug \  
make \  
npm \  
nodejs \  
nodejs-legacy \  
ruby \  
ruby-dev \  
python-pip \  
# PHP setup  
&& touch /etc/php5/mods-available/timezone.ini \  
&& echo "date.timezone = \"${TIMEZONE}\"" >> /etc/php5/mods-
available/timezone.ini \  
&& php5enmod mcrypt \  
curl \  
timezone \  
# Setup default host  
&& echo "ServerName localhost" >> /etc/apache2/apache2.conf \  
&& cp ${SCRIPT_DIR}/apache-default.conf /etc/apache2/sites-
available/000-default.conf \  
# Apache + PHP requires preforking Apache for best results  
&& a2dismod mpm_event && a2enmod mpm_prefork \  
# Setup apache modules  
&& a2enmod \  
rewrite \  
expires \  
filter \  
headers \  
rewrite \  
setenvif \  
proxy_http \  
remoteip \  
deflate \  
expires \  
env \  
# logs should go to stdout / stderr  
&& mkdir -p "$APACHE_LOG_DIR/error" \  
&& touch "$APACHE_LOG_DIR/error/$SITE_NAME.log" \  
&& ln -sfT /dev/stderr "$APACHE_LOG_DIR/error/$SITE_NAME.log" \  
&& mkdir -p "$APACHE_LOG_DIR/access" \  
&& touch "$APACHE_LOG_DIR/access/$SITE_NAME.log" \  
&& ln -sfT /dev/stdout "$APACHE_LOG_DIR/access/$SITE_NAME.log" \  
  
&& mkdir -p /var/log/apache2/ \  
&& touch /var/log/apache2/access.log \  
&& ln -sfT /dev/stderr /var/log/apache2/access.log \  
&& touch /var/log/apache2/error.log \  
&& ln -sfT /dev/stderr /var/log/apache2/error.log \  
&& touch /var/log/apache2/other_vhosts_access.log \  
&& ln -sfT /dev/stderr /var/log/apache2/other_vhosts_access.log \  
  
# Dev tools  
&& bash ${SCRIPT_DIR}/powerline.sh \  
&& bash ${SCRIPT_DIR}/latest_node.sh \  
&& bash ${SCRIPT_DIR}/php.sh \  
  
# Cleanup cache  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
# Remove install scripts  
&& rm -rf ${SCRIPT_DIR}  
  
EXPOSE 80  
  
ENTRYPOINT ["/usr/sbin/apache2ctl"]  
CMD ["-D", "FOREGROUND"]  

