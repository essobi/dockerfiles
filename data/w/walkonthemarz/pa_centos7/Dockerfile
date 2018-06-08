FROM centos:7  
  
MAINTAINER walkonthemarz@gmail.com  
  
COPY libImageOperationLib.so /usr/local/lib  
COPY supervisord.conf /etc/supervisord.conf  
  
  
RUN yum install -y epel-release \  
&& rpm -Uvh http://rpms.remirepo.net/enterprise/remi-release-7.rpm \  
&& yum install -y wget gcc yum-utils make python-setuptools python-pip \  
&& yum-config-manager --enable remi-php71 \  
&& yum install -y httpd mod_ssl php php-devel php-fpm php-gmp php-json php-
mbstring php-mcrypt php-mysqlnd php-opcache php-pdo php-pear php-xml php-gd
php-intl php-process php-tidy php-recode php-timecop php-soap php-pgsql php-
phpiredis php-pspell php-snappy php-xmlrpc php-ldap php-imap php-cli php-
bcmath php-ast php-embedded php-enchant php-pecl-mailparse php-pecl-
uploadprogress \  
&& pip install --upgrade pip \  
&& pip install supervisor \  
&& chmod 755 /usr/local/lib/libImageOperationLib.so \  
&& yum clean all  
  
COPY httpd.conf /etc/httpd/conf/httpd.conf  
COPY 00-mpm.conf /etc/httpd/conf.modules.d/00-mpm.conf  
COPY php.conf /etc/httpd/conf.d/php.conf  
  
COPY php-fpm.conf /etc/php-fpm.conf  
COPY www.conf /etc/php-fpm.d/www.conf  
RUN wget http://www.ijg.org/files/jpegsrc.v9b.tar.gz -O
/root/jpegsrc.v9b.tar.gz \  
&& tar -xvf /root/jpegsrc.v9b.tar.gz -C /root \  
&& cd /root/jpeg-9b && ./configure && make && make install clean \  
&& cd /root && echo "/usr/local/lib">> /etc/ld.so.conf && ldconfig \  
&& rm -rf /root/jpegsrc.v9b.tar.gz \  
&& rm -rf /root/jpeg-9b \  
&& mv /etc/httpd/conf.modules.d/15-php.conf
/etc/httpd/conf.modules.d/15-php.conf.bk \  
&& mkdir -p /var/www/html/app/public /var/www/html/log/ \  
&& useradd -rU -u 33 www-data && groupmod -g 33 -o www-data \  
&& mkdir -p /run/php-fpm && chown -R www-data:www-data /run/php-fpm \  
&& rm -rf /var/lib/php/{session,wsdlcache,opcache} && mkdir -p
/var/lib/php/{session,wsdlcache,opcache} && chown www-data:www-data
/var/lib/php/{session,wsdlcache,opcache}  
  
  
COPY kfb_reader /root/kfb_reader  
RUN cd /root/kfb_reader && phpize && ./configure && make && make install \  
&& cd /root && rm -rf /root/kfb_reader && echo "extension=kfb_reader.so" >
/etc/php.d/50-kfb_reader.ini  
  
  
HEALTHCHECK --interval=5s \--timeout=3s CMD curl -fs http://localhost || exit
1  
EXPOSE 80  
EXPOSE 443  
CMD []  
#ENTRYPOINT ["/opt/rh/httpd24/root/usr/sbin/apachectl", "-D", "FOREGROUND"]  
ENTRYPOINT ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]  
  

