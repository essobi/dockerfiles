FROM centos:6.8  
MAINTAINER walkonthemarz@gmail.com  
  
COPY epel-release-latest-6.noarch.rpm /root  
COPY remi-release-6.rpm /root  
COPY libImageOperationLib.so /usr/local/lib  
COPY supervisord.conf /etc/supervisord.conf  
  
RUN chmod 755 /usr/local/lib/libImageOperationLib.so \  
&& rpm -Uvh /root/remi-release-6.rpm /root/epel-release-latest-6.noarch.rpm \  
&& yum --enablerepo=extras install -y wget gcc yum-utils python-setuptools
centos-release-scl python-pip \  
&& wget http://www.ijg.org/files/jpegsrc.v9b.tar.gz -O
/root/jpegsrc.v9b.tar.gz \  
&& tar -xvf /root/jpegsrc.v9b.tar.gz -C /root \  
&& cd /root/jpeg-9b && ./configure && make && make install clean \  
&& cd /root && echo "/usr/local/lib">> /etc/ld.so.conf && ldconfig \  
&& pip install --upgrade pip==9.0.3 \  
&& pip install --upgrade setuptools \  
&& pip install supervisor \  
&& rm -rf /root/jpegsrc.v9b.tar.gz \  
&& rm -rf /root/jpeg-9b \  
&& rm -rf /root/epel-release-latest-6.noarch.rpm \  
&& rm -rf /root/remi-release-6.rpm \  
&& yum clean all  
  
RUN yum-config-manager --enable remi-php71 \  
&& yum install -y php php-devel php-fpm php-gmp php-json php-mbstring php-
redis php-mcrypt php-mysqlnd php-opcache php-pdo php-pear php-xml php-gd php-
intl php-process php-smbclient php-tidy php-recode php-timecop php-soap php-
pgsql php-pspell php-snappy php-xmlrpc php-ldap php-imap php-cli php-bcmath
php-ast php-embedded php-enchant php-pecl-mailparse php-pecl-uploadprogress
php-pecl-swoole2 \  
&& yum clean all \  
&& mkdir -p /var/www/html/log/  
  
COPY php.ini /etc/php.ini  
  
COPY 50-kfb_reader.ini /etc/php.d/50-kfb_reader.ini  
COPY kfb_reader /root/kfb_reader  
  
RUN cd /root/kfb_reader && phpize && ./configure && make && make install \  
&& cd /root && rm -rf /root/kfb_reader  
  
COPY swoole /swoole  
  
HEALTHCHECK \--interval=5s --timeout=3s CMD curl -fs http://localhost || exit
1  
EXPOSE 80  
CMD []  
#ENTRYPOINT ["/opt/rh/httpd24/root/usr/sbin/apachectl", "-D", "FOREGROUND"]  
ENTRYPOINT ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]  

