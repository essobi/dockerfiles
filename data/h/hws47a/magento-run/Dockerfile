FROM ubuntu  
  
## INSTALL SSH (used by external  
ENV NOTVISIBLE "in users profile"  
RUN apt-get -qy update \  
&& apt-get install -y openssh-server \  
&& mkdir -p /var/run/sshd \  
&& echo 'root:root' | chpasswd \  
&& sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config \  
&& sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd \  
&& echo "export VISIBLE=now" >> /etc/profile \  
&& rm -rf /var/lib/apt/lists/*  
  
# INSTALL SUPERVISOR AND VIM  
RUN apt-get -qy update \  
&& apt-get install -y supervisor \  
&& apt-get install -qy vim \  
&& rm -rf /var/lib/apt/lists/*  
  
# supervisor  
COPY config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
## INSTALL NGINX  
ENV NGINX_VERSION 1.10.2-1~jessie  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \  
&& echo "deb http://nginx.org/packages/debian/ jessie nginx" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y nginx \  
&& rm -rf /var/lib/apt/lists/*  
  
#nginx  
COPY config/ssl/cert.pem /etc/nginx/ssl/cert.pem  
COPY config/ssl/cert.key /etc/nginx/ssl/cert.key  
COPY config/nginx/nginx.conf /etc/nginx/nginx.conf  
COPY config/nginx/sites-enabled/default.conf /etc/nginx/conf.d/default.conf  
COPY config/nginx/includes /etc/nginx/includes  
  
## INSTALL PHP  
RUN apt-get -qy update \  
&& apt-get install -y software-properties-common \  
&& locale-gen en_US.UTF-8 \  
&& export LANG=en_US.UTF-8 \  
&& add-apt-repository -y ppa:ondrej/php \  
&& apt-get -qy update \  
&& apt-get install -y php5.6-cli php5.6-common php5.6-json php5.6-mysql
php5.6-opcache php5.6-fpm php5.6-curl php5.6-gd php5.6-xml \  
&& apt-get purge -qy software-properties-common \  
&& apt-get -y autoremove \  
&& apt-get -y autoclean \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /run/php/  
  
# Configure  
COPY config/php/php.ini /etc/php/5.6/fpm/php.ini  
COPY config/php/php-fpm.conf /etc/php/5.6/fpm/pool.d/www.conf  
  
# INSTALL MYSQL  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get -qy update \  
&& echo 'mysql-server mysql-server/root_password password root' | debconf-set-
selections \  
&& echo 'mysql-server mysql-server/root_password_again password root' |
debconf-set-selections \  
&& apt-get install -qy mysql-client mysql-server \  
&& rm -rf /var/lib/mysql/* \  
&& mysqld --initialize --datadir /var/lib/mysql
--explicit_defaults_for_timestamp \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /var/run/mysqld \  
&& chmod -R 777 /var/run/mysqld  
  
# Make sure the volume mount point is empty  
RUN rm -rf /var/www/html/*  
  
EXPOSE 80 443 22  
CMD ["supervisord"]  

