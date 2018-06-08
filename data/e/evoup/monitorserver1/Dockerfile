# Run monitorserver1 in a container  
# (first create network: docker network create --subnet=172.18.0.0/16 b0)  
# if use use_source_mirror and use gitee: docker build -t evoup/monitorserver1
--build-arg use_source_mirror=1 --build-arg gitee_passwd=xxx .  
# default and use github: docker build -t evoup/monitorserver1 .  
# docker run --name monitorserver1_1 --privileged=true -p8004:80 -ti -d --ip
172.18.0.30 --net b0 --hostname monitorserver1_1 evoup/monitorserver1  
# docker run --name monitorserver1_2 --privileged=true -p8005:80 -ti -d --ip
172.18.0.31 --net b0 --hostname monitorserver1_2 evoup/monitorserver1  
# docker exec -it monitorserver1 /bin/tcsh  
# Base docker image  
#FROM debian:jessie  
FROM ubuntu:16.04  
LABEL maintainer "evoup <evoex123@gmail.com>"  
ARG use_source_mirror  
ARG gitee_passwd  
#avoid using add https://docs.docker.com/engine/userguide/eng-
image/dockerfile_best-practices/#entrypoint  
#ADD https://secure.php.net/distributions/php-5.4.45.tar.gz
/src/php-5.4.45.tar.gz  
#ADD http://pecl.php.net/get/proctitle-0.1.2.tgz /src/proctitle-0.1.2.tgz  
#ADD http://pecl.php.net/get/memcache-2.2.7.tgz /src/memcache-2.2.7.tgz  
#ADD http://alpha.gnu.org/pub/gnu/autoconf/autoconf-2.59d.tar.gz
/src/autoconf-2.59d.tar.gz  
#ADD
http://mirrors.hust.edu.cn/apache/zookeeper/zookeeper-3.4.6/zookeeper-3.4.6.tar.gz
/src/zookeeper-3.4.6.tar.gz  
#RUN sed -i 's/httpredir.debian.org/mirrors.ustc.edu.cn/g'
/etc/apt/sources.list  
RUN if [ "x$use_source_mirror" = "x" ] ; then echo not use yum mirror ; else
sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list ; fi  
RUN apt-get update  
RUN apt-get install libmemcache-dev libz-dev libxml2-dev libmemcache-dev
build-essential m4 git autoconf libjpeg-dev libpng-dev libcurl4-gnutls-dev
libfreetype6-dev libmcrypt-dev wget unzip libnet-ifconfig-wrapper-perl nginx
lsof inetutils-syslogd tcsh vim python python-pip libzookeeper-mt-dev -y  
RUN export LC_ALL=C && pip install --upgrade pip  
RUN pip install zkpython  
RUN mkdir -p /services/software/ext  
RUN wget http://museum.php.net/php5/php-5.4.45.tar.gz -O
/services/software/php-5.4.45.tar.gz  
RUN wget http://pecl.php.net/get/proctitle-0.1.2.tgz -O
/services/software/ext/proctitle-0.1.2.tgz  
RUN wget http://pecl.php.net/get/memcache-2.2.7.tgz -O
/services/software/ext/memcache-2.2.7.tgz  
RUN wget http://pecl.php.net/get/zookeeper-0.4.0.tgz -O
/services/software/ext/zookeeper-0.4.0.tgz  
RUN wget http://alpha.gnu.org/pub/gnu/autoconf/autoconf-2.59d.tar.gz -O
/services/software/autoconf-2.59d.tar.gz  
#RUN wget
http://mirrors.hust.edu.cn/apache/zookeeper/zookeeper-3.4.11/zookeeper-3.4.11.tar.gz
-O /services/software/zookeeper-3.4.11.tar.gz  
RUN wget
https://archive.apache.org/dist/zookeeper/zookeeper-3.4.11/zookeeper-3.4.11.tar.gz
-O /services/software/zookeeper-3.4.11.tar.gz  
  
#RUN mv /src/php-5.4.45.tar.gz /services/software/  
RUN cd /services/software/ && tar xzf php-5.4.45.tar.gz  
#RUN mv /src/proctitle-0.1.2.tgz /services/software/ext/  
RUN cd /services/software/ext && tar xzf proctitle-0.1.2.tgz  
RUN cp -r /services/software/ext/proctitle-0.1.2
/services/software/php-5.4.45/ext/proctitle  
#RUN mv /src/memcache-2.2.7.tgz /services/software/ext/  
RUN cd /services/software/ext && tar xzf memcache-2.2.7.tgz  
RUN cp -r /services/software/ext/memcache-2.2.7
/services/software/php-5.4.45/ext/memcache  
#RUN mv /src/autoconf-2.59d.tar.gz /services/software/  
RUN cd /services/software && tar xzf autoconf-2.59d.tar.gz  
RUN cd /services/software/autoconf-2.59d/ && ./configure && make && make
install  
RUN autoconf --version  
#RUN mv /src/zookeeper-3.4.6.tar.gz /services/software/  
RUN cd /services/software/ && tar xzf zookeeper-3.4.11.tar.gz  
RUN cd /services/software/ext/ && tar xzf zookeeper-0.4.0.tgz  
RUN cp -r /services/software/ext/zookeeper-0.4.0
/services/software/php-5.4.45/ext/zookeeper  
RUN cd /services/software/php-5.4.45 && ./buildconf --force  
RUN cd /services/software/zookeeper-3.4.11/src/c && ./configure
--prefix=/services/software/zookeeper-3.4.11/prefix/ && make -j$(nproc) &&
make install  
RUN cd /services/software/php-5.4.45/ && './configure' '--
prefix=/usr/local/php5_new' '--disable-cgi' '--enable-mbstring=all' '--enable-
pcntl' '--enable-dba' '--enable-sysvmsg' '--enable-sysvshm' '--enable-sockets'
'-enable-sigchild' '--enable-ftp' '--enable-memcache' '--enable-zookeeper' '--
with-libzookeeper-dir=/services/software/zookeeper-3.4.11/prefix/' '--enable-
proctitle' '--with-zlib' && make -j$(nproc) && make install  
#RUN cd /services/software && git clone git://git.gnome.org/libxml2  
#RUN cd /services/software/libxml2/ &&  
#RUN cd /services/software/php-5.4.45 && ./buildconf --force  
RUN cd /services/software/php-5.4.45/ && make clean && './configure' '--
prefix=/usr/local/php5_admin' '--with-layout=GNU' '--with-config-file-scan-
dir=/usr/local/php5_admin/etc/php' '--disable-all' '--enable-dom' '--enable-
filter' '--enable-hash' '--enable-json' '--with-mcrypt' '--with-curl' '--with-
pcre-regex' '--enable-mbstring' '--enable-ctype' '--enable-session' '--with-
libxml-dir' '--enable-libxml' '--enable-simplexml' '--enable-pdo' '--with-pdo-
mysql=mysqlnd' '--with-mysqli=mysqlnd' '--enable-sysvsem' '--enable-sysvshm' '
--enable-memcache' '--enable-fpm' '--enable-pcntl' '--enable-dba' '--enable-
dba' '--enable-sysvmsg' '--enable-sysvshm' '--enable-sockets' '--enable-
sigchild' '--enable-ftp' '--with-gd' '--enable-gd' '--enable-gd-native-ttf' '
--with-jpeg-dir=/usr/local' '--with-png=/usr/local' '--with-ttf' '--with-zlib'
'--with-freetype-dir=/usr/local' '--enable-track-vars' '--with-
pear=/usr/local/pear' '--enable-xml' '--with-mysql' '--enable-zookeeper' '--
with-libzookeeper-dir=/services/software/zookeeper-3.4.11/prefix' && find .
-name '*.1' > /tmp/php-1.lst.$$ && tar -cf /tmp/php-1.tar.$$ -T
/tmp/php-1.lst.$$ && make clean && tar -xf /tmp/php-1.tar.$$ && rm
/tmp/php-1.tar.$$ /tmp/php-1.lst.$$ && make -j$(nproc) && make install  
RUN cp /usr/local/php5_admin/etc/php-fpm.conf.default
/usr/local/php5_admin/etc/php-fpm.conf  
ADD files/php-fpm /etc/init.d/php-fpm  
RUN chmod +x /etc/init.d/php-fpm && touch /var/run/php-fpm.pid  
  
RUN groupadd nobody  
ADD files/php_fcgi_params.conf /etc/nginx/php_fcgi_params.conf  
ADD files/default /etc/nginx/sites-available/default  
RUN echo "\n\n\nsecurity.limit_extensions = .php .php3 .php4 .php5 .m\n" >>
/usr/local/php5_admin/etc/php-fpm.conf  
ADD files/php.ini /usr/local/php5_admin/etc/php.ini  
ADD files/php.ini /usr/local/php5_new/etc/php.ini  
#RUN cd /var/www/html/ && git clone https://github.com/evoup/monitor_pass.git  
#RUN cd /var/www/html/ && git clone
http://evoup:${gitee_passwd}@gitee.com/evoup/monitor_pass.git  
RUN if [ "x$use_source_mirror" = "x" ] ; then cd /var/www/html/ && git clone
https://github.com/evoup/monitor_pass.git ; else cd /var/www/html/ && git
clone http://evoup:${gitee_passwd}@gitee.com/evoup/monitor_pass.git ; fi  
RUN ln -s /var/www/html/monitor_pass/monitor_ui/ /var/www/html/monitor_ui  
#RUN cd /tmp/ && wget https://codeload.github.com/evoup/workenv/zip/master -O
/tmp/workenv.zip && unzip workenv.zip && cd /tmp/workenv-master/ && mv
vim_setting/ .vimrc .vim .cshrc /root/ && rm -rf /tmp/workenv-master && rm -rf
/tmp/workenv.zip && mkdir /root/.vimbak  
#RUN cd /tmp/ && git clone
http://evoup:${gitee_passwd}@gitee.com/evoup/workenv.git && cd /tmp/workenv/
&& mv vim_setting/ .vimrc .vim .cshrc /root/ && rm -rf /tmp/workenv && mkdir
/root/.vimbak  
RUN if [ "x$use_source_mirror" = "x" ] ; then cd /tmp/ && wget
https://codeload.github.com/evoup/workenv/zip/master -O /tmp/workenv.zip &&
unzip workenv.zip && cd /tmp/workenv-master/ && mv vim_setting/ .vimrc .vim
.cshrc /root/ && rm -rf /tmp/workenv-master && rm -rf /tmp/workenv.zip &&
mkdir /root/.vimbak ; else cd /tmp/ && git clone
http://evoup:${gitee_passwd}@gitee.com/evoup/workenv.git && cd /tmp/workenv/
&& mv vim_setting/ .vimrc .vim .cshrc /root/ && rm -rf /tmp/workenv && mkdir
/root/.vimbak ; fi  
RUN apt-get install --reinstall dpkg  
  
EXPOSE 80  
ADD files/start.sh /start.sh  
RUN chmod 755 start.sh  
CMD ["./start.sh" ]  
  

