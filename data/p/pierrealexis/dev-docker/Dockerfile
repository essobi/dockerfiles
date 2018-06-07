FROM debian:stretch  
MAINTAINER Pierre-Alexis de Solminihac <pa@solminihac.fr>  
  
#####################  
# ENABLE REPOSITORIES  
#####################  
# enable more packages  
RUN sed -i 's/main/main contrib non-free/g' /etc/apt/sources.list  
  
# choose a faster mirror  
#COPY sources.list /etc/apt/sources.list  
ENV DEBIAN_FRONTEND=noninteractive  
  
# enable docker repository for docker-in-docker  
RUN apt-get update  
RUN apt-get -y install apt-transport-https ca-certificates gnupg curl  
# try with multiple keyservers because some may be unavailable  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D || \  
apt-key adv --keyserver pgp.mit.edu --recv-keys
58118E89F3A912897C070ADBF76221572C52609D || \  
apt-key adv --keyserver keyserver.pgp.com --recv-keys
58118E89F3A912897C070ADBF76221572C52609D || \  
apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
58118E89F3A912897C070ADBF76221572C52609D  
RUN echo "deb https://apt.dockerproject.org/repo debian-stretch main" >
/etc/apt/sources.list.d/docker.list  
  
# enable blackfire.io additional repository  
ADD https://packagecloud.io/gpg.key /tmp/blackfire.key  
RUN apt-key add /tmp/blackfire.key && \  
echo "deb http://packages.blackfire.io/debian any main" | tee
/etc/apt/sources.list.d/blackfire.list  
  
# enable elasticsearch logstash kibana additional repository  
ADD https://artifacts.elastic.co/GPG-KEY-elasticsearch /tmp/elasticsearch.key  
RUN apt-key add /tmp/elasticsearch.key && \  
echo "deb https://artifacts.elastic.co/packages/5.x/apt stable main" | tee -a
/etc/apt/sources.list.d/elastic-5.x.list  
  
# enable debian stretch backports  
RUN echo "deb http://httpredir.debian.org/debian stretch-backports main" | tee
/etc/apt/sources.list.d/backports.list  
  
# enable dotdeb repository for php7  
#ADD https://www.dotdeb.org/dotdeb.gpg /tmp/dotdeb.key  
#RUN apt-key add /tmp/dotdeb.key && \  
# echo "deb http://packages.dotdeb.org stretch all" | tee
/etc/apt/sources.list.d/dotdeb.list  
# enable nodejs repository  
WORKDIR /usr/local/src/  
RUN curl -sL https://deb.nodesource.com/setup_6.x -o setup_6.x && \  
chmod +x setup_6.x && \  
./setup_6.x # includes apt-get update  
  
#########################  
# INSTALL DISTRO PACKAGES  
#########################  
#RUN apt-get update # included in setup_6.x script running just before  
RUN apt-get -y install \  
apt-utils \  
lsb-release \  
screen \  
dialog \  
locales-all \  
net-tools dnsutils whois strace \  
sudo \  
memcached  
  
RUN echo "LANG=en_US.UTF-8" > /etc/default/locale && \  
echo "LANGUAGE=en_GB:en" >> /etc/default/locale  
  
RUN apt-get -y install \  
apache2 \  
libapache2-mod-php \  
php-apcu \  
php-mcrypt \  
php-memcached \  
redis-server php-redis \  
php-intl \  
php-mysqlnd \  
php-pgsql \  
php-json \  
php-xsl \  
php-imap \  
php-curl \  
php-gd \  
php-imagick \  
gettext php-gettext \  
php-oauth \  
php-pspell \  
php-ssh2 \  
php-ldap \  
php-sqlite3 \  
php-pear \  
phpunit php-xdebug  
  
RUN apt-get -y install \  
poppler-utils tesseract-ocr tesseract-ocr-eng tesseract-ocr-fra bc \  
bash bash-completion \  
pv \  
ncdu ncurses-bin \  
vim nano \  
grep ack-grep silversearcher-ag \  
git tig \  
openssh-server openssh-client rsync \  
lynx wget netcat tor whatweb \  
phpmyadmin \  
man-db manpages manpages-fr manpages-fr-extra \  
blackfire-agent blackfire-php \  
mailutils \  
mariadb-server \  
mysql-utilities \  
mariadb-client # includes mytop  
  
RUN apt-get -y install \  
build-essential autoconf pkg-config nasm libtool \  
rsyslog \  
imagemagick \  
ssl-cert \  
unzip unrar-free p7zip-full \  
trash-cli \  
lftp \  
youtube-dl \  
libimage-exiftool-perl \  
varnish \  
ttf-mscorefonts-installer \  
tcpdump \  
tcpflow \  
spfquery  
  
RUN apt-get -y install docker-engine  
  
# decent nodejs version and gulp  
RUN apt-get -y install nodejs build-essential libssl-dev  
RUN npm install -g n gulp  
RUN n stable  
  
# TODO: more tools (http://agile.dzone.com/news/continuous-integration-php  
# install libreoffice from backports  
RUN apt-get -y install -t stretch-backports openjdk-8-jre-headless ca-
certificates-java && \  
update-alternatives --set java /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java  
RUN apt-get -y install -t stretch-backports libreoffice-writer jodconverter  
  
# install letsencrypt from backports  
RUN apt-get -y install -t stretch-backports python-certbot-apache  
  
# install mycli  
RUN easy_install3 mycli  
  
# install elasticsearch logstash kibana  
ENV ES_SKIP_SET_KERNEL_PARAMETERS=true  
RUN apt-get -y install elasticsearch logstash kibana  
  
# image optimisation tools  
RUN apt-get -y install jpegoptim gifsicle optipng pngquant  
  
#################################  
# WORKAROUND for write permission  
#################################  
# See https://github.com/boot2docker/boot2docker/pull/534  
ENV USER_ID=9999 GROUP_ID=9999  
RUN addgroup devdocker --gid $GROUP_ID && \  
adduser --disabled-login --gecos "devdocker" devdocker --uid $USER_ID \--gid
$GROUP_ID && \  
echo "devdocker ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/devdocker && \  
chmod 440 /etc/sudoers.d/devdocker  
  
##########################  
# INSTALL WITHOUT PACKAGES  
##########################  
# composer  
WORKDIR /usr/local/bin  
RUN curl -s "https://getcomposer.org/installer" | php && mv composer.phar
/usr/local/bin/composer  
  
ARG CACHEBUST=1  
# install wp-cli  
WORKDIR /usr/local/bin  
RUN curl -O "https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar" && \  
chmod +x wp-cli.phar && \  
mv wp-cli.phar wp  
  
# install drush  
WORKDIR /usr/local/src/  
RUN git clone https://github.com/drush-ops/drush.git /usr/local/src/drush && \  
cd drush && ln -s /usr/local/src/drush/drush /usr/local/bin/drush && composer
install  
  
# install php beautifiers  
WORKDIR /usr/local/bin  
RUN wget http://get.sensiolabs.org/php-cs-fixer.phar -O php-cs-fixer && \  
chmod a+x php-cs-fixer && \  
pear install PHP_Beautifier-0.1.15 && \  
git clone https://github.com/pa-de-solminihac/php-auto-indent.git
/usr/local/src/php-auto-indent && \  
chmod a+x /usr/local/src/php-auto-indent && \  
ln -s /usr/local/src/php-auto-indent/php-auto-indent /usr/local/bin  
  
# install cdiff  
WORKDIR /usr/local/src/  
RUN git clone https://github.com/ymattw/cdiff.git && \  
cd cdiff && \  
./setup.py install  
  
# install sitesync  
WORKDIR /usr/local/src/  
RUN git clone https://github.com/pa-de-solminihac/sitesync.git /sitesync && \  
chmod -R 777 /sitesync/tmp && \  
chmod -R 777 /sitesync/log  
COPY profile.d_sitesync.sh /etc/profile.d/sitesync.sh  
  
# # install php code analysis tools  
# WORKDIR /usr/local/bin/  
# RUN git wget http://static.pdepend.org/php/latest/pdepend.phar && \  
# chmod ugo+x /usr/local/bin/pdepend.phar && \  
# mv /usr/local/bin/pdepend.phar /usr/local/bin/pdepend  
# configure elasticsearch and kibana, then install metricbeat (for container
monitoring in elasticsearch logstash kibana) and elasticsearch plugin ingest-
attachment to index files using Apache Tika  
RUN sed -i 's/-Xms2g/-Xms512m/g' /etc/elasticsearch/jvm.options && \  
sed -i 's/-Xmx2g/-Xmx512m/g' /etc/elasticsearch/jvm.options && \  
sed -i 's/#network.host: 192.168.0.1/network.host: 0.0.0.0/g'
/etc/elasticsearch/elasticsearch.yml && \  
sed -i 's/#server.host: "localhost"/server.host: "0.0.0.0"/g'
/etc/kibana/kibana.yml && \  
mkdir -p /usr/local/src/metricbeat && \  
cd /usr/local/src/metricbeat && \  
curl -L -O
https://artifacts.elastic.co/downloads/beats/metricbeat/metricbeat-5.0.0-amd64.deb
&& \  
dpkg -i metricbeat-5.0.0-amd64.deb && \  
cd /usr/share/elasticsearch && \  
bin/elasticsearch-plugin install -b ingest-attachment  
  
# configure redis-server to allow remote access  
RUN sed -i -e 's/^bind /#bind /' '/etc/redis/redis.conf'  
  
# better shell config  
WORKDIR /root/  
RUN [ ! -d ".config" ] && mkdir .config && chmod 700 .config  
RUN git clone https://github.com/pa-de-solminihac/configuration.git
/root/.config/config-pa-de-solminihac && \  
echo "source /root/.bashrc_common" >> /root/.bashrc && \  
ln -s /root/.config/config-pa-de-solminihac/bash/.bashrc_common && \  
echo "source /root/.vimrc_common" >> /root/.vimrc && \  
ln -s /root/.config/config-pa-de-solminihac/vim/.vimrc_common && \  
mkdir -p bin && \  
ln -s /root/.config/config-pa-de-solminihac/bin/diffconflicts bin/  
WORKDIR /home/devdocker/  
RUN sudo -u devdocker bash -c '[ ! -d ".config" ] && mkdir .config && chmod
700 .config'  
RUN sudo -u devdocker bash -c 'git clone https://github.com/pa-de-
solminihac/configuration.git ~/.config/config-pa-de-solminihac' && \  
sudo -u devdocker bash -c 'echo "source ~/.bashrc_common" >> ~/.bashrc && ln
-s ~/.config/config-pa-de-solminihac/bash/.bashrc_common ~/.bashrc_common' &&
\  
sudo -u devdocker bash -c 'echo "source ~/.vimrc_common" >> ~/.vimrc && ln -s
~/.config/config-pa-de-solminihac/vim/.vimrc_common ~/.vimrc_common' && \  
sudo -u devdocker bash -c 'mkdir -p bin && ln -s ~/.config/config-pa-de-
solminihac/bin/diffconflicts ~/bin/'  
  
###########  
# CONFIGURE  
###########  
# timezone  
ENV TZ=Europe/Paris  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
# logs directory  
RUN mkdir -p /var/log/dockersite && \  
chmod 777 /var/log/dockersite  
  
# configure git  
COPY gitconfig /home/devdocker/.gitconfig  
  
# configure blackfire  
COPY blackfire-agent /etc/blackfire/agent  
COPY blackfire-client /home/devdocker/.blackfire.ini  
  
# apache  
COPY 000-default.conf /etc/apache2/sites-enabled/  
RUN make-ssl-cert generate-default-snakeoil  
RUN a2enmod rewrite && \  
a2enmod headers && \  
a2enmod http2 && \  
a2enmod proxy && \  
a2enmod proxy_http && \  
a2enmod expires && \  
a2enmod include && \  
a2enmod ssl && \  
a2enmod vhost_alias && \  
echo 'ServerName localhost' >> /etc/apache2/apache2.conf && \  
sed -i 's/AllowOverride None/AllowOverride All/g' /etc/apache2/apache2.conf &&
\  
sed -i 's/export APACHE_LOG_DIR=.*/export
APACHE_LOG_DIR=\/var\/log\/dockersite$SUFFIX/g' /etc/apache2/envvars && \  
sed -i 's@#. /etc/default/locale@. /etc/default/locale@g' /etc/apache2/envvars
&& \  
sed -i 's/Listen 80/Listen 0.0.0.0:80/g' /etc/apache2/ports.conf && \  
sed -i 's/Listen 443/Listen 0.0.0.0:443/g' /etc/apache2/ports.conf && \  
sed -i 's/CustomLog ${APACHE_LOG_DIR}\/access.log combined/CustomLog
${APACHE_LOG_DIR}\/access.log dockersite/g' /etc/apache2/sites-
available/000-default.conf && \  
sed -i 's/CustomLog ${APACHE_LOG_DIR}\/access.log combined/CustomLog
${APACHE_LOG_DIR}\/access.log dockersite/g' /etc/apache2/sites-
available/default-ssl.conf && \  
mkdir -p /etc/apache2/dockersite && \  
echo 'LogFormat "%V:%p %h %l %u %t \"%r\" %>s %O \"%{Referer}i\" \"%{User-
Agent}i\"" dockersite' >> /etc/apache2/apache2.conf && \  
echo 'Protocols h2 h2c http/1.1' >> /etc/apache2/apache2.conf && \  
echo 'IncludeOptional dockersite/*.conf' >> /etc/apache2/apache2.conf  
  
# mod_security  
#RUN apt-get -y install libapache2-mod-security2 \  
# a2enmod security2 && \  
# cp /etc/modsecurity/modsecurity.conf-recommended
/etc/modsecurity/modsecurity.conf && \  
# sed -i 's/SecRuleEngine DetectionOnly/SecRuleEngine On/g'
/etc/modsecurity/modsecurity.conf  
# apache: workaround for write permission  
RUN sed -i "s/export APACHE_RUN_USER=www-data/export
APACHE_RUN_USER=devdocker/g" /etc/apache2/envvars && \  
sed -i "s/export APACHE_RUN_GROUP=www-data/export
APACHE_RUN_GROUP=devdocker/g" /etc/apache2/envvars && \  
chgrp devdocker /var/lib/phpmyadmin/* /etc/phpmyadmin/config-db.php
/etc/phpmyadmin/htpasswd.setup  
  
# php: xdebug is used for phpunit code coverage, but slows down PHP so we
disable it in for apache2 SAPI  
RUN sed -i "s/^display_errors = Off/display_errors = On/g"
/etc/php/7.0/apache2/php.ini && \  
sed -i "s/^track_errors = Off/track_errors = On/g"
/etc/php/7.0/apache2/php.ini && \  
sed -i "s/^;error_log = php_errors.log/error_log =
\/var\/log\/dockersite\/php_errors.log/g" /etc/php/7.0/apache2/php.ini && \  
sed -i "s/^disable_functions =.*/disable_functions = shell-exec, system,
passthru, popen/g" /etc/php/7.0/apache2/php.ini && \  
sed -i "s/^; max_input_vars =.*/max_input_vars = 2000/g"
/etc/php/7.0/apache2/php.ini && \  
sed -i "s/^post_max_size =.*/post_max_size = 32M/g"
/etc/php/7.0/apache2/php.ini && \  
sed -i "s/^upload_max_filesize =.*/upload_max_filesize = 32M/g"
/etc/php/7.0/apache2/php.ini && \  
sed -i "s/^;date\\.timezone =.*/date.timezone = 'Europe\/Paris'/g"
/etc/php/7.0/apache2/php.ini && \  
phpdismod -s ALL xdebug  
  
# phpmyadmin  
RUN echo "Include /etc/phpmyadmin/apache.conf" >> /etc/apache2/apache2.conf &&
\  
sed -i 's/ \/\/ $cfg\\['\''Servers'\''\\]\\[$i\\]\\['\''AllowNoPassword'\''\\]
= TRUE/ $cfg\\['\''Servers'\''\\]\\[$i\\]\\['\''AllowNoPassword'\''\\] =
TRUE/g' /etc/phpmyadmin/config.inc.php && \  
sed -i "s/^\$dbuser='phpmyadmin';/\$dbuser='root';/g" /etc/phpmyadmin/config-
db.php && \  
sed -i "s/^\$dbpass='.*';/\$dbpass='MYSQL_FORCED_ROOT_PASSWORD';/g"
/etc/phpmyadmin/config-db.php && \  
echo '<?php' > /etc/phpmyadmin/conf.d/devdocker.php && \  
echo '$cfg["MaxNavigationItems"] = 500;' >>
/etc/phpmyadmin/conf.d/devdocker.php && \  
echo '$sessionDuration = 60*60*24*7; // 60*60*24*7 = one week' >>
/etc/phpmyadmin/conf.d/devdocker.php && \  
echo 'ini_set("session.gc_maxlifetime", $sessionDuration);' >>
/etc/phpmyadmin/conf.d/devdocker.php && \  
echo '$cfg["LoginCookieValidity"] = $sessionDuration;' >>
/etc/phpmyadmin/conf.d/devdocker.php && \  
echo '$cfg["LoginCookieStore"] = $sessionDuration;' >>
/etc/phpmyadmin/conf.d/devdocker.php  
  
# mysql: enable cache for performance, set charset to utf8, enable binlogs for
point in time recovery, allow startup even when corrupt innodb tables are
found  
RUN sed -i "s/^bind-address.*/bind-address = 0.0.0.0/g"
/etc/mysql/mariadb.conf.d/50-server.cnf && \  
sed -i "s/^user[[:space:]]*=[[:space:]]*mysql/user = devdocker/g"
/etc/mysql/mariadb.conf.d/50-server.cnf && \  
sed -i "s/^query_cache_limit.*/slow_query_log = 1\nslow_query_log_file =
\/var\/log\/dockersite\/mysql-slow.log\nlong_query_time = 2/g"
/etc/mysql/mariadb.conf.d/50-server.cnf && \  
sed -i "s/^query_cache_size.*/query_cache_type = 1\nquery_cache_limit =
16M\nquery_cache_size = 256M\nopen_files_limit = 9999\ninnodb_buffer_pool_size
= 32M\nmax_allowed_packet = 32M\ninnodb_log_file_size = 32M\n/g"
/etc/mysql/mariadb.conf.d/50-server.cnf && \  
sed -i "s/^#log_bin[[:space:]]*=.*/log_bin = \/var\/lib\/mysql\/binlog\/mysql-
bin.log/g" /etc/mysql/mariadb.conf.d/50-server.cnf && \  
sed -i "s/^character-set-server = utf8mb4/\ncharacter-set-server = utf8/g"
/etc/mysql/mariadb.conf.d/50-server.cnf && \  
sed -i "s/^collation-server = utf8mb4_general_ci/collation-server =
utf8_general_ci/g" /etc/mysql/mariadb.conf.d/50-server.cnf && \  
sed -i "s/^default-character-set = utf8mb4/default-character-set = utf8/g"
/etc/mysql/mariadb.conf.d/50-client.cnf  
COPY perfs.cnf /etc/mysql/conf.d/  
  
# config mail server so websites can send emails (outgoing mails are caught in
run.sh)  
RUN sed -i
"s/^dc_eximconfig_configtype='local'/dc_eximconfig_configtype='internet'/g"
/etc/exim4/update-exim4.conf.conf && \  
sed -i "s/^dc_local_interfaces=.*/dc_local_interfaces='127.0.0.1'/g"
/etc/exim4/update-exim4.conf.conf && \  
update-exim4.conf  
  
# ssh  
RUN sed -i "s/^#Port 22/Port 8022/g" /etc/ssh/sshd_config && \  
sed -i "s/^#PermitRootLogin prohibit-password/PermitRootLogin yes/g"
/etc/ssh/sshd_config  
# copy your *readonly* mounted ssh keys and config everytime you login  
COPY copy-ssh-config.sh /  
RUN mkdir -p /root/.ssh && chmod 700 /root/.ssh  
RUN mkdir -p /home/devdocker/.ssh && chmod 700 /home/devdocker/.ssh  
  
# varnish  
RUN /bin/cp -a /lib/systemd/system/varnish.service /etc/systemd/system  
COPY varnish/varnish.service /etc/systemd/system/varnish.service  
COPY varnish/reload-vcl.sh /etc/varnish/reload-vcl.sh  
COPY varnish/prestashop.vcl /etc/varnish/default.vcl  
RUN chmod 700 /etc/varnish/reload-vcl.sh  
  
# allow docker to run without sudo  
RUN gpasswd -a devdocker docker  
  
# cleanup  
RUN apt-get -y clean  
  
# fix docker exec -t  
RUN echo 'if [ "$TERM" == "dumb" ]; then ' >> /home/devdocker/.bashrc && \  
echo ' export TERM=xterm' >> /home/devdocker/.bashrc && \  
echo 'fi' >> /home/devdocker/.bashrc  
  
# cd /var/www/html at startup  
RUN echo 'cd /var/www/html' >> /home/devdocker/.bashrc  
  
# longer log messages  
RUN echo '$MaxMessageSize 20k' > /etc/rsyslog.d/devdocker.conf  
  
# source custom bashrc file at startup  
RUN echo "for f in \$(find /home/devdocker/bashrc.d -maxdepth 1 -type f -name
'*.sh'); do source \$f; done" >> /home/devdocker/.bashrc  
  
RUN echo '' > /etc/motd  
  
RUN echo devdocker:devdocker | chpasswd  
  
# ProFtpd  
RUN apt -y install proftpd \  
&& sed -i 's/# AuthOrder.*/AuthOrder mod_auth_file.c
mod_auth_unix.c\nAuthUserFile \/etc\/proftpd\/passwd\/ftpd.passwd/g'
/etc/proftpd/proftpd.conf \  
&& sed -i 's/# PassivePorts.*/PassivePorts 7000 7003/g'
/etc/proftpd/proftpd.conf \  
&& sed -i 's/User[[:space:]].*/User devdocker/g' /etc/proftpd/proftpd.conf \  
&& sed -i 's/Group[[:space:]].*/Group devdocker/g' /etc/proftpd/proftpd.conf \  
&& sed -i 's/UseIPv6.*/UseIPv6 off/g' /etc/proftpd/proftpd.conf \  
&& sed -i 's/# DefaultRoot.*/DefaultRoot ~/g' /etc/proftpd/proftpd.conf \  
&& touch /etc/proftpd/ftpd.passwd \  
&& chmod 600 /etc/proftpd/ftpd.passwd  
  
# expose ports  
EXPOSE 8022 20 21 80 443 3306 5601 6379 6081 6082 9200 9300 11211 7000-7003  
# caution: CMD works ok with double quotes (") but not with single quotes (')  
COPY run.sh /run.sh  
RUN chmod 755 /run.sh  
CMD ["/run.sh"]  

