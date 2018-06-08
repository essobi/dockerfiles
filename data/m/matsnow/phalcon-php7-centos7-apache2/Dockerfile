FROM centos:7  
MAINTAINER matnow <matsnow@outlook.jp>  
  
# install package  
RUN yum -y update && \  
yum install -y initscripts wget gcc make make tar gcc-c++ git vim which \  
pcre-devel openssl-devel libxml2-devel curl-devel libpng-devel autoconf | true  
  
WORKDIR /usr/local/src  
RUN wget http://www.us.apache.org/dist/apr/apr-1.5.2.tar.gz &&\  
wget http://www.us.apache.org/dist/apr/apr-util-1.5.4.tar.gz &&\  
wget http://archive.apache.org/dist/httpd/httpd-2.4.20.tar.gz &&\  
wget
'http://osdn.jp/frs/g_redir.php?m=kent&f=%2Fmcrypt%2FLibmcrypt%2F2.5.8%2Flibmcrypt-2.5.8.tar.gz'
-O libmcrypt-2.5.8.tar.gz &&\  
wget --max-redirect=3 -O php-7.0.11.tar.gz
http://jp2.php.net/get/php-7.0.11.tar.gz/from/this/mirror  
RUN tar -xzvf libmcrypt-2.5.8.tar.gz &&\  
tar -zxvf apr-1.5.2.tar.gz &&\  
tar -xzvf apr-util-1.5.4.tar.gz &&\  
tar -xzvf httpd-2.4.20.tar.gz &&\  
tar -xzvf php-7.0.11.tar.gz  
RUN git clone \--depth=1 https://github.com/phalcon/cphalcon.git &&\  
git clone git://github.com/phalcon/phalcon-devtools.git  
  
# install APR  
WORKDIR /usr/local/src/apr-1.5.2  
RUN ./configure --prefix=/opt/apr/apr-1.5.2 && make && make install  
  
# install APR-util  
WORKDIR /usr/local/src/apr-util-1.5.4  
RUN ./configure --prefix=/opt/apr-util/apr-util-1.5.4 --with-
apr=/opt/apr/apr-1.5.2  
RUN make && make install  
  
# install apache  
WORKDIR /usr/local/src/httpd-2.4.20  
RUN ./configure --enable-so --enable-ssl --enable-rewrite --with-
apr=/opt/apr/apr-1.5.2 --with-apr-util=/opt/apr-util/apr-util-1.5.4 &&\  
make && make install  
  
# install mcypt  
WORKDIR /usr/local/src/libmcrypt-2.5.8  
RUN ./configure --disable-posix-threads && make install  
  
# install php  
WORKDIR /usr/local/src/php-7.0.11  
RUN ./configure --with-apxs2=/usr/local/apache2/bin/apxs --with-mysql --with-
zlib --enable-mysqlnd --enable-zip --with-xml --with-curl --with-hash --with-
pdo --enable-mbstring --with-pdo-mysql --with-openssl --with-mcrypt=/usr/local
&& make && make install  
  
# install apcu  
RUN echo yes | pecl install apcu  
  
# install phalcon  
WORKDIR /usr/local/src/cphalcon/build  
RUN ./install  
  
# setting php.ini  
WORKDIR /usr/local/src  
RUN cp /usr/local/src/php-7.0.11/php.ini-development /usr/local/lib/php.ini  
RUN sed -i -e 's/;date.timezone =/date.timezone = Asia\/Tokyo/g'
/usr/local/lib/php.ini  
ADD ./php.ini.add php.ini.add  
RUN cat php.ini.add >> /usr/local/lib/php.ini  
  
# add www user  
RUN useradd -u 1000 -s /bin/bash -m www  
RUN mkdir -p /var/www/html && chown www /var/www/html  
  
# setting apache  
RUN sed -i -e 's/User daemon/User www/g' /usr/local/apache2/conf/httpd.conf
&&\  
sed -i -e 's/Group daemon/Group www/g' /usr/local/apache2/conf/httpd.conf &&\  
sed -i -e 's/#LoadModule ssl_module /LoadModule ssl_module /g'
/usr/local/apache2/conf/httpd.conf && \  
sed -i -e 's/#LoadModule socache_shmcb_module /LoadModule socache_shmcb_module
/g' /usr/local/apache2/conf/httpd.conf && \  
sed -i -e 's/#LoadModule rewrite_module /LoadModule rewrite_module /g'
/usr/local/apache2/conf/httpd.conf && \  
sed -i -e '236 s/AllowOverride None/AllowOverride All/g'
/usr/local/apache2/conf/httpd.conf && \  
sed -i -e 's/\/usr\/local\/apache2\/htdocs/\/var\/www\/html/g'
/usr/local/apache2/conf/httpd.conf  
ADD ./apache/server.key /usr/local/apache2/conf/server.key  
ADD ./apache/server.crt /usr/local/apache2/conf/server.crt  
ADD ./apache/server.csr /usr/local/apache2/conf/server.csr  
ADD ./apache/local.conf /usr/local/apache2/conf/extra/httpd-local.conf  
RUN echo "Include conf/extra/httpd-local.conf" >>
/usr/local/apache2/conf/httpd.conf  
  
# install phalcon devtools  
WORKDIR phalcon-devtools/  
ENV PTOOLSPATH /usr/local/src/phalcon-devtools/  
RUN . ./phalcon.sh  
RUN ln -s /usr/local/src/phalcon-devtools/phalcon.php /usr/bin/phalcon  
RUN chmod ugo+x /usr/bin/phalcon  
  
# create sample project  
USER www  
WORKDIR /var/www/html  
RUN phalcon create-project hello-world --enable-webtools  
RUN sed -i -e "s/define('PTOOLS_IP', '192.168.');/define('PTOOLS_IP',
'172.17.');/" hello-world/public/webtools.config.php  
  
# set environment path  
USER root  
ENV PATH $PATH:/usr/local/apache2/bin  
  
# start service  
EXPOSE 80 443  
VOLUME ["/var/www/html"]  
ADD services.sh /usr/local/bin/services.sh  
CMD ["/usr/local/bin/services.sh"]  

