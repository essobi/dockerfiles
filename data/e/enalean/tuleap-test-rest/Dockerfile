FROM centos:6  
  
COPY Tuleap.repo /etc/yum.repos.d/  
  
RUN yum -y install epel-release centos-release-scl && \  
yum -y --exclude php-pecl-apcu install \  
tuleap \  
rh-mysql56-mysql \  
rh-mysql56-mysql-server \  
php-restler-3.0-0.7.1 \  
php-phpwiki-tuleap \  
php-ZendFramework2-Mail \  
libnss-mysql \  
rh-php56-php-gd \  
rh-php56-php-pecl \  
rh-php56-php-pear \  
rh-php56-php-soap \  
rh-php56-php-mysqlnd \  
rh-php56-php-xml \  
rh-php56-php-mbstring \  
rh-php56-php-cli \  
rh-php56-php-opcache \  
rh-php56-php-process \  
rh-php56-php-pdo \  
rh-php56-php-fpm \  
httpd24-httpd \  
java-1.8.0-openjdk \  
rh-php70-php-cli \  
rh-php70-php-pdo \  
rh-php70-php-xml \  
rh-php70-php-mbstring \  
rh-php70-php-mysqlnd \  
sudo \  
&& \  
yum remove -y tuleap \  
tuleap-core-subversion \  
tuleap-core-subversion-modperl \  
tuleap-documentation && \  
yum --disablerepo=Tuleap install -y git19-git rh-git29-git && \  
yum clean all  
  
COPY libnss-mysql-root.cfg libnss-mysql.cfg /etc/  
  
RUN sed -i -e 's/^passwd\\(.*\\)/passwd\1 mysql/g' \  
-e 's/^shadow\\(.*\\)/shadow\1 mysql/g' \  
-e 's/^group\\(.*\\)/group\1 mysql/g' /etc/nsswitch.conf && \  
curl -k -sS https://getcomposer.org/installer | /opt/rh/rh-
php70/root/usr/bin/php && mv composer.phar /usr/local/bin && \  
touch /etc/aliases.codendi && \  
mkdir -p /etc/tuleap/conf \  
/etc/tuleap/plugins \  
/var/tmp/tuleap_cache/lang \  
/var/tmp/tuleap_cache/combined \  
/var/tmp/tuleap_cache/restler \  
/var/lib/tuleap/gitolite/admin \  
/var/log/tuleap \  
/usr/lib/tuleap/bin \  
/home/users \  
/home/groups \  
/var/lib/tuleap/ftp/pub \  
/var/lib/tuleap/ftp/incoming \  
/var/lib/tuleap/ftp/tuleap && \  
chown -R codendiadm:codendiadm /etc/tuleap \  
/var/tmp/tuleap_cache \  
/var/lib/tuleap \  
/var/log/tuleap && \  
cd /usr/share && ln -s tuleap codendi && \  
cd /var/tmp && ln -s tuleap_cache codendi_cache  
  
COPY mysql-server.cnf /etc/opt/rh/rh-mysql56/my.cnf.d/mysql-server.cnf  
  
RUN service rh-mysql56-mysqld start && service rh-mysql56-mysqld stop  
  
CMD /usr/share/tuleap/tests/rest/bin/run.sh  
  
ENV MYSQL_DAEMON=rh-mysql56-mysqld  
ENV FPM_DAEMON=rh-php56-php-fpm  
ENV HTTPD_DAEMON=httpd24-httpd  

