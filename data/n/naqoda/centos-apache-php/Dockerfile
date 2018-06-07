#
=============================================================================  
# naqoda/centos-apache-php  
#  
# CentOS-7, Apache 2.4, PHP 7.1, Ioncube, MYSQL  
#  
#
=============================================================================  
FROM centos:centos7  
  
MAINTAINER Naqoda <info@naqoda.com>  
  
ARG uid=1000  
ARG gid=1000  
#
-----------------------------------------------------------------------------  
# Import the RPM GPG keys for Repositories  
#
-----------------------------------------------------------------------------  
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm \  
&& rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm  
  
#
-----------------------------------------------------------------------------  
# Apache + PHP  
#
-----------------------------------------------------------------------------  
RUN yum -y update \  
&& yum --setopt=tsflags=nodocs -y install \  
gcc \  
gcc-c++ \  
httpd \  
mod_ssl \  
php71w \  
php71w-cli \  
php71w-devel \  
php71w-mysql \  
php71w-pdo \  
php71w-mbstring \  
php71w-soap \  
php71w-gd \  
php71w-xml \  
php71w-pecl-apcu \  
unzip \  
libXrender fontconfig libXext urw-fonts \  
ImageMagick ImageMagick-devel \  
&& rm -rf /var/cache/yum/* \  
&& yum clean all  
  
#
-----------------------------------------------------------------------------  
# UTC Timezone & Networking  
#
-----------------------------------------------------------------------------  
RUN ln -sf /usr/share/zoneinfo/UTC /etc/localtime \  
&& echo "NETWORKING=yes" > /etc/sysconfig/network  
  
#
-----------------------------------------------------------------------------  
# Install DB2 PDO driver  
#
-----------------------------------------------------------------------------  
#ENV DB2EXPRESSC_URL https://s3-ap-
southeast-1.amazonaws.com/naqoda/downloads/ibm_data_server_driver_package_linuxx64_v10.5.tar.gz  
#ENV IBM_DB_HOME /opt/ibm/dsdriver  
#ENV LD_LIBRARY_PATH
/opt/ibm/dsdriver/odbc_cli_driver/linuxamd64/clidriver/lib  
#RUN mkdir /opt/ibm \  
# && curl -fSLo /opt/ibm/expc.tar.gz $DB2EXPRESSC_URL \  
# && cd /opt/ibm && tar xf expc.tar.gz \  
# && rm /opt/ibm/expc.tar.gz \  
# && cp $IBM_DB_HOME/php_driver/linuxamd64/php64/ibm_db2_5.3.6_nts.so
/usr/lib64/php/modules/ibm_db2.so \  
# && cp $IBM_DB_HOME/php_driver/linuxamd64/php64/pdo_ibm_5.3.6_nts.so
/usr/lib64/php/modules/pdo_ibm.so \  
# && cd /opt/ibm/dsdriver/odbc_cli_driver/linuxamd64 \  
# && tar xf ibm_data_server_driver_for_odbc_cli.tar.gz \  
# && echo 'extension=ibm_db2.so' > /etc/php.d/pdo_db2.ini \  
# && echo 'extension=pdo_ibm.so' >> /etc/php.d/pdo_db2.ini  
#COPY modules/php71/* /usr/lib64/php/modules/  
#
-----------------------------------------------------------------------------  
# Build Kafka PHP extension  
#
-----------------------------------------------------------------------------  
#RUN curl -fSLo /tmp/librdkafka-master.zip
https://github.com/edenhill/librdkafka/archive/master.zip \  
# && cd /tmp \  
# && unzip librdkafka-master.zip \  
# && cd librdkafka-master \  
# && ./configure \  
# && make \  
# && make install  
#RUN pecl install channel://pecl.php.net/rdkafka-2.0.0 \  
# && echo 'extension=rdkafka.so' > /etc/php.d/kafka.ini  
#
-----------------------------------------------------------------------------  
# Global Apache configuration changes  
# Disable Apache directory indexes  
# Disable Apache language based content negotiation  
# Disable all Apache modules and enable the minimum  
# Enable ServerStatus access via /_httpdstatus to local client  
# Apache tuning  
#
-----------------------------------------------------------------------------  
RUN sed -i \  
-e 's~^ServerSignature On$~ServerSignature Off~g' \  
-e 's~^ServerTokens OS$~ServerTokens Prod~g' \  
-e 's~^DirectoryIndex \\(.*\\)$~DirectoryIndex \1 index.php~g' \  
-e 's~^Group apache$~Group app~g' \  
-e 's~^IndexOptions \\(.*\\)$~#IndexOptions \1~g' \  
-e 's~^IndexIgnore \\(.*\\)$~#IndexIgnore \1~g' \  
-e 's~^AddIconByEncoding \\(.*\\)$~#AddIconByEncoding \1~g' \  
-e 's~^AddIconByType \\(.*\\)$~#AddIconByType \1~g' \  
-e 's~^AddIcon \\(.*\\)$~#AddIcon \1~g' \  
-e 's~^DefaultIcon \\(.*\\)$~#DefaultIcon \1~g' \  
-e 's~^ReadmeName \\(.*\\)$~#ReadmeName \1~g' \  
-e 's~^HeaderName \\(.*\\)$~#HeaderName \1~g' \  
-e 's~^LanguagePriority \\(.*\\)$~#LanguagePriority \1~g' \  
-e 's~^ForceLanguagePriority \\(.*\\)$~#ForceLanguagePriority \1~g' \  
-e 's~^AddLanguage \\(.*\\)$~#AddLanguage \1~g' \  
-e '/#<Location \/server-status>/,/#<\/Location>/ s~^#~~' \  
-e '/<Location \/server-status>/,/<\/Location>/ s~Allow from .example.com~Allow from localhost 127.0.0.1~' \  
-e 's~^StartServers \\(.*\\)$~StartServers 3~g' \  
-e 's~^MinSpareServers \\(.*\\)$~MinSpareServers 3~g' \  
-e 's~^MaxSpareServers \\(.*\\)$~MaxSpareServers 3~g' \  
-e 's~^ServerLimit \\(.*\\)$~ServerLimit 10~g' \  
-e 's~^MaxClients \\(.*\\)$~MaxClients 10~g' \  
-e 's~^MaxRequestsPerChild \\(.*\\)$~MaxRequestsPerChild 1000~g' \  
/etc/httpd/conf/httpd.conf  
  
RUN sed -i \  
-e 's~^\\(LoadModule .*\\)$~#\1~g' \  
/etc/httpd/conf.modules.d/00-dav.conf  
  
RUN sed -i \  
-e 's~^\\(LoadModule .*\\)$~#\1~g' \  
/etc/httpd/conf.modules.d/00-lua.conf  
  
RUN sed -i \  
-e 's~^\\(LoadModule .*\\)$~#\1~g' \  
/etc/httpd/conf.modules.d/00-proxy.conf  
  
RUN sed -i \  
-e 's~^LoadModule suexec_module ~#LoadModule suexec_module ~g' \  
-e 's~^LoadModule authn_~#LoadModule authn_~g' \  
-e 's~^LoadModule authz_dbd_module ~#LoadModule authz_dbd_module ~g' \  
-e 's~^LoadModule authz_dbm_module ~#LoadModule authz_dbm_module ~g' \  
-e 's~^LoadModule authz_groupfile_module ~#LoadModule authz_groupfile_module ~g' \  
-e 's~^LoadModule substitute_module ~#LoadModule substitute_module ~g' \  
-e 's~^LoadModule cache_disk_module ~#LoadModule cache_disk_module ~g' \  
-e 's~^LoadModule dbd_module ~#LoadModule dbd_module ~g' \  
-e 's~^LoadModule dumpio_module ~#LoadModule dumpio_module ~g' \  
-e 's~^LoadModule echo_module ~#LoadModule echo_module ~g' \  
-e 's~^LoadModule userdir_module ~#LoadModule userdir_module ~g' \  
-e 's~^LoadModule authz_user_module ~#LoadModule authz_user_module ~g' \  
/etc/httpd/conf.modules.d/00-base.conf  
  
RUN sed -i \  
-e 's~^\\(LoadModule .*\\)$~#\1~g' \  
/etc/httpd/conf.modules.d/01-cgi.conf  
  
#
-----------------------------------------------------------------------------  
# Disable the default SSL Virtual Host  
#
-----------------------------------------------------------------------------  
RUN sed -i \  
-e '/<VirtualHost _default_:443>/,/#<\/VirtualHost>/ s~^~#~' \  
/etc/httpd/conf.d/ssl.conf  
  
#
-----------------------------------------------------------------------------  
# Limit process for the application user  
#
-----------------------------------------------------------------------------  
RUN { \  
echo ''; \  
echo $'apache\tsoft\tnproc\t30'; \  
echo $'apache\thard\tnproc\t50'; \  
echo $'app\tsoft\tnproc\t30'; \  
echo $'app\thard\tnproc\t50'; \  
} >> /etc/security/limits.conf  
  
#
-----------------------------------------------------------------------------  
# Global PHP configuration changes  
#
-----------------------------------------------------------------------------  
RUN sed -i \  
-e 's~^;date.timezone =$~date.timezone = UTC~g' \  
-e 's~^;user_ini.filename =$~user_ini.filename =~g' \  
-e 's~^; max_input_vars.*$~max_input_vars = 4000~g' \  
-e 's~^;always_populate_raw_post_data = -1$~always_populate_raw_post_data = -1~g' \  
-e 's~^upload_max_filesize.*$~upload_max_filesize = 8M~g' \  
-e 's~^post_max_size.*$~post_max_size = 12M~g' \  
-e 's~^expose_php.*$~expose_php = Off~g' \  
-e 's~^allow_url_fopen.*$~allow_url_fopen = Off~g' \  
-e 's~^session.cookie_httponly.*$~session.cookie_httponly = On~g' \  
-e 's~^disable_functions.*$~disable_functions = shell_exec,show_source,fopen_with_path,dbmopen,dbase_open,filepro,filepro_rowcount,filepro_retrieve,posix_mkfifo~g' \  
/etc/php.ini  
  
#
-----------------------------------------------------------------------------  
# PHP Ioncube  
#
-----------------------------------------------------------------------------  
RUN cd /usr/lib64/php/modules \  
&& curl -fSLo ioncube_loaders_lin_x86-64.tar.gz
https://downloads.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
\  
&& tar -xvf ioncube_loaders_lin_x86-64.tar.gz \  
&& rm ioncube_loaders_lin_x86-64.tar.gz  
  
RUN echo '[Ioncube]' >> /etc/php.ini  
RUN echo 'zend_extension =
/usr/lib64/php/modules/ioncube/ioncube_loader_lin_7.1.so' >> /etc/php.ini  
  
#
-----------------------------------------------------------------------------  
# ImageMagick  
#
-----------------------------------------------------------------------------  
RUN echo '' | pecl install imagick  
RUN echo "extension=imagick.so" > /etc/php.d/imagick.ini  
  
#
-----------------------------------------------------------------------------  
# https://wkhtmltopdf.org  
# with dependencies: libXrender fontconfig libXext urw-fonts  
#
-----------------------------------------------------------------------------  
RUN cd /usr/local/bin \  
&& curl -fSLo wkhtmltox.tar.xz
https://downloads.wkhtmltopdf.org/0.12/0.12.4/wkhtmltox-0.12.4_linux-generic-
amd64.tar.xz \  
&& tar -xf wkhtmltox.tar.xz \  
&& rm wkhtmltox.tar.xz \  
&& ln -s /usr/local/bin/wkhtmltox/bin/wkhtmltopdf /usr/local/bin/wkhtmltopdf  
  
#
-----------------------------------------------------------------------------  
# Redis client  
#
-----------------------------------------------------------------------------  
RUN curl -fSLo /tmp/phpredis-master.zip
https://github.com/phpredis/phpredis/archive/master.zip \  
&& cd /tmp \  
&& unzip phpredis-master.zip \  
&& cd phpredis-master \  
&& phpize \  
&& ./configure \  
&& make \  
&& make install \  
&& cp /tmp/phpredis-master/modules/redis.so /usr/lib64/php/modules/ \  
&& cp /tmp/phpredis-master/rpm/redis.ini /etc/php.d/ \  
&& rm -fR /tmp/phpredis-master*  
  
#
-----------------------------------------------------------------------------  
# Unoconv  
#
-----------------------------------------------------------------------------  
RUN yum -y install unoconv libreoffice-headless  
  
#
-----------------------------------------------------------------------------  
# PDFtk  
# https://www.linuxglobal.com/pdftk-works-on-centos-7/  
#
-----------------------------------------------------------------------------  
COPY rpm/pdftk-2.02-1.el7.x86_64.rpm /tmp  
RUN yum -y localinstall /tmp/pdftk-2.02-1.el7.x86_64.rpm && \  
rm /tmp/pdftk-2.02-1.el7.x86_64.rpm  
  
#
-----------------------------------------------------------------------------  
# Add default service users  
#
-----------------------------------------------------------------------------  
RUN if ! grep -q ":${gid}:" /etc/group;then groupadd -g ${gid} app;fi  
RUN useradd -u ${uid} -d /var/www/app -m -g ${gid} app \  
&& usermod -a -G ${gid} apache  
  
#
-----------------------------------------------------------------------------  
# Add a symbolic link to the app users home within the home directory &  
# Create the initial directory structure  
#
-----------------------------------------------------------------------------  
RUN ln -s /var/www/app /home/app \  
&& mkdir -p /var/www/app/{public_html,var/{log,session}}  
  
#
-----------------------------------------------------------------------------  
# Virtual hosts configuration  
#
-----------------------------------------------------------------------------  
ADD etc/httpd/conf.d/ /etc/httpd/conf.d  
  
#
-----------------------------------------------------------------------------  
# Set permissions  
#
-----------------------------------------------------------------------------  
RUN chown -R app:${gid} /var/www/app \  
&& chmod 770 /var/www/app \  
&& chmod -R g+w /var/www/app/var  
  
#
-----------------------------------------------------------------------------  
# Remove packages  
#
-----------------------------------------------------------------------------  
RUN yum -y remove \  
gcc \  
gcc-c++ \  
&& rm -rf /var/cache/yum/* \  
&& yum clean all  
  
#
-----------------------------------------------------------------------------  
# Set default environment variables used to identify the service container  
#
-----------------------------------------------------------------------------  
ENV SERVICE_UNIT_APP_GROUP app-1  
ENV SERVICE_UNIT_LOCAL_ID 1  
ENV SERVICE_UNIT_INSTANCE 1  
#
-----------------------------------------------------------------------------  
# Set default environment variables used to configure the service container  
#
-----------------------------------------------------------------------------  
ENV APACHE_SERVER_ALIAS ""  
ENV APACHE_SERVER_NAME app-1.local  
ENV APP_HOME_DIR /var/www/app  
ENV DATE_TIMEZONE UTC  
ENV HTTPD /usr/sbin/httpd  
ENV SERVICE_USER app  
ENV SERVICE_USER_GROUP app  
ENV SERVICE_USER_PASSWORD ""  
ENV SUEXECUSERGROUP false  
ENV TERM xterm  
ENV DB_MYSQL_PORT_3306_TCP_ADDR ""  
ENV DB_MYSQL_PORT_3306_TCP_PORT ""  
#
-----------------------------------------------------------------------------  
# Set locale  
#
-----------------------------------------------------------------------------  
RUN localedef -i en_GB -f UTF-8 en_GB.UTF-8  
ENV LANG en_GB.UTF-8  
#
-----------------------------------------------------------------------------  
# Set ports  
#
-----------------------------------------------------------------------------  
EXPOSE 80 443  
#
-----------------------------------------------------------------------------  
# Copy files into place  
#
-----------------------------------------------------------------------------  
ADD index.php /var/www/app/public_html/index.php  
  
CMD ["/usr/sbin/httpd", "-DFOREGROUND"]

