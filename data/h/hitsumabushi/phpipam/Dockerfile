FROM debian:wheezy  
MAINTAINER hitsumabushi <hitsumabushi.org@gmail.com>  
  
ARG PHPIPAM_VERSION  
ARG APACHE_WEBROOT_DIR  
ENV APACHE_WEBROOT_DIR ${APACHE_WEBROOT_DIR:-/var/www/html}  
  
ENV APACHE_RUN_USER="www-data" \  
APACHE_RUN_GROUP="www-data" \  
APACHE_PID_FILE="/var/run/apache2.pid" \  
APACHE_RUN_DIR="/var/run/apache2" \  
APACHE_LOG_DIR="/var/log/apache2" \  
APACHE_LOCK_DIR="/var/lock/apache2" \  
APACHE_SERVER_ADMIN="webmaster@localhost" \  
SSL_ENABLED="false" \  
DEBUGGING="false" \  
PHPSESSNAME="phpipam" \  
PROXY_ENABLED="false"  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update \  
&& apt-get -y install apache2 libapache2-mod-php5 php5 php5-gmp php-pear
php5-mysql php5-ldap vim curl \  
&& a2enmod rewrite \  
&& mkdir -p "${APACHE_WEBROOT_DIR}" \  
&& curl -sL
"https://github.com/phpipam/phpipam/archive/${PHPIPAM_VERSION}.tar.gz" | tar
-xzC "${APACHE_WEBROOT_DIR}" \--strip-components=1 \  
&& chown -R "${APACHE_RUN_USER}":"${APACHE_RUN_GROUP}" "${APACHE_WEBROOT_DIR}"
\  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY 000-default.conf /etc/apache2/sites-available/default  
COPY config.php "${APACHE_WEBROOT_DIR}"  
  
ARG IMAGE_VCS_REF  
ARG IMAGE_BUILD_DATE  
  
LABEL PHPIPAM_VERSION="${PHPIPAM_VERSION}" \  
org.label-schema.schema-version="1.0" \  
org.label-schema.name="phpipam" \  
org.label-schema.version="${PHPIPAM_VERSION}" \  
org.label-schema.description="phpipam is an open-source web IP address
management application. Its goal is to provide light and simple IP address
management application." \  
org.label-schema.vendor="phpipam" \  
org.label-schema.url="https://github.com/phpipam/phpipam" \  
org.label-schema.usage="" \  
org.label-schema.vcs-url="https://github.com/hitsumabushi/docker-phpipam.git"
\  
org.label-schema.vcs-ref="${IMAGE_VCS_REF}" \  
org.label-schema.build-date="${IMAGE_BUILD_DATE}"  
  
EXPOSE 80 443  
CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]  

