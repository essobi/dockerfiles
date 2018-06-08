  
#  
# Debian 7 (wheezy) PHP56 Language (dockerfile)  
# Copyright (C) 2016-2017 Stafli  
# Luís Pedro Algarvio  
# This file is part of the Stafli Application Stack.  
#  
# This program is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, either version 3 of the License, or  
# (at your option) any later version.  
#  
# This program is distributed in the hope that it will be useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU General Public License for more details.  
#  
# You should have received a copy of the GNU General Public License  
# along with this program. If not, see <http://www.gnu.org/licenses/>.  
#  
#  
# Build  
#  
# Base image to use  
FROM stafli/stafli.init.supervisor:supervisor30_debian7  
  
# Labels to apply  
LABEL description="Stafli PHP Language (stafli/stafli.language.php), Based on
Stafli Supervisor Init (stafli/stafli.init.supervisor)" \  
maintainer="lp@algarvio.org" \  
org.label-schema.schema-version="1.0.0-rc.1" \  
org.label-schema.name="Stafli PHP Language (stafli/stafli.language.php)" \  
org.label-schema.description="Based on Stafli Supervisor Init
(stafli/stafli.init.supervisor)" \  
org.label-schema.keywords="stafli, php, language, debian, centos" \  
org.label-schema.url="https://stafli.org/" \  
org.label-schema.license="GPLv3" \  
org.label-schema.vendor-name="Stafli" \  
org.label-schema.vendor-email="info@stafli.org" \  
org.label-schema.vendor-website="https://www.stafli.org" \  
org.label-schema.authors.lpalgarvio.name="Luis Pedro Algarvio" \  
org.label-schema.authors.lpalgarvio.email="lp@algarvio.org" \  
org.label-schema.authors.lpalgarvio.homepage="https://lp.algarvio.org" \  
org.label-schema.authors.lpalgarvio.role="Maintainer" \  
org.label-schema.registry-
url="https://hub.docker.com/r/stafli/stafli.language.php" \  
org.label-schema.vcs-url="https://github.com/stafli-org/stafli.language.php" \  
org.label-schema.vcs-branch="master" \  
org.label-schema.os-id="debian" \  
org.label-schema.os-version-id="7" \  
org.label-schema.os-architecture="amd64" \  
org.label-schema.version="1.0"  
  
#  
# Arguments  
#  
ARG app_php_exts_core_dis="mysql"  
ARG app_php_exts_core_en="mcrypt curl gd imap ldap mysqli mysqlnd odbc pdo
pdo_mysql pdo_odbc opcache"  
ARG app_php_exts_extra_dis="xdebug xhprof"  
ARG app_php_exts_extra_en="igbinary msgpack yaml solr mongodb memcache
memcached redis"  
ARG app_php_global_log_level="E_ALL"  
ARG app_php_global_log_display="On"  
ARG app_php_global_log_file="On"  
ARG app_php_global_limit_timeout="120"  
ARG app_php_global_limit_memory="134217728"  
ARG app_fpm_global_user="www-data"  
ARG app_fpm_global_group="www-data"  
ARG app_fpm_global_home="/var/www"  
ARG app_fpm_global_log_level="notice"  
ARG app_fpm_global_limit_descriptors="1024"  
ARG app_fpm_global_limit_processes="128"  
ARG app_fpm_pool_id="default"  
ARG app_fpm_pool_user="www-data"  
ARG app_fpm_pool_group="www-data"  
ARG app_fpm_pool_listen_wlist=""  
ARG app_fpm_pool_listen_addr="[::]"  
ARG app_fpm_pool_listen_port="9000"  
ARG app_fpm_pool_limit_descriptors="1024"  
ARG app_fpm_pool_limit_backlog="65536"  
ARG app_fpm_pool_pm_method="dynamic"  
ARG app_fpm_pool_pm_max_children="100"  
ARG app_fpm_pool_pm_start_servers="20"  
ARG app_fpm_pool_pm_min_spare_servers="10"  
ARG app_fpm_pool_pm_max_spare_servers="30"  
ARG app_fpm_pool_pm_process_idle_timeout="10s"  
ARG app_fpm_pool_pm_max_requests="5000"  
#  
# Environment  
#  
# Working directory to use when executing build and run instructions  
# Defaults to /.  
#WORKDIR /  
# User and group to use when executing build and run instructions  
# Defaults to root.  
#USER root:root  
#  
# Packages  
#  
# Add foreign repositories and GPG keys  
# - packages.dotdeb.org: for DotDeb  
# - apt.mariadb.org: for MariaDB  
# Refresh the package manager  
# Install the selected packages  
# Install the php packages  
# - php5: the server-side, HTML-embedded scripting language (metapackage)  
# - php5-common: the PHP common libraries and files  
# - php-pear: the PEAR package manager  
# - php5-cli: for php5, the PHP CLI (command line interface)  
# - php5-fpm: the PHP FPM (fast process manager)  
# - php5-gmp: the PHP GMP (GNU Multiple Precision) arithmetic extension  
# - php5-mcrypt: the PHP Mcrypt extension  
# - php5-json: the PHP JSON (JavaScript Object Notation) extension  
# - php5-xmlrpc: the PHP XML-RPC (Extensible Markup Language - Remote
Procedure Call) extension  
# - php5-gd: the PHP GD (Graphics Draw) extension  
# - php5-imap: the PHP IMAP (IMAP, POP3 and NNTP) extension  
# - php5-geoip: the PHP GeoIP extension  
# - php5-curl: the PHP cURL extension  
# - php5-ssh2: the PHP SSH2 (Secure Shell version 2) extension  
# - php5-ldap: the PHP LDAP (Lightweight Directory Access Protocol) extension  
# - php5-mysqlnd: the PHP MySQLND (MySQL Native Driver) extension  
# - php5-pgsql: the PHP PgSQL (PostgreSQL) extension  
# - php5-sqlite: the PHP SQLite extension  
# - php5-odbc: the PHP ODBC (Open Database Connectivity) extension  
# Install the utilities and clients packages  
# - apache2-utils: for ab and others, the HTTPd utilities  
# - libfcgi0ldbl: the Shared library of FastCGI, which includes the command
cgi-fcgi  
# - mariadb-client: for mysql, the MariaDB client  
# - postgresql-client: for psql, the front-end programs for PostgreSQL  
# - sqlite3: for sqlite, the Command line interface for SQLite 3  
# - redis-tools: for redis-cli, the Redis client  
# Cleanup the package manager  
RUN printf "Installing repositories and packages...\n" && \  
\  
printf "Install the repositories and refresh the GPG keys...\n" && \  
printf "# Dotdeb repository\n\  
deb http://packages.dotdeb.org wheezy all\n\  
deb http://packages.dotdeb.org wheezy-php56 all\n\  
\n" > /etc/apt/sources.list.d/dotdeb.list && \  
apt-key adv --fetch-keys http://www.dotdeb.org/dotdeb.gpg && \  
\  
printf "# MariaDB repository\n\  
deb http://lon1.mirrors.digitalocean.com/mariadb/repo/10.1/debian wheezy
main\n\  
\n" > /etc/apt/sources.list.d/mariadb.list && \  
apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 0xcbcb082a1bb943db &&
\  
\  
printf "Refresh the package manager...\n" && \  
apt-get update && \  
\  
printf "Install the php packages...\n" && \  
apt-get install -qy \  
php5 php5-common php-pear \  
php5-cli php5-fpm \  
php5-gmp php5-mcrypt \  
php5-json php5-xmlrpc \  
php5-gd php5-imap \  
php5-geoip php5-curl php5-ssh2 \  
php5-ldap \  
php5-mysqlnd php5-pgsql php5-sqlite php5-odbc && \  
\  
printf "Install the utilities and clients packages...\n" && \  
apt-get install -qy \  
apache2-utils libfcgi0ldbl \  
mariadb-client postgresql-client sqlite3 \  
redis-tools && \  
\  
printf "Cleanup the package manager...\n" && \  
apt-get clean && rm -rf /var/lib/apt/lists/* && rm -Rf /var/cache/apt/* && \  
\  
printf "Finished installing repositories and packages...\n";  
  
#  
# PHP extensions  
#  
# Refresh the package manager  
# Install the selected packages  
# Install the binary library packages  
# - libssl1.0.0, the Secure Sockets Layer toolkit - shared libraries (required
for running)  
# - libcurl3, the easy-to-use client-side URL transfer library (OpenSSL
flavour) (required for running)  
# - libsasl2-2, the Cyrus SASL - authentication abstraction library (required
for running)  
# - libxml2, the GNOME XML library (required for running)  
# - zlib1g, the compression library - runtime (required for running)  
# - libyaml-0-2, the Fast YAML 1.1 parser and emitter library (required for
running)  
# - libmemcached11, the C and C++ client library to the memcached server
(required for running)  
# Install the php packages  
# - php5-dev: the PHP development libraries and files (required for compiling)  
# Install the parser packages  
# - gawk: for gawk, GNU awk, a pattern scanning and processing language  
# - m4: for m4, the GNU m4 which is an interpreter for a macro processing
language (required for compiling)  
# - re2c: for r2ec, a tool for generating fast C-based recognizers  
# Install the build tools packages  
# - make: for make, the GNU make which is an utility for Directing compilation  
# - automake: for automake, a tool for generating GNU Standards-compliant
Makefiles (required for compiling)  
# - autoconf: for autoconf, a automatic configure script builder for FSF
source packages (required for compiling)  
# - pkg-config: for pkg-config, a tool to manage compile and link flags for
libraries (required for compiling)  
# - libtool: for GNU libtool, a generic library support script (required for
compiling)  
# Install the compiler packages  
# - cpp: for cpp, the GNU C preprocessor (cpp) for the C Programming language
(required for compiling)  
# - gcc: for gcc, the GNU C compiler (required for compiling)  
# - g++: for g++, the GNU C++ compiler (required for compiling)  
# Install the library packages  
# - linux-libc-dev: the Linux Kernel - Headers for development (required for
compiling)  
# - libc6-dev: the Embedded GNU C Library - Development Libraries and Header
Files (required for compiling)  
# - libpcre3-dev: the Perl 5 Compatible Regular Expression Library -
development files (required for compiling)  
# - libssl-dev: the OpenSSL toolkit - development files (required for
compiling)  
# - libcurl4-openssl-dev: the CURL library - development files (OpenSSL
version)  
# - libsasl2-dev: the Cyrus SASL library - development files  
# - libxml2-dev: the GNOME XML library - development files  
# - zlib1g-dev: the ZLib library - development files (required for compiling)  
# - libyaml-dev: the YAML library - development files  
# - libmemcached-dev: the Memcached library - development files  
# Build and install the php extensions  
# - Binary API (igbinary)  
# - MessagePack (msgpack)  
# - YAML  
# - Solr  
# - MongoDB  
# - Memcache  
# - Memcached  
# - Redis  
# - Xdebug  
# - XHProf  
# Remove the various development packages  
# Cleanup the package manager  
# Enable/disable the php extensions  
RUN printf "Start installing extensions...\n" && \  
\  
printf "Refresh the package manager...\n" && \  
apt-get update && \  
\  
printf "Install the runtime packages...\n" && \  
apt-get install -qy \  
libssl1.0.0 libcurl3 \  
libsasl2-2 \  
libxml2 zlib1g \  
libyaml-0-2 libmemcached11 && \  
\  
printf "Install the development packages...\n" && \  
packages_devel=" \  
php5-dev \  
gawk m4 re2c \  
make automake autoconf pkg-config libtool \  
cpp gcc g++ \  
linux-libc-dev libc6-dev libpcre3-dev \  
libssl-dev libcurl4-openssl-dev \  
libsasl2-dev \  
libxml2-dev zlib1g-dev \  
libyaml-dev libmemcached-dev \  
" && \  
apt-get install -qy \  
${packages_devel} && \  
\  
printf "Building the Binary API (deb: N/A) extension...\n" && \  
$(which pecl) install igbinary-1.2.1 && \  
$(which pecl) install igbinary-2.0.5 && \  
echo "extension=igbinary.so" > /etc/php5/mods-available/igbinary.ini && \  
rm -rf /tmp/pear && \  
\  
printf "Building the MessagePack (deb: php5-msgpack) extension...\n" && \  
$(which pecl) install msgpack-0.5.7 && \  
echo "extension=msgpack.so" > /etc/php5/mods-available/msgpack.ini && \  
rm -rf /tmp/pear && \  
\  
printf "Building the YAML (deb: N/A) extension...\n" && \  
$(which pecl) install yaml-1.2.0 && \  
$(which pecl) install yaml-1.3.1 && \  
echo "extension=yaml.so" > /etc/php5/mods-available/yaml.ini && \  
rm -rf /tmp/pear && \  
\  
printf "Building the Solr (deb: N/A) extension...\n" && \  
$(which pecl) install solr-2.4.0 && \  
echo "extension=solr.so" > /etc/php5/mods-available/solr.ini && \  
rm -rf /tmp/pear && \  
\  
printf "Building the MongoDB (deb: php5-mongo) extension...\n" && \  
$(which pecl) install mongodb-1.1.9 && \  
$(which pecl) install mongodb-1.3.4 && \  
echo "extension=mongodb.so" > /etc/php5/mods-available/mongodb.ini && \  
rm -rf /tmp/pear && \  
\  
printf "Building the Memcache (deb: php5-memcache) extension...\n" && \  
$(which pecl) install memcache-2.2.7 && \  
$(which pecl) install memcache-3.0.8 && \  
echo "extension=memcache.so" > /etc/php5/mods-available/memcache.ini && \  
rm -rf /tmp/pear && \  
\  
printf "Building the Memcached (deb: php5-memcached) extension...\n" && \  
( \  
curl -sL https://github.com/php-memcached-dev/php-
memcached/archive/2.2.0.tar.gz | tar xz && cd php-memcached-2.2.0 && \  
perl -0p -i -e "s><extsrcrelease\>><extsrcrelease\>\n\  
<configureoption name=\"enable-memcached-sasl\" default=\"yes\"
prompt=\"Enable SASL\"/\>\n\  
<configureoption name=\"enable-memcached-json\" default=\"yes\"
prompt=\"Enable JSON\"/\>\n\  
<configureoption name=\"enable-memcached-igbinary\" default=\"yes\"
prompt=\"Enable igbinary\"/\>\n\  
<configureoption name=\"enable-memcached-msgpack\" default=\"yes\"
prompt=\"Enable msgpack\"/\>\n\  
<configureoption name=\"enable-memcached-protocol\" default=\"no\"
prompt=\"Enable protocol\"/\>\  
>" package.xml && \  
$(which pecl) install package.xml && \  
echo -e "extension=memcached.so\n\n$(cat memcached.ini)" > /etc/php5/mods-
available/memcached.ini && \  
cd .. && rm -Rf php-memcached-2.2.0 \  
) && \  
rm -rf /tmp/pear && \  
\  
printf "Building the Redis (deb: php5-redis) extension...\n" && \  
( \  
curl -sL https://github.com/phpredis/phpredis/archive/2.2.8.tar.gz | tar xz &&
cd phpredis-2.2.8 && \  
perl -0p -i -e "s><extsrcrelease/\>><extsrcrelease\>\n\  
<configureoption name=\"enable-redis-igbinary\" default=\"yes\"
prompt=\"Enable igbinary\"/\>\n\  
</extsrcrelease\>>" package.xml && \  
$(which pecl) install package.xml && \  
cd .. && rm -Rf phpredis-2.2.8 \  
) && \  
echo "extension=redis.so" > /etc/php5/mods-available/redis.ini && \  
rm -rf /tmp/pear && \  
\  
printf "Building the Xdebug (deb: php5-xdebug) extension...\n" && \  
$(which pecl) install xdebug-2.4.1 && \  
$(which pecl) install xdebug-2.5.5 && \  
echo "zend_extension=xdebug.so" > /etc/php5/mods-available/xdebug.ini && \  
rm -rf /tmp/pear && \  
\  
printf "Building the XHProf (deb: php5-xhprof) extension...\n" && \  
$(which pecl) install xhprof-0.9.4 && \  
echo "extension=xhprof.so" > /etc/php5/mods-available/xhprof.ini && \  
rm -rf /tmp/pear && \  
\  
printf "Done building extensions...\n" && \  
\  
printf "Remove the various development packages...\n" && \  
apt-get remove --purge ${packages_devel} -qy && \  
apt-get autoremove --purge -qy && \  
\  
printf "Cleanup the package manager...\n" && \  
apt-get clean && rm -rf /var/lib/apt/lists/* && rm -Rf /var/cache/apt/* && \  
\  
printf "Enabling/disabling extensions...\n" && \  
# Core extensions \  
$(which php5dismod) -f ${app_php_exts_core_dis} && \  
$(which php5enmod) -f ${app_php_exts_core_en} && \  
# Extra extensions \  
$(which php5dismod) -f ${app_php_exts_extra_dis} && \  
$(which php5enmod) -f ${app_php_exts_extra_en} && \  
printf "Done enabling/disabling extensions...\n" && \  
\  
printf "\nChecking extensions...\n" && \  
$(which php) -m && \  
printf "Done checking extensions...\n" && \  
\  
printf "Finished installing extensions...\n";  
  
#  
# PHP tools  
#  
# Install php tools  
# - Composer  
# - Drush  
RUN printf "Start installing tools...\n" && \  
\  
printf "Installing composer...\n" && \  
$(which php) -r "copy('https://getcomposer.org/installer', 'composer-
setup.php');" && \  
$(which php) composer-setup.php --install-dir=/usr/local/bin
--filename=composer && \  
$(which php) -r "unlink('composer-setup.php');" && \  
\  
printf "Installing drush...\n" && \  
$(which php) -r
"readfile('https://s3.amazonaws.com/files.drush.org/drush.phar');" >
/usr/local/bin/drush && \  
chmod +x /usr/local/bin/drush && \  
$(which drush) core-init --add-path -y && \  
$(which drush) @none dl registry_rebuild-7.x && \  
$(which drush) cc drush && \  
\  
printf "Finished installing tools...\n";  
  
#  
# Configuration  
#  
# Add users and groups  
RUN printf "Adding users and groups...\n" && \  
\  
printf "Add php-fpm user and group...\n" && \  
id -g ${app_fpm_global_user} \  
|| \  
groupadd \  
\--system ${app_fpm_global_group} && \  
id -u ${app_fpm_global_user} && \  
usermod \  
\--gid ${app_fpm_global_group} \  
\--home ${app_fpm_global_home} \  
\--shell /usr/sbin/nologin \  
${app_fpm_global_user} \  
|| \  
useradd \  
\--system --gid ${app_fpm_global_group} \  
\--no-create-home --home-dir ${app_fpm_global_home} \  
\--shell /usr/sbin/nologin \  
${app_fpm_global_user} && \  
\  
printf "Add pool user and group...\n" && \  
app_fpm_pool_home="${app_fpm_global_home}/${app_fpm_pool_id}" && \  
id -g ${app_fpm_pool_user} \  
|| \  
groupadd \  
\--system ${app_fpm_pool_group} && \  
id -u ${app_fpm_pool_user} && \  
usermod \  
\--gid ${app_fpm_global_group} \  
\--home ${app_fpm_pool_home} \  
\--shell /usr/sbin/nologin \  
${app_fpm_global_user} \  
|| \  
useradd \  
\--system --gid ${app_fpm_pool_group} \  
\--create-home --home-dir ${app_fpm_pool_home} \  
\--shell /usr/sbin/nologin \  
${app_fpm_pool_user} && \  
\  
printf "Setting pool ownership and permissions...\n" && \  
mkdir -p ${app_fpm_pool_home}/bin ${app_fpm_pool_home}/log
${app_fpm_pool_home}/html ${app_fpm_pool_home}/tmp && \  
chown -R ${app_fpm_global_user}:${app_fpm_global_group} ${app_fpm_pool_home}
&& \  
chmod -R ug=rwX,o=rX ${app_fpm_pool_home} && \  
\  
printf "Finished adding users and groups...\n";  
  
# Supervisor  
RUN printf "Updading Supervisor configuration...\n" && \  
\  
# /etc/supervisor/conf.d/init.conf \  
file="/etc/supervisor/conf.d/init.conf" && \  
printf "\n# Applying configuration for ${file}...\n" && \  
perl -0p -i -e "s>supervisorctl start rclocal;>supervisorctl start rclocal;
supervisorctl start phpfpm;>" ${file} && \  
printf "Done patching ${file}...\n" && \  
\  
# /etc/supervisor/conf.d/phpfpm.conf \  
file="/etc/supervisor/conf.d/phpfpm.conf" && \  
printf "\n# Applying configuration for ${file}...\n" && \  
printf "# PHP-FPM\n\  
[program:phpfpm]\n\  
command=/bin/bash -c \"\$(which php5-fpm) -y /etc/php5/fpm/php-fpm.conf -c
/etc/php5/fpm/php.ini --nodaemonize\"\n\  
autostart=false\n\  
autorestart=true\n\  
stdout_logfile=/dev/stdout\n\  
stdout_logfile_maxbytes=0\n\  
stderr_logfile=/dev/stderr\n\  
stderr_logfile_maxbytes=0\n\  
stdout_events_enabled=true\n\  
stderr_events_enabled=true\n\  
\n" > ${file} && \  
printf "Done patching ${file}...\n" && \  
\  
printf "Finished updading Supervisor configuration...\n";  
  
# PHP / PHP-FPM  
RUN printf "Updading PHP and PHP-FPM configuration...\n" && \  
\  
# /etc/php5/cli/php.ini \  
file="/etc/php5/cli/php.ini" && \  
printf "\n# Applying configuration for ${file}...\n" && \  
# change logging \  
perl -0p -i -e "s>; http://php.net/error-reporting\nerror_reporting = .*>;
http://php.net/error-reporting\nerror_reporting =
${app_php_global_log_level}>" ${file} && \  
perl -0p -i -e "s>; http://php.net/display-startup-
errors\ndisplay_startup_errors = .*>; http://php.net/display-startup-
errors\ndisplay_startup_errors = ${app_php_global_log_display}>" ${file} && \  
perl -0p -i -e "s>; http://php.net/display-errors\ndisplay_errors = .*>;
http://php.net/display-errors\ndisplay_errors =
${app_php_global_log_display}>" ${file} && \  
perl -0p -i -e "s>; http://php.net/log-errors\nlog_errors = .*>;
http://php.net/log-errors\nlog_errors = ${app_php_global_log_file}>" ${file}
&& \  
perl -0p -i -e "s>; http://php.net/log-errors-max-len\nlog_errors_max_len =
.*>; http://php.net/log-errors-max-len\nlog_errors_max_len = 10M>" ${file} &&
\  
perl -0p -i -e "s>; http://php.net/error-log\n>; http://php.net/error-
log\nerror_log = /proc/self/fd/2\n>" ${file} && \  
# change timeouts \  
perl -0p -i -e "s>; http://php.net/max-input-time\nmax_input_time = .*>;
http://php.net/max-input-time\nmax_input_time = -1>" ${file} && \  
perl -0p -i -e "s>; Note: This directive is hardcoded to 0 for the CLI
SAPI\nmax_execution_time = .*>; Note: This directive is hardcoded to 0 for the
CLI SAPI\nmax_execution_time = -1>" ${file} && \  
# change memory limit \  
perl -0p -i -e "s>; http://php.net/memory-limit\nmemory_limit = .*>;
http://php.net/memory-limit\nmemory_limit = -1>" ${file} && \  
# change upload limit \  
perl -0p -i -e "s>; http://php.net/post-max-size\npost_max_size = .*>;
http://php.net/post-max-size\npost_max_size = -1>" ${file} && \  
perl -0p -i -e "s>; http://php.net/upload-max-filesize\nupload_max_filesize =
.*>; http://php.net/upload-max-filesize\nupload_max_filesize = -1>" ${file} &&
\  
# change i18n \  
perl -0p -i -e "s>; http://php.net/default-mimetype\ndefault_mimetype = .*>;
http://php.net/default-mimetype\ndefault_mimetype = \"text/html\">" ${file} &&
\  
perl -0p -i -e "s>; http://php.net/default-charset\ndefault_charset =.*>;
http://php.net/default-charset\ndefault_charset = \"UTF-8\">" ${file} && \  
perl -0p -i -e "s>; http://php.net/date.timezone\n;date.timezone =.*>;
http://php.net/date.timezone\ndate.timezone = \"UTC\">" ${file} && \  
printf "Done patching ${file}...\n" && \  
\  
# /etc/php5/fpm/php.ini \  
file="/etc/php5/fpm/php.ini" && \  
printf "\n# Applying configuration for ${file}...\n" && \  
# change logging \  
perl -0p -i -e "s>; http://php.net/error-reporting\nerror_reporting = .*>;
http://php.net/error-reporting\nerror_reporting =
${app_php_global_log_level}>" ${file} && \  
perl -0p -i -e "s>; http://php.net/display-startup-
errors\ndisplay_startup_errors = .*>; http://php.net/display-startup-
errors\ndisplay_startup_errors = ${app_php_global_log_display}>" ${file} && \  
perl -0p -i -e "s>; http://php.net/display-errors\ndisplay_errors = .*>;
http://php.net/display-errors\ndisplay_errors =
${app_php_global_log_display}>" ${file} && \  
perl -0p -i -e "s>; http://php.net/log-errors\nlog_errors = .*>;
http://php.net/log-errors\nlog_errors = ${app_php_global_log_file}>" ${file}
&& \  
perl -0p -i -e "s>; http://php.net/log-errors-max-len\nlog_errors_max_len =
.*>; http://php.net/log-errors-max-len\nlog_errors_max_len = 10M>" ${file} &&
\  
perl -0p -i -e "s>; http://php.net/error-log\n>; http://php.net/error-
log\nerror_log = /proc/self/fd/2\n>" ${file} && \  
# change timeouts \  
perl -0p -i -e "s>; http://php.net/max-input-time\nmax_input_time = .*>;
http://php.net/max-input-time\nmax_input_time =
$((${app_php_global_limit_timeout}/2))>" ${file} && \  
perl -0p -i -e "s>; Note: This directive is hardcoded to 0 for the CLI
SAPI\nmax_execution_time = .*>; Note: This directive is hardcoded to 0 for the
CLI SAPI\nmax_execution_time = ${app_php_global_limit_timeout}>" ${file} && \  
# change memory limit \  
perl -0p -i -e "s>; http://php.net/memory-limit\nmemory_limit = .*>;
http://php.net/memory-limit\nmemory_limit =
$((${app_php_global_limit_memory}/1024/1024))M>" ${file} && \  
# change upload limit \  
perl -0p -i -e "s>; http://php.net/post-max-size\npost_max_size = .*>;
http://php.net/post-max-size\npost_max_size =
$((${app_php_global_limit_memory}*15/20/1024/1024))M>" ${file} && \  
perl -0p -i -e "s>; http://php.net/upload-max-filesize\nupload_max_filesize =
.*>; http://php.net/upload-max-filesize\nupload_max_filesize =
$((${app_php_global_limit_memory}/2/1024/1024))M>" ${file} && \  
# change i18n \  
perl -0p -i -e "s>; http://php.net/default-mimetype\ndefault_mimetype = .*>;
http://php.net/default-mimetype\ndefault_mimetype = \"text/html\">" ${file} &&
\  
perl -0p -i -e "s>; http://php.net/default-charset\ndefault_charset =.*>;
http://php.net/default-charset\ndefault_charset = \"UTF-8\">" ${file} && \  
perl -0p -i -e "s>; http://php.net/date.timezone\n;date.timezone =.*>;
http://php.net/date.timezone\ndate.timezone = \"UTC\">" ${file} && \  
# change CGI \  
perl -0p -i -e "s>; http://php.net/cgi.force-redirect\n;cgi.force_redirect =
.*>; http://php.net/cgi.force-redirect\ncgi.force_redirect = 1>" ${file} && \  
perl -0p -i -e "s>; http://php.net/cgi.fix-pathinfo\n;cgi.fix_pathinfo=.*>;
http://php.net/cgi.fix-pathinfo\ncgi.fix_pathinfo = 1>" ${file} && \  
perl -0p -i -e "s>; this feature.\n;fastcgi.logging = .*>; this
feature.\nfastcgi.logging = 1>" ${file} && \  
perl -0p -i -e "s>; http://php.net/cgi.rfc2616-headers\n;cgi.rfc2616_headers =
.*>; http://php.net/cgi.rfc2616-headers\ncgi.rfc2616_headers = 0>" ${file} &&
\  
printf "Done patching ${file}...\n" && \  
\  
# /etc/php5/fpm/php-fpm.conf \  
file="/etc/php5/fpm/php-fpm.conf" && \  
printf "\n# Applying configuration for ${file}...\n" && \  
# disable daemon/run in foreground \  
perl -0p -i -e "s>; Default Value: yes\n;daemonize = .*>; Default Value:
yes\ndaemonize = no>" ${file} && \  
# change logging \  
perl -0p -i -e "s>; Default Value: daemon\n;syslog.facility = .*>; Default
Value: daemon\nsyslog.facility = daemon>" ${file} && \  
perl -0p -i -e "s>; Default Value: php-fpm\n;syslog.ident = .*>; Default
Value: php-fpm\nsyslog.ident = php-fpm>" ${file} && \  
perl -0p -i -e "s>; Default Value: notice\n;log_level = .*>; Default Value:
notice\nlog_level = ${app_fpm_global_log_level}>" ${file} && \  
perl -0p -i -e "s>; Default Value: log/php-fpm.log\n.*error_log = .*>; Default
Value: log/php-fpm.log\nerror_log = /proc/self/fd/2>" ${file} && \  
# change maximum file open limit \  
perl -0p -i -e "s>; Default Value: system defined value\n;rlimit_files = .*>;
Default Value: system defined value\nrlimit_files =
${app_fpm_global_limit_descriptors}>" ${file} && \  
# change maximum processes \  
perl -0p -i -e "s>; Default Value: 0\n; process.max = .*>; Default Value:
0\nprocess.max = ${app_fpm_global_limit_processes}>" ${file} && \  
printf "Done patching ${file}...\n" && \  
\  
# PHP-FPM Pool \  
app_fpm_pool_home="${app_fpm_global_home}/${app_fpm_pool_id}" && \  
\  
# Rename original pool configuration \  
mv "/etc/php5/fpm/pool.d/www.conf" "/etc/php5/fpm/pool.d/www.conf.orig" && \  
\  
# /etc/php5/fpm/pool.d/${app_fpm_pool_id}.conf \  
file="/etc/php5/fpm/pool.d/${app_fpm_pool_id}.conf" && \  
cp "/etc/php5/fpm/pool.d/www.conf.orig" $file && \  
printf "\n# Applying configuration for ${file}...\n" && \  
# delete bad defaults \  
perl -0p -i -e "s>php_admin_flag\\[.*>>g" ${file} && \  
perl -0p -i -e "s>php_flag\\[.*>>g" ${file} && \  
perl -0p -i -e "s>php_admin_value\\[.*>>g" ${file} && \  
perl -0p -i -e "s>php_value\\[.*>>g" ${file} && \  
# rename pool \  
perl -0p -i -e "s>; pool name \\(\'www\' here\\)\n\\[www\\]>; pool name ('www'
here)\n[${app_fpm_pool_id}]>" ${file} && \  
# change pool prefix \  
perl -0p -i -e "s>; Default Value: none\n;prefix = .*>; Default Value:
none\nprefix = ${app_fpm_global_home}/\\\\\$pool>" ${file} && \  
# run as user/group \  
perl -0p -i -e "s>user = .*\ngroup = .*>user = ${app_fpm_pool_user}\ngroup =
${app_fpm_pool_group}>" ${file} && \  
# listen as user/group \  
perl -0p -i -e "s>listen.owner = .*\nlisten.group = .*\n;listen.mode =
.*>listen.owner = ${app_fpm_pool_user}\nlisten.group =
${app_fpm_pool_group}\nlisten.mode = 0660>" ${file} && \  
# change logging \  
printf "\n; Error log path\nphp_value[error_log] = /proc/self/fd/2\n" >>
${file} && \  
perl -0p -i -e "s>; Default: not set\n;access.log = .*>; Default: not
set\naccess.log = /proc/self/fd/2>" ${file} && \  
perl -0p -i -e "s>; Note: slowlog is mandatory if request_slowlog_timeout is
set\n;slowlog = .*>; Note: slowlog is mandatory if request_slowlog_timeout is
set\nslowlog = /proc/self/fd/2>" ${file} && \  
perl -0p -i -e "s>; Default Value: no\n;catch_workers_output = .*>; Default
Value: no\ncatch_workers_output = yes>" ${file} && \  
# change status \  
perl -0p -i -e "s>; Default Value: not set \n;pm.status_path = .*>; Default
Value: not set\npm.status_path = /phpfpm-status>" ${file} && \  
perl -0p -i -e "s>; Default Value: not set\n;ping.path = .*>; Default Value:
not set\nping.path = /phpfpm-ping>" ${file} && \  
perl -0p -i -e "s>; Default Value: pong\n;ping.response = .*>; Default Value:
pong\nping.response = pong>" ${file} && \  
# change whitelist \  
if [ ! -z "$app_fpm_pool_listen_wlist" ]; then perl -0p -i -e "s>; Default
Value: any\n;listen.allowed_clients = .*>; Default Value:
any\nlisten.allowed_clients = ${app_fpm_pool_listen_wlist}>" ${file}; else
perl -0p -i -e "s>; Default Value: any\n;listen.allowed_clients = .*>; Default
Value: any\n;listen.allowed_clients = 127.0.0.1>" ${file}; fi && \  
# change interface and port \  
perl -0p -i -e "s>; Note: This value is mandatory.\nlisten = .*>; Note: This
value is mandatory.\nlisten =
${app_fpm_pool_listen_addr}:${app_fpm_pool_listen_port}>" ${file} && \  
# change maximum file open limit \  
perl -0p -i -e "s>; Default Value: system defined value\n;rlimit_files = .*>;
Default Value: system defined value\nrlimit_files =
${app_fpm_pool_limit_descriptors}>" ${file};\  
# change backlog queue limit \  
perl -0p -i -e "s>; Default Value: 65535 \\(-1 on FreeBSD and
OpenBSD\\)\n;listen.backlog = .*>; Default Value: 65535 \\(-1 on FreeBSD and
OpenBSD\\)\nlisten.backlog = ${app_fpm_pool_limit_backlog}>" ${file} && \  
# change process manager \  
perl -0p -i -e "s>; Note: This value is mandatory.\npm = .*>; Note: This value
is mandatory.\npm = ${app_fpm_pool_pm_method}>" ${file} && \  
perl -0p -i -e "s>; Note: This value is mandatory.\npm.max_children = .*>;
Note: This value is mandatory.\npm.max_children =
${app_fpm_pool_pm_max_children}>" ${file} && \  
perl -0p -i -e "s>; Default Value: min_spare_servers \\+ \\(max_spare_servers
- min_spare_servers\\) / 2\npm.start_servers = .*>; Default Value:
min_spare_servers \\+ \\(max_spare_servers - min_spare_servers\\) /
2\npm.start_servers = ${app_fpm_pool_pm_start_servers}>" ${file} && \  
perl -0p -i -e "s>; Note: Mandatory when pm is set to
'dynamic'\npm.min_spare_servers = .*>; Note: Mandatory when pm is set to
'dynamic'\npm.min_spare_servers = ${app_fpm_pool_pm_min_spare_servers}>"
${file} && \  
perl -0p -i -e "s>; Note: Mandatory when pm is set to
'dynamic'\npm.max_spare_servers = .*>; Note: Mandatory when pm is set to
'dynamic'\npm.max_spare_servers = ${app_fpm_pool_pm_max_spare_servers}>"
${file} && \  
perl -0p -i -e "s>; Default Value: 10s\n;pm.process_idle_timeout = .*>;
Default Value: 10s\npm.process_idle_timeout =
${app_fpm_pool_pm_process_idle_timeout}>" ${file} && \  
perl -0p -i -e "s>; Default Value: 0\n;pm.max_requests = .*>; Default Value:
0\npm.max_requests = ${app_fpm_pool_pm_max_requests}>" ${file} && \  
# change timeouts \  
perl -0p -i -e "s>; Default Value: 0\n;request_slowlog_timeout = .*>; Default
Value: 0\nrequest_slowlog_timeout = $((${app_php_global_limit_timeout}+5))>"
${file} && \  
perl -0p -i -e "s>; Default Value: 0\n;request_terminate_timeout = .*>;
Default Value: 0\nrequest_terminate_timeout =
$((${app_php_global_limit_timeout}+10))>" ${file} && \  
# change chroot \  
perl -0p -i -e "s>; Default Value: not set\n;chroot = .*>; Default Value: not
set\n;chroot = ${app_fpm_pool_home}>" ${file} && \  
# change chdir \  
perl -0p -i -e "s>; Default Value: current directory or / when chroot\nchdir =
.*>; Default Value: current directory or / when chroot\n;chdir = /html/>"
${file} && \  
# change allowed extensions \  
perl -0p -i -e "s>; Default Value: .php\n;security.limit_extensions = .*>;
Default Value: .php\nsecurity.limit_extensions = .php>" ${file} && \  
# change temporary files \  
printf "\n; Temporary files path\nphp_value[upload_tmp_dir] =
${app_fpm_pool_home}/tmp\n" >> ${file} && \  
# change session \  
printf "\n; Session handler\nphp_value[session.save_handler] = files\n" >>
${file} && \  
printf "\n; Session path\nphp_value[session.save_path] =
${app_fpm_pool_home}/tmp\n" >> ${file} && \  
# change environment \  
perl -0p -i -e "s>; Default Value: clean env>; Default Value: clean env\n\n;
Main variables>" ${file} && \  
perl -0p -i -e "s>;env\\[HOSTNAME\\] = .*>env\\[HOSTNAME\\] = \\\\\$HOSTNAME>"
${file} && \  
perl -0p -i -e "s>;env\\[PATH\\] = .*>env\\[PATH\\] = \\\\\$PATH>" ${file} &&
\  
perl -0p -i -e "s>;env\\[TMP\\] = .*>env\\[TMP\\] = ${app_fpm_pool_home}/tmp>"
${file} && \  
perl -0p -i -e "s>;env\\[TMPDIR\\] = .*>env\\[TMPDIR\\] =
${app_fpm_pool_home}/tmp>" ${file} && \  
perl -0p -i -e "s>;env\\[TEMP\\] = .*>env\\[TEMP\\] =
${app_fpm_pool_home}/tmp>" ${file} && \  
perl -0p -i -e "s>; Additional php.ini defines, specific to this pool of
workers>; Proxy variables\n\n; Additional php.ini defines, specific to this
pool of workers>" ${file} && \  
perl -0p -i -e "s>; Proxy variables\n>; Proxy variables\nenv\\[ftp_proxy\\] =
\\\\\$ftp_proxy\n>" ${file} && \  
perl -0p -i -e "s>; Proxy variables\n>; Proxy variables\nenv\\[https_proxy\\]
= \\\\\$https_proxy\n>" ${file} && \  
perl -0p -i -e "s>; Proxy variables\n>; Proxy variables\nenv\\[http_proxy\\] =
\\\\\$http_proxy\n>" ${file} && \  
printf "Done patching ${file}...\n" && \  
\  
# ${app_fpm_pool_home}/test-fpm.sh \  
file="${app_fpm_pool_home}/test-fpm.sh" && \  
printf "\n# Writing test for php-fpm...\n" && \  
printf "\n\  
# https://easyengine.io/tutorials/php/directly-connect-php-fpm/\n\  
SCRIPT_NAME=/phpfpm-status SCRIPT_FILENAME=/phpfpm-status REQUEST_METHOD=GET
cgi-fcgi -bind -connect 127.0.0.1:${app_fpm_pool_listen_port}\n\  
"> ${file} && \  
chmod +x ${file} && \  
printf "Done writing ${file}...\n" && \  
\  
printf "\n# Testing configuration...\n" && \  
echo "Testing $(which ab):"; $(which ab) -V && \  
echo "Testing $(which mysql):"; $(which mysql) -V && \  
echo "Testing $(which redis-cli):"; $(which redis-cli) -v && \  
echo "Testing $(which php):"; $(which php) -v; $(which php) --ini && \  
echo "Testing $(which php5-fpm):"; $(which php5-fpm) -v; $(which php5-fpm)
--test && \  
echo "Testing $(which composer):"; $(which composer) --version && \  
echo "Testing $(which drush):"; $(which drush) core-status && \  
printf "Done testing configuration...\n" && \  
\  
printf "Finished updading PHP and PHP-FPM configuration...\n";  
  
#  
# Demo  
#  
RUN printf "Preparing demo...\n" && \  
# PHP-FPM Pool \  
app_fpm_pool_home="${app_fpm_global_home}/${app_fpm_pool_id}" && \  
\  
# ${app_fpm_pool_home}/html/index.php \  
file="${app_fpm_pool_home}/html/index.php" && \  
printf "\n# Adding demo file ${file}...\n" && \  
printf "<?php\n\  
echo \"Hello World!\";\n\  
\n" > ${file} && \  
printf "Done patching ${file}...\n" && \  
\  
# ${app_fpm_pool_home}/html/phpinfo.php \  
file="${app_fpm_pool_home}/html/phpinfo.php" && \  
printf "\n# Adding demo file ${file}...\n" && \  
printf "<?php\n\  
phpinfo();\n\  
\n" > ${file} && \  
printf "Done patching ${file}...\n";  
  
#  
# Run  
#  
# Command to execute  
# Defaults to /bin/bash.  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf", "--
nodaemon"]  
  
# Ports to expose  
# Defaults to 9000  
EXPOSE ${app_fpm_pool_listen_port}  
  

