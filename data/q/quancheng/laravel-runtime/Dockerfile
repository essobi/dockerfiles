FROM ubuntu:14.04  
ENV TZ="Asia/Shanghai"  
RUN apt-get update;  
  
RUN apt-get install -y software-properties-common python-software-properties;  
RUN add-apt-repository ppa:git-core/ppa;  
  
RUN add-apt-repository ppa:ondrej/php;  
RUN add-apt-repository ppa:chris-lea/nginx-devel  
  
RUN apt-get update;  
  
RUN apt-get install -y --force-yes vim wget git-core libpcre3 libpcre3-dev
libssl-dev libldap2-dev libtool nodejs \  
redis-server python python-pip python-dev build-essential \  
php5.6 php5.6-redis php5.6-mcrypt php5.6-mongo php5.6-fpm php5.6-mysql
php5.6-curl php5.6-xml \  
php5.6-zip php5.6-intl php5.6-gmp php5.6-mbstring php5.6-amqp php5.6-opcache
php5.6-soap php5.6-bcmath php5.6-gd php5.6-xdebug redis-server;  
  
#编译安装nginx  
RUN pwd  
RUN wget https://nginx.org/download/nginx-1.13.3.tar.gz  
RUN wget http://zlib.net/zlib-1.2.11.tar.gz  
RUN tar -xvzf nginx-1.13.3.tar.gz  
RUN tar -zxf zlib-1.2.11.tar.gz  
RUN git clone https://github.com/kvspb/nginx-auth-ldap.git  
RUN cd /zlib-1.2.11 && ./configure  
RUN cd /zlib-1.2.11 && make  
RUN cd /zlib-1.2.11 && make install  
RUN chmod +x /nginx-1.13.3/configure  
RUN cd /nginx-1.13.3 && ./configure --user=root --group=root
--prefix=/etc/nginx --sbin-path=/usr/sbin/nginx --conf-
path=/etc/nginx/nginx.conf --pid-path=/var/run/nginx.pid --lock-
path=/var/run/nginx.lock --error-log-path=/var/log/nginx/error.log --http-log-
path=/var/log/nginx/access.log --with-http_gzip_static_module --with-
http_stub_status_module --with-http_ssl_module --with-pcre --with-file-aio
--with-http_realip_module --add-module=/nginx-auth-ldap/ --with-ipv6 --with-
debug  
RUN cd /nginx-1.13.3 && make  
RUN cd /nginx-1.13.3 && make install  
RUN mkdir /etc/nginx/sites-enabled  
  
RUN pip install -U pip; pip --version;  
  
RUN pip install supervisor;  
  
RUN echo_supervisord_conf > /etc/supervisord.conf;  
  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
RUN sed -i '116i\include /etc/nginx/sites-enabled/*;' /etc/nginx/nginx.conf  
  
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/5.6/fpm/php-
fpm.conf  
  
RUN sed -i -e "s/nodaemon=false/nodaemon=true/g" /etc/supervisord.conf  
  
RUN echo "files = /config/supervisor/*.conf" >> /etc/supervisord.conf  
  
RUN sed -i -e "s/;\\[include\\]/\\[include\\]/g" /etc/supervisord.conf  
  
RUN echo "opcache.revalidate_freq=60" >>
/etc/php/5.6/cli/conf.d/10-opcache.ini  
  
RUN sed -i -e "s/pm.max_children = 5/pm.max_children = 70/g"
/etc/php/5.6/fpm/pool.d/www.conf  
  
RUN sed -i -e "s/pm.start_servers = 2/pm.start_servers = 30/g"
/etc/php/5.6/fpm/pool.d/www.conf  
  
RUN sed -i -e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 10/g"
/etc/php/5.6/fpm/pool.d/www.conf  
  
RUN sed -i -e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 50/g"
/etc/php/5.6/fpm/pool.d/www.conf  
  
RUN mkdir /run/php/  
  
WORKDIR /root  
  

