FROM php:5.6.28-apache  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r mysql && useradd -r -g mysql mysql  
  
# add gosu for easy step-down from root  
ENV GOSU_VERSION 1.7  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget && rm -rf /var/lib/apt/lists/* \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apt-get purge -y --auto-remove ca-certificates wget  
  
RUN mkdir /mysql-initdb.d  
  
# install "pwgen" for randomizing passwords  
# install "apt-transport-https" for Percona's repo (switched to https-only)  
RUN apt-get update && apt-get install -y --no-install-recommends \  
apt-transport-https ca-certificates \  
pwgen \  
&& rm -rf /var/lib/apt/lists/*  
  
# Key fingerprint = 1993 69E5 404B D5FC 7D2F E43B CBCB 082A 1BB9 43DB  
# MariaDB Package Signing Key <package-signing-key@mariadb.org>  
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
199369E5404BD5FC7D2FE43BCBCB082A1BB943DB \  
# pub 1024D/CD2EFD2A 2009-12-15  
# Key fingerprint = 430B DF5C 56E7 C94E 848E E60C 1C4C BDCD CD2E FD2A  
# uid Percona MySQL Development Team <mysql-dev@percona.com>  
# sub 2048g/2D607DAF 2009-12-15  
&& apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
430BDF5C56E7C94E848EE60C1C4CBDCDCD2EFD2A \  
# pub 4096R/8507EFA5 2016-06-30  
# Key fingerprint = 4D1B B29D 63D9 8E42 2B21 13B1 9334 A25F 8507 EFA5  
# uid Percona MySQL Development Team (Packaging key) <mysql-dev@percona.com>  
# sub 4096R/4CAC6D72 2016-06-30  
&& apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
4D1BB29D63D98E422B2113B19334A25F8507EFA5  
  
RUN echo "deb https://repo.percona.com/apt jessie main" >
/etc/apt/sources.list.d/percona.list \  
&& { \  
echo 'Package: *'; \  
echo 'Pin: release o=Percona Development Team'; \  
echo 'Pin-Priority: 998'; \  
} > /etc/apt/preferences.d/percona  
  
ENV MARIADB_MAJOR 10.0  
ENV MARIADB_VERSION 10.0.28+maria-1~jessie  
  
RUN echo "deb http://ftp.osuosl.org/pub/mariadb/repo/$MARIADB_MAJOR/debian
jessie main" > /etc/apt/sources.list.d/mariadb.list \  
&& { \  
echo 'Package: *'; \  
echo 'Pin: release o=MariaDB'; \  
echo 'Pin-Priority: 999'; \  
} > /etc/apt/preferences.d/mariadb  
# add repository pinning to make sure dependencies from this MariaDB repo are
preferred over Debian dependencies  
# libmariadbclient18 : Depends: libmysqlclient18 (= 5.5.42+maria-1~wheezy) but
5.5.43-0+deb7u1 is to be installed  
# the "/var/lib/mysql" stuff here is because the mysql-server postinst doesn't
have an explicit way to disable the mysql_install_db codepath besides having a
database already "configured" (ie, stuff in /var/lib/mysql/mysql)  
# also, we set debconf keys to make APT a little quieter  
RUN { \  
echo mariadb-server-$MARIADB_MAJOR mysql-server/root_password password
'unused'; \  
echo mariadb-server-$MARIADB_MAJOR mysql-server/root_password_again password
'unused'; \  
} | debconf-set-selections \  
&& apt-get update \  
&& apt-get install -y \  
mariadb-server=$MARIADB_VERSION \  
# percona-xtrabackup is installed at the same time so that `mysql-common` is
only installed once from just mariadb repos  
percona-xtrabackup \  
socat \  
&& rm -rf /var/lib/apt/lists/* \  
# comment out any "user" entires in the MySQL config ("docker-entrypoint.sh"
or "--user" will handle user switching)  
&& sed -ri 's/^user\s/#&/' /etc/mysql/my.cnf /etc/mysql/conf.d/* \  
# purge and re-create /var/lib/mysql with appropriate ownership  
&& rm -rf /var/lib/mysql && mkdir -p /var/lib/mysql /var/run/mysqld \  
&& chown -R mysql:mysql /var/lib/mysql /var/run/mysqld \  
# ensure that /var/run/mysqld (used for socket and lock files) is writable
regardless of the UID our mysqld instance ends up having at runtime  
&& chmod 777 /var/run/mysqld  
  
# comment out a few problematic configuration values  
# don't reverse lookup hostnames, they are usually another container  
RUN sed -Ei 's/^(bind-address|log)/#&/' /etc/mysql/my.cnf \  
&& echo 'skip-host-cache\nskip-name-resolve' | awk '{ print } $1 == "[mysqld]"
&& c == 0 { c = 1; system("cat") }' /etc/mysql/my.cnf > /tmp/my.cnf \  
&& mv /tmp/my.cnf /etc/mysql/my.cnf  
  
VOLUME /var/lib/mysql  
  
RUN a2enmod rewrite  
  
# install the PHP extensions we need  
RUN apt-get update && apt-get install -y netcat-openbsd libpng12-dev libjpeg-
dev libpq-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mbstring pdo pdo_mysql pdo_pgsql zip mysql  
  
WORKDIR /var/www/html  
  
# https://www.drupal.org/node/3060/release  
ENV DRUPAL_VERSION 7.52  
ENV DRUPAL_MD5 4963e68ca12918d3a3eae56054214191  
ENV CIVICRM_VERSION 4.6.23  
ENV CIVICRM_MD5 58ae0594b94ccbbfb96cbc0cbf9de2b1  
  
RUN curl -fSL
"https://ftp.drupal.org/files/projects/drupal-${DRUPAL_VERSION}.tar.gz" -o
drupal.tar.gz \  
&& echo "${DRUPAL_MD5} *drupal.tar.gz" | md5sum -c - \  
&& tar -xz --strip-components=1 -f drupal.tar.gz \  
&& rm drupal.tar.gz \  
&& chown -R www-data:www-data sites \  
&& mkdir /sites-default-source \  
&& cd /var/www/html/sites/all/modules \  
&& curl -fSL
"https://download.civicrm.org/civicrm-${CIVICRM_VERSION}-drupal.tar.gz" -o
civicrm.tar.gz \  
&& echo "${CIVICRM_MD5} *civicrm.tar.gz" | md5sum -c - \  
&& tar -xzf civicrm.tar.gz \  
&& rm civicrm.tar.gz \  
&& curl -fSL "https://ftp.drupal.org/files/projects/og-7.x-2.9.tar.gz" -o
og.tar.gz \  
&& tar -xf og.tar.gz \  
&& rm og.tar.gz \  
&& curl -fSL "https://ftp.drupal.org/files/projects/rules-7.x-2.9.tar.gz" -o
rules.tar.gz \  
&& tar -xf rules.tar.gz \  
&& rm rules.tar.gz \  
&& curl -fSL "https://ftp.drupal.org/files/projects/entity-7.x-1.8.tar.gz" -o
entity.tar.gz \  
&& tar -xf entity.tar.gz \  
&& rm entity.tar.gz \  
&& curl -fSL
"https://ftp.drupal.org/files/projects/entityreference-7.x-1.2.tar.gz" -o
entityreference.tar.gz \  
&& tar -xf entityreference.tar.gz \  
&& rm entityreference.tar.gz \  
&& curl -fSL "https://ftp.drupal.org/files/projects/ctools-7.x-1.11.tar.gz" -o
ctools.tar.gz \  
&& tar -xf ctools.tar.gz \  
&& rm ctools.tar.gz \  
&& curl -fSL "https://ftp.drupal.org/files/projects/i18n-7.x-1.14.tar.gz" -o
il8n.tar.gz \  
&& tar -xf il8n.tar.gz \  
&& rm il8n.tar.gz \  
&& curl -fSL
"https://ftp.drupal.org/files/projects/views_bulk_operations-7.x-3.3.tar.gz"
-o views_bulk_operations.tar.gz \  
&& tar -xf views_bulk_operations.tar.gz \  
&& rm views_bulk_operations.tar.gz \  
&& curl -fSL "https://ftp.drupal.org/files/projects/views-7.x-3.14.tar.gz" -o
views.tar.gz \  
&& tar -xf views.tar.gz \  
&& rm views.tar.gz \  
&& curl -fSL "https://ftp.drupal.org/files/projects/webform-7.x-4.14.tar.gz"
-o webform.tar.gz \  
&& tar -xf webform.tar.gz \  
&& rm webform.tar.gz \  
&& curl -fSL
"https://ftp.drupal.org/files/projects/webform_civicrm-7.x-4.16.tar.gz" -o
webform_civicrm.tar.gz \  
&& tar -xf webform_civicrm.tar.gz \  
&& rm webform_civicrm.tar.gz \  
&& curl -fSL "https://ftp.drupal.org/files/projects/libraries-7.x-2.3.tar.gz"
-o libraries.tar.gz \  
&& tar -xf libraries.tar.gz \  
&& rm libraries.tar.gz \  
&& curl -fSL
"https://ftp.drupal.org/files/projects/options_element-7.x-1.12.tar.gz" -o
options_element.tar.gz \  
&& tar -xf options_element.tar.gz \  
&& rm options_element.tar.gz \  
&& chown -R www-data:www-data . \  
&& php -r "readfile('https://s3.amazonaws.com/files.drush.org/drush.phar');" >
/usr/local/bin/drush \  
&& chmod +x /usr/local/bin/drush \  
&& mkdir /root/.drush  
  
COPY .bashrc /root/  
COPY .drush/ /root/.drush/  
COPY scripts/ /usr/local/bin/  
COPY sql/ /mysql-initdb.d/  
COPY sites-default-source/ /sites-default-source/  
  
CMD ["start.sh"]  

