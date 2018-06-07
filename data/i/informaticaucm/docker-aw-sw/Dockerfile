# School of Computer Engineering at Complutense University  
#  
# LAMP stack for student projects  
FROM ubuntu:xenial  
LABEL maintainer="Ivan Martinez-Ortiz <imartinez@fdi.ucm.es>"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Optimize recurrent builds by using a helper container runing apt-cache  
ARG USE_APT_CACHE  
ENV USE_APT_CACHE ${USE_APT_CACHE}  
RUN ([ ! -z $USE_APT_CACHE ] && echo 'Acquire::http { Proxy
"http://172.17.0.1:3142"; };' >> /etc/apt/apt.conf.d/01proxy \  
&& echo 'Acquire::HTTPS::Proxy "false";' >> /etc/apt/apt.conf.d/01proxy) ||
true  
  
# grab tini for signal processing and zombie killing  
ENV TINI_VERSION v0.16.1  
RUN apt-get update && apt-get install -y --no-install-recommends \  
curl \  
&& curl -k -fSL
"https://github.com/krallin/tini/releases/download/$TINI_VERSION/tini" -o
/usr/local/bin/tini \  
&& curl -k -fSL
"https://github.com/krallin/tini/releases/download/$TINI_VERSION/tini.asc" -o
/usr/local/bin/tini.asc \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 \--recv-keys
595E85A6B1B4779EA4DAAEC70B588DFF0527A9B7 \  
&& gpg --batch --verify /usr/local/bin/tini.asc /usr/local/bin/tini \  
&& rm -r "$GNUPGHOME" /usr/local/bin/tini.asc && unset GNUPGHOME \  
&& chmod +x /usr/local/bin/tini \  
# installation cleanup  
&& apt-get remove --purge -y curl \  
&& apt-get clean \  
&& rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install and cofigure supervisor  
COPY supervisor/*.conf /etc/supervisor/conf.d/  
COPY supervisor/start_*.sh /usr/local/bin/  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
supervisor \  
&& chmod +x /usr/local/bin/start*.sh \  
# installation cleanup  
&& apt-get clean \  
&& rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install and configure OpenSSH  
ENV SSH_PASS default  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
openssh-server \  
# Configure SSH  
&& sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config \  
# SSH login fix. Otherwise user is kicked off after login  
&& sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd \  
&& mkdir /var/run/sshd && chmod 0755 /var/run/sshd \  
# installation cleanup  
&& apt-get clean \  
&& rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install and configure MySQL  
ENV MYSQL_PASS default  
COPY mysql/configure_mysql.sh /usr/local/bin  
  
RUN {\  
echo mysql-server-5.7 mysql-server/root_password password ''; \  
echo mysql-server-5.7 mysql-server/root_password_again password ''; \  
} | debconf-set-selections \  
&& apt-get update && apt-get install -y --no-install-recommends \  
mysql-server-5.7 \  
&& rm -fr /var/lib/mysql \  
&& mkdir -p /var/lib/mysql /var/run/mysqld \  
&& chown -R mysql:mysql /var/lib/mysql /var/run/mysqld \  
# ensure that /var/run/mysqld (used for socket and lock files) is writable
regardless of the UID our mysqld instance ends up having at runtime  
&& chmod 777 /var/run/mysqld \  
&& sed -i 's/127\\.0\\.0\\.1/0\\.0\\.0\\.0/g' /etc/mysql/my.cnf \  
# comment out a few problematic configuration values  
# don't reverse lookup hostnames, they are usually another container  
&& sed -Ei 's/^(bind-address|log)/#&/' /etc/mysql/mysql.conf.d/mysqld.cnf \  
&& echo '[mysqld]\nskip-host-cache\nskip-name-resolve' >
/etc/mysql/conf.d/docker.cnf \  
&& chmod +x /usr/local/bin/configure_mysql.sh \  
# installation cleanup  
&& apt-get clean \  
&& rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# Add volume for MySQL  
VOLUME [ "/var/lib/mysql" ]  
  
# Install and configure Apache 2.4 + PHP 7  
ENV PHP_UPLOAD_MAX_FILESIZE 10M  
ENV PHP_POST_MAX_SIZE 10M  
COPY apache/fix_acl.sh /usr/local/bin/  
  
RUN export GNUPGHOME="$(mktemp -d)" \  
&& gpg --no-default-keyring --keyring /etc/apt/trusted.gpg.d/ondrej-ppa.gpg
--keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
14AA40EC0831756756D7F66C4F4EA0AAE5267A6C \  
&& chmod 544 /etc/apt/trusted.gpg.d/ondrej-ppa.gpg \  
&& rm -fr "$GNUPGHOME" && unset GNUPGHOME \  
&& echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu xenial main" >
/etc/apt/sources.list.d/ondrej-ppa.list \  
&& echo "deb-src http://ppa.launchpad.net/ondrej/php/ubuntu xenial main" >>
/etc/apt/sources.list.d/ondrej-ppa.list \  
&& apt-get update && apt-get install -y --no-install-recommends \  
apache2 libapache2-mod-php7.2 php7.2-mysqli php7.2-mbstring php7.2-xml
php7.2-gd php7.2-bz2 php7.2-zip php7.2-curl php7.2-opcache php7.2-json php-
apcu \  
&& echo "ServerName localhost" >> /etc/apache2/apache2.conf \  
&& a2enmod rewrite \  
&& chmod +x /usr/local/bin/fix_acl.sh \  
# installation cleanup  
&& apt-get clean \  
&& rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*
/etc/apt/trusted.gpg.d/ondrej-ppa.gpg /etc/apt/sources.list.d/ondrej-ppa.list  
# Add volumes for Apache2 + PHP  
VOLUME ["/var/www", "/etc/apache2", "/etc/php/" ]  
  
# Install phpmyadmin  
ENV PHP_MY_ADMIN_VERSION 4.7.7  
ENV PHP_MY_ADMIN_HOME /opt/phpmyadmin  
COPY phpmyadmin/configure_phpmyadmin.sh /usr/local/bin  
RUN apt-get update && apt-get install -y --no-install-recommends \  
curl \  
&& curl -k -fSL
"https://files.phpmyadmin.net/phpMyAdmin/${PHP_MY_ADMIN_VERSION}/phpMyAdmin-${PHP_MY_ADMIN_VERSION}-all-
languages.tar.gz" -o /opt/phpmyadmin.tar.gz \  
&& curl -k -fSL
"https://files.phpmyadmin.net/phpMyAdmin/${PHP_MY_ADMIN_VERSION}/phpMyAdmin-${PHP_MY_ADMIN_VERSION}-all-
languages.tar.gz.asc" -o /opt/phpmyadmin.tar.gz.asc \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
3D06A59ECE730EB71B511C17CE752F178259BD92 \  
&& gpg --batch --verify /opt/phpmyadmin.tar.gz.asc /opt/phpmyadmin.tar.gz \  
&& rm -r "$GNUPGHOME" && unset GNUPGHOME \  
&& tar xzf /opt/phpmyadmin.tar.gz -C /opt \  
&& mv "/opt/phpMyAdmin-${PHP_MY_ADMIN_VERSION}-all-languages"
"$PHP_MY_ADMIN_HOME" \  
&& rm -rf "$PHP_MY_ADMIN_HOME/setup/" "$PHP_MY_ADMIN_HOME/examples/"
"$PHP_MY_ADMIN_HOME/test/" "$PHP_MY_ADMIN_HOME/po/"
"$PHP_MY_ADMIN_HOME/composer.json" "$PHP_MY_ADMIN_HOME/RELEASE-
DATE-${PHP_MY_ADMIN_VERSION}" \  
&& sed -i "s@define('CONFIG_DIR'.*@define('CONFIG_DIR', '/etc/phpmyadmin/');@"
"$PHP_MY_ADMIN_HOME/libraries/vendor_config.php" \  
&& chown -R www-data:www-data "$PHP_MY_ADMIN_HOME" \  
&& find "$PHP_MY_ADMIN_HOME" -type d -exec chmod 750 {} \; \  
&& find "$PHP_MY_ADMIN_HOME" -type f -exec chmod 640 {} \; \  
&& chmod +x /usr/local/bin/configure_phpmyadmin.sh \  
&& mkdir /etc/phpmyadmin \  
# installation cleanup  
&& apt-get remove --purge -y curl \  
&& apt-get clean \  
&& rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/* /opt/phpmyadmin.tar.gz
/opt/phpmyadmin.tar.gz.asc  
COPY phpmyadmin/config.inc.php /etc/phpmyadmin  
COPY phpmyadmin/apache.conf /etc/phpmyadmin  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
pwgen \  
# installation cleanup  
&& apt-get remove --purge -y curl \  
&& apt-get clean \  
&& rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY run.sh /usr/local/bin  
RUN chmod +x /usr/local/bin/run.sh  
  
ENTRYPOINT ["/usr/local/bin/tini", "--"]  
  
EXPOSE 80 22  
## Run your program under Tini  
CMD ["/usr/local/bin/run.sh"]  

