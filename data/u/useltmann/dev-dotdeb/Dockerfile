### install debian ###  
FROM debian:jessie  
MAINTAINER ulf.seltmann@metaccount.de  
EXPOSE 80 443 3306  
VOLUME ["/var/lib/mysql", "/var/run/mysqld", "/app", "/var/lib/xdebug"]  
ENTRYPOINT ["/docker/entrypoint"]  
CMD ["run"]  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y wget less vim supervisor
nullmailer graphviz locales ssh rsync graphicsmagick-imagemagick-compat
libapache2-mod-shib2 git \  
&& echo "deb http://packages.dotdeb.org jessie all"
>/etc/apt/sources.list.d/dotdeb.list \  
&& wget -O - http://www.dotdeb.org/dotdeb.gpg | apt-key add - \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y openssl ca-certificates
apache2-mpm-worker \  
php7.0-fpm php7.0-cli php-pear php7.0-curl php7.0-gd php7.0-intl php7.0-ldap
php7.0-readline php7.0-mcrypt php7.0-mysqlnd php7.0-sqlite php7.0-xdebug
php7.0-xsl php7.0-mbstring php7.0-dev \  
make mysql-client mysql-server unzip \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/cache/apt/archives/*  
  
ENV APP_HOME=/app \  
APP_USER=dev \  
FCGID_MAX_REQUEST_LEN=16384000 \  
TIME_ZONE=Europe/Berlin \  
WEBGRIND_ARCHIVE=1.1.0 \  
WEBGRIND_FORK=rovangju \  
SHIB_HOSTNAME=https://localhost \  
SHIB_HANDLER_URL=/Shibboleth.sso \  
SHIB_SP_ENTITY_ID=https://hub.docker.com/r/smoebody/dev-dotdeb \  
SHIB_IDP_DISCOVERY_URL=https://wayf.aai.dfn.de/DFN-AAI-Test/wayf \  
SHIB_ATTRIBUTE_MAP="" \  
SQL_MODE="" \  
SMTP_HOST="" \  
SMTP_NAME=dev-dotdeb \  
SMTP_PORT=25  
COPY assets/init /docker/init  
COPY assets/build /docker/build  
RUN chmod 755 /docker/init \  
&& /docker/init \  
&& rm -rf /docker/build  
  
COPY assets/setup /docker/setup  
COPY assets/entrypoint /docker/entrypoint  
RUN chmod 755 /docker/entrypoint  

