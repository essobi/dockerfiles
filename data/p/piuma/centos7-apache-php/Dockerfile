FROM centos:7.2.1511  
  
MAINTAINER Piuma <piuma@piumalab.org>  
  
#  
# Import the Centos-6 RPM GPG key to prevent warnings and Add EPEL Repository  
#  
RUN rpm --import http://mirror.centos.org/centos/RPM-GPG-KEY-CentOS-7 \  
&& rpm --import http://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-7 \  
&& yum -y install epel-release.noarch  
  
  
RUN yum -y install \  
httpd \  
mysql-devel \  
mysql-libs \  
mod_ssl \  
php \  
php-cli \  
php-imap \  
php-ldap \  
php-mbstring \  
php-mcrypt \  
php-mysql \  
php-pear-MDB2-Driver-mysqli \  
php-pecl-memcached \  
php-tidy \  
php-xml \  
php-gd \  
msmtp \  
&& yum -y update bash \  
&& rm -rf /var/cache/yum/* \  
&& yum clean all  
  
#  
# UTC Timezone & Networking  
#  
RUN ln -sf /usr/share/zoneinfo/UTC /etc/localtime \  
&& echo "NETWORKING=yes" > /etc/sysconfig/network  
  
#  
# Global Apache configuration changes  
#  
RUN sed -i \  
-e 's~^ServerSignature On$~ServerSignature Off~g' \  
-e 's~^ServerTokens OS$~ServerTokens Prod~g' \  
-e 's~^#ExtendedStatus On$~ExtendedStatus On~g' \  
-e 's~^DirectoryIndex \\(.*\\)$~DirectoryIndex \1 index.php~g' \  
-e 's~^NameVirtualHost \\(.*\\)$~#NameVirtualHost \1~g' \  
/etc/httpd/conf/httpd.conf  
  
#  
# Disable Apache directory indexes  
#  
RUN sed -i \  
-e 's~^IndexOptions \\(.*\\)$~#IndexOptions \1~g' \  
-e 's~^IndexIgnore \\(.*\\)$~#IndexIgnore \1~g' \  
-e 's~^AddIconByEncoding \\(.*\\)$~#AddIconByEncoding \1~g' \  
-e 's~^AddIconByType \\(.*\\)$~#AddIconByType \1~g' \  
-e 's~^AddIcon \\(.*\\)$~#AddIcon \1~g' \  
-e 's~^DefaultIcon \\(.*\\)$~#DefaultIcon \1~g' \  
-e 's~^ReadmeName \\(.*\\)$~#ReadmeName \1~g' \  
-e 's~^HeaderName \\(.*\\)$~#HeaderName \1~g' \  
/etc/httpd/conf/httpd.conf  
  
#  
# Disable Apache language based content negotiation  
#  
RUN sed -i \  
-e 's~^LanguagePriority \\(.*\\)$~#LanguagePriority \1~g' \  
-e 's~^ForceLanguagePriority \\(.*\\)$~#ForceLanguagePriority \1~g' \  
-e 's~^AddLanguage \\(.*\\)$~#AddLanguage \1~g' \  
/etc/httpd/conf/httpd.conf  
  
#  
# Disable all Apache modules and enable the minimum  
#  
RUN sed -i \  
-e 's~^\\(LoadModule .*\\)$~#\1~g' \  
-e 's~^#LoadModule mime_module ~LoadModule mime_module ~g' \  
-e 's~^#LoadModule log_config_module ~LoadModule log_config_module ~g' \  
-e 's~^#LoadModule setenvif_module ~LoadModule setenvif_module ~g' \  
-e 's~^#LoadModule status_module ~LoadModule status_module ~g' \  
-e 's~^#LoadModule authz_host_module ~LoadModule authz_host_module ~g' \  
-e 's~^#LoadModule dir_module ~LoadModule dir_module ~g' \  
-e 's~^#LoadModule alias_module ~LoadModule alias_module ~g' \  
-e 's~^#LoadModule expires_module ~LoadModule expires_module ~g' \  
-e 's~^#LoadModule deflate_module ~LoadModule deflate_module ~g' \  
-e 's~^#LoadModule headers_module ~LoadModule headers_module ~g' \  
-e 's~^#LoadModule alias_module ~LoadModule alias_module ~g' \  
/etc/httpd/conf/httpd.conf  
  
#  
# Global PHP configuration changes  
#  
RUN sed -i \  
-e 's~^;date.timezone =$~date.timezone = Europe/Rome~g' \  
-e 's~^;user_ini.filename =$~user_ini.filename =~g' \  
-e 's~^sendmail_path = /usr/sbin/sendmail -t -i$~sendmail_path = /usr/bin/msmtp -C /etc/msmtprc -t -i~g' \  
/etc/php.ini  
  
RUN echo '<?php phpinfo(); ?>' > /var/www/html/index.php  
  
#  
# Add msmtp example configuration  
#  
RUN curl http://msmtp.sourceforge.net/doc/msmtprc.txt -o /etc/msmtprc  
  
#  
# Copy files into place  
#  
#ADD  
#  
# Purge  
#  
  
RUN rm -rf /sbin/sln \  
; rm -rf
/usr/{{lib,share}/locale,share/{man,doc,info,gnome/help,cracklib,il8n},{lib,lib64}/gconv,bin/localedef,sbin/build-
locale-archive} \  
; rm -rf /var/cache/{ldconfig,yum}/*  
  
EXPOSE 80 443  
  
CMD /usr/sbin/httpd -c "ErrorLog /dev/stdout" -DFOREGROUND  

