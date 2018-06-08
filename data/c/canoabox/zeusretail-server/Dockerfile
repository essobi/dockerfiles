FROM centos:6.7  
MAINTAINER CD2 DevOps <gabriel@cd2.com.br>  
ENV HOME /root  
  
# Dependencias  
ADD ./third-party/epel-release-6-8.noarch.rpm /tmp/  
RUN yum localinstall -y /tmp/epel-release-6-8.noarch.rpm \  
&& rm -rf /var/cache/yum/* \  
&& yum clean all  
RUN rpm --rebuilddb \  
&& yum install -y tar gcc make perl gd-devel libxml2 libxml2-devel \  
openssl openssl-devel wget patch samba \  
glibc-common.i686 glibc.i686 libaio python-setuptools unzip curl-devel \  
openssl098e \  
nano telnet dos2unix libpng12 libpng libpng-devel libhugetlbfs links \  
net-tools zip gcc-c++ openssh-clients rsync libjpeg libjpeg-devel \  
mysql-devel mysql-libs \  
# postgresql postgresql-devel \  
memcached \  
strace vim-enhanced freetype freetype-devel zlib curl \  
ftp libmcrypt libmcrypt-devel \  
openldap openldap-devel autoconf \  
#TODO: Verificado essas necessidades pelo log zeusmanager.log  
libxml2-2.7.6-21.el6_8.1.i686 \  
&& rm -rf /var/cache/yum/* \  
&& yum clean all  
  
# SupervisorD  
RUN easy_install 'supervisor == 3.2.0' 'supervisor-stdout == 0.1.1' \  
&& mkdir -p /var/log/supervisor/ && mkdir -p /etc/supervisor/conf.d/  
ADD ./conf/supervisor/supervisord.conf /etc/supervisor/supervisord.conf  
ADD ./conf/supervisor/apache2.ini /etc/supervisor/conf.d/apache2.ini  
ADD ./conf/supervisor/samba.ini /etc/supervisor/conf.d/samba.ini  
ADD ./conf/supervisor/memcached.ini /etc/supervisor/conf.d/memcached.ini  
ADD ./conf/supervisor/comet_zanthus.ini
/etc/supervisor/conf.d/comet_zanthus.ini  
ADD ./conf/supervisor/mirage.ini /etc/supervisor/conf.d/mirage.ini  
  
# Samba  
ADD ./conf/samba/smb.conf /etc/samba/smb.conf  
  
# Zeus Retail  
ADD ./conf/zanthus/zanthus.conf /etc/ld.so.conf.d/zanthus.conf  
RUN ldconfig  
RUN adduser zanthus && usermod -u 900 zanthus && groupmod -g 900 zanthus  
RUN mkdir -p /Zanthus/Zeus/Manager \  
&& mkdir -p /Zanthus/Zeus/lib \  
&& mkdir -p /Zanthus/Zeus/especial \  
&& mkdir -p /Zanthus/Zeus/path_comum/EXISTE \  
&& chmod 777 /Zanthus/Zeus/path_comum  
RUN ln -s /usr/lib64/libjpeg.so.62.1.0 /usr/lib/libjpeg.so  
RUN ln -s /usr/lib64/libgd.so.2 /usr/lib/libgd.so  
RUN ln -s /usr/lib64/libpng.so /usr/lib/libpng.so  
  
# Apache  
ADD ./third-party/httpd-2.2.32.tar.gz /usr/src  
WORKDIR /usr/src/httpd-2.2.32  
RUN ./configure --enable-ssl --enable-so --enable-rewrite --enable-deflate \  
\--enable-cache --enable-mem_cache && make && make install  
WORKDIR /usr/src  
RUN rm -rf httpd-2.2.32  
# Apache config for Zeus Retail  
RUN chown -R zanthus.zanthus /usr/local/apache2  
RUN chmod -R 775 /usr/local/apache2/  
ADD ./conf/apache/zeusretail.conf
/usr/local/apache2/conf/extra/zeusretail.conf  
RUN echo "Include conf/extra/httpd-default.conf" >>
/usr/local/apache2/conf/httpd.conf  
RUN echo "Include conf/extra/zeusretail.conf" >>
/usr/local/apache2/conf/httpd.conf  
RUN sed -i "s/AccessFileName .htaccess/#AccessFileName .htaccess/g" \  
/usr/local/apache2/conf/extra/httpd-default.conf  
RUN rm -f /usr/local/apache2/htdocs/index.html  
ADD ./conf/apache/index.html /usr/local/apache2/htdocs/index.html  
#TODO: Verificado essas necessidades pelo log zeusmanager.log  
RUN ln -sf /usr/local/apache2/htdocs/manager/Kernel /Kernel  
RUN ln -sf /usr/local/apache2/htdocs /web  
  
# Postgres Libs 9.4  
ADD ./third-party/pgdg-centos94-9.4-3.noarch.rpm /tmp/  
RUN yum localinstall -y /tmp/pgdg-centos94-9.4-3.noarch.rpm \  
&& yum install -y postgresql94-libs postgresql94-devel \  
&& rm -rf /var/cache/yum/* \  
&& yum clean all  
RUN rm -rf /tmp/pgdg-centos94-9.4-3.noarch.rpm  
  
# Oracle Instant Client 12.1  
ADD ./third-party/oracle_instantclient_12_1-a.tar.xz /usr/local/  
ADD ./third-party/oracle_instantclient_12_1-b.tar.xz /usr/local/  
RUN ldconfig  
  
# PHP 5.6  
ADD ./third-party/php-5.6.28.tar.gz /usr/src  
WORKDIR /usr/src/php-5.6.28  
RUN ./configure --with-libdir=lib64 \  
\--with-apxs2=/usr/local/apache2/bin/apxs --enable-mbstring --with-zlib \  
\--enable-zip --with-freetype-dir=/usr/lib64 --with-gd --enable-soap \  
\--enable-sockets --enable-pcntl --enable-sigchild --enable-bcmath \  
\--enable-exif --with-openssl --with-curl=/usr \  
\--disable-cgi --enable-gd-native-ttf \  
\--with-mcrypt \  
\--with-pdo-pgsql=/usr/pgsql-9.4 --with-pgsql=/usr/pgsql-9.4 \  
\--with-mysql --with-mysqli \  
\--with-oci8=instantclient,/usr/local/instantclient_12_1 \  
&& make && make install  
ADD ./conf/php/php.ini /usr/local/lib/php.ini  
WORKDIR /usr/src  
RUN rm -rf php-5.6.28  
# PHP config for Zeus Retail  
ADD ./third-party/bibliotecas_php56.tar.xz /usr/local/lib/php/extensions/no-
debug-non-zts-20131226  
  
# NodeJS  
ADD ./third-party/node-v0.12.9.tar.gz /usr/src  
WORKDIR /usr/src/node-v0.12.9  
RUN ./configure && make && make install && ln -sf /usr/local/bin/node /bin/  
WORKDIR /usr/src  
RUN rm -rf node-v0.12.9  
  
# MemCache  
ADD ./third-party/memcache-3.0.8.tgz /usr/src  
WORKDIR /usr/src/memcache-3.0.8  
RUN phpize \  
&& ./configure --with-php-config=/usr/local/bin/php-config \  
&& make && make install  
WORKDIR /usr/src  
RUN rm -rf memcache-3.0.8  
RUN sed -i '/MAXCONN=/s/"1024"/"5000"/' /etc/sysconfig/memcached \  
&& sed -i '/CACHESIZE=/s/"64"/"2048"/' /etc/sysconfig/memcached  
  
# Zeus Retail parte 2  
RUN wget
ftp://ftp.zanthus.com.br:2142/pub/Zeus_Frente_de_Loja/_Complementares/so/* \  
-P /Zanthus/Zeus/lib \  
&& wget
ftp://ftp.zanthus.com.br:2142/pub/Zeus_Frente_de_Loja/_Complementares/kernz/2_4/kernz_r64.so
\  
-P /Zanthus/Zeus/lib \  
&& wget
ftp://ftp.zanthus.com.br:2142/pub/Zeus_Frente_de_Loja/_Complementares/KernD/v2_1/*.so
\  
-P /Zanthus/Zeus/lib \  
&& wget
ftp://ftp.zanthus.com.br:2142/pub/Zeus_Frente_de_Loja/_Complementares/so_r64/*
\  
-P /Zanthus/Zeus/lib   
RUN LATEST_WEB=$(curl ftp://ftp.zanthus.com.br:2142/pub/Zeus_Retail/WEB/ 2>
/dev/null | grep _php_5_6 | tail -n1 | cut -d ":" -f2 | cut -d " " -f2) \  
&& wget ftp://ftp.zanthus.com.br:2142/pub/Zeus_Retail/WEB/$LATEST_WEB \  
-P /usr/local/apache2/htdocs \  
&& unzip /usr/local/apache2/htdocs/$LATEST_WEB -d
/usr/local/apache2/htdocs/manager \  
&& LATEST_CODFON=$(curl ftp://ftp.zanthus.com.br:2142/pub/Zeus_Frente_de_Loja/
2> /dev/null | grep v_1_1 | tail -n1 | cut -d ":" -f2 | cut -d " " -f2) \  
&& RADICAL_CODFON=$(curl
ftp://ftp.zanthus.com.br:2142/pub/Zeus_Frente_de_Loja/$LATEST_CODFON/ 2>
/dev/null | tail -n1 | cut -d ":" -f2 | cut -d " " -f2 | cut -d "." -f1 | cut
-d "_" -f1,2,3,4,5,6) \  
&& wget
ftp://ftp.zanthus.com.br:2142/pub/Zeus_Frente_de_Loja/$LATEST_CODFON/$RADICAL_CODFON\\_CZ.EXL
\  
-P /Zanthus/Zeus/lib \  
&& tar zxvf /Zanthus/Zeus/lib/$RADICAL_CODFON\\_CZ.EXL -C /Zanthus/Zeus/lib/ \  
#&& wget
ftp://ftp.zanthus.com.br:2142/pub/Zeus_Frente_de_Loja/$LATEST_CODFON/$RADICAL_CODFON\\_CJ.EXL
\  
#-P /Zanthus/Zeus/lib \  
#&& tar zxvf /Zanthus/Zeus/lib/$RADICAL_CODFON\\_CJ.EXL -C /Zanthus/Zeus/lib/
\  
&& wget
ftp://ftp.zanthus.com.br:2142/pub/Zeus_Frente_de_Loja/$LATEST_CODFON/$RADICAL_CODFON\\_CW.EXL
\  
-P /Zanthus/Zeus/lib \  
&& tar zxvf /Zanthus/Zeus/lib/$RADICAL_CODFON\\_CW.EXL -C /Zanthus/Zeus/lib/  
RUN LATEST_KC=$(curl ftp://ftp.zanthus.com.br:2142/pub/Zeus_Frente_de_Loja/ 2>
/dev/null | grep -v v_1_X_X | grep -v 1_X_4 | grep v_1_X | tail -n1 | cut -d
":" -f2 | cut -d " " -f2) \  
&& RADICAL_KC=$(curl
ftp://ftp.zanthus.com.br:2142/pub/Zeus_Frente_de_Loja/$LATEST_KC/ 2> /dev/null
| tail -n1 | cut -d ":" -f2 | cut -d " " -f2 | cut -d "." -f1 | cut -d "_"
-f1,2,3,4,5,6) \  
&& wget
ftp://ftp.zanthus.com.br:2142/pub/Zeus_Frente_de_Loja/$LATEST_KC/$RADICAL_KC\\_CZ.EXL
\  
-P /Zanthus/Zeus/lib \  
&& tar zxvf /Zanthus/Zeus/lib/$RADICAL_KC\\_CZ.EXL -C /Zanthus/Zeus/lib/  
RUN ln -sf /Zanthus/Zeus/lib/kernz_r64.so /usr/local/lib/kernz.so \  
&& ln -sf /Zanthus/Zeus/lib/lib_rotkernD_r64.so
/usr/local/lib/lib_rotkernD_r64.so \  
&& chmod -R 777 /Zanthus \  
&& chown -R zanthus.zanthus /Zanthus \  
&& chown -R zanthus.zanthus /usr/local/apache2/ \  
&& ldconfig \  
&& ln -sf /etc/config/ZMWSInfo.ini /Zanthus/Zeus/Manager/ZMWSInfo.ini  
RUN ln -sf /usr/local/apache2/htdocs/manager/Arquivos /Zanthus/Zeus/Arquivos  
  
# kernz.so para php 5.6 eh diferente e nao esta no FTP!  
RUN rm -rf /Zanthus/Zeus/lib/kernz_r64.so  
ADD ./third-party/kernz_r64.so /Zanthus/Zeus/lib/  
RUN ln -sf /Zanthus/Zeus/lib/kernz_r64.so /usr/local/lib/php/extensions/no-
debug-non-zts-20131226/kernz.so  
RUN chown zanthus.zanthus /Zanthus/Zeus/lib/kernz_r64.so  
RUN chmod 777 /Zanthus/Zeus/lib/kernz_r64.so  
  
#comet_zanthus  
ADD ./third-party/comet_zanthus_1.0.1.5.zip /web  
WORKDIR /web  
RUN unzip comet_zanthus_1.0.1.5.zip \  
&& chown -R zanthus.zanthus comet_zanthus_nodejs \  
&& rm -rf comet_zanthus_1.0.1.5.zip  
  
#phpPgAdmin  
RUN wget
https://downloads.sourceforge.net/project/phppgadmin/phpPgAdmin%20%5Bstable%5D/phpPgAdmin-5.1/phpPgAdmin-5.1.tar.gz
-O phpPgAdmin-5.1.tar.gz \  
&& tar zxvf phpPgAdmin-5.1.tar.gz -C /usr/local/apache2/htdocs/ \  
&& rm -f phpPgAdmin-5.1.tar.gz \  
&& mv /usr/local/apache2/htdocs/phpPgAdmin-5.1
/usr/local/apache2/htdocs/pgadmin \  
&& sed -i "/['extra_login_security']/s/true/false/"
/usr/local/apache2/htdocs/pgadmin/conf/config.inc.php \  
&& sed -i "/['host']/s/'';/'postgres';/"
/usr/local/apache2/htdocs/pgadmin/conf/config.inc.php  
  
#config volume  
RUN mkdir -p /etc/config && chmod 777 -R /etc/config  
VOLUME ["/etc/config"]  
WORKDIR /  
EXPOSE 80 137 139 445  
CMD ["/usr/bin/supervisord", "--
configuration=/etc/supervisor/supervisord.conf"]  

