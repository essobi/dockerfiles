FROM ubuntu:14.04  
# Get noninteractive frontend for Debian to avoid some problems:  
# debconf: unable to initialize frontend: Dialog  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV LANG en_US.UTF-8  
ENV LC_ALL "en_US.UTF-8"  
ENV LANGUAGE en_US:en  
  
RUN apt-get update && apt-get install -y wget \  
software-properties-common python-software-properties supervisor language-
pack-en-base \  
curl git vim nfs-kernel-server nfs-common unzip pwgen  
RUN mkdir -p /var/log/supervisor /var/log/nginx /run/php  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile \  
&& echo "/var/www *(rw,async,no_subtree_check,insecure)" >> /etc/exports \  
&& echo "export TERM=xterm" >> ~/.bashrc  
  
# nginx  
RUN printf '%s\n%s\n' "deb http://nginx.org/packages/mainline/ubuntu/ trusty
nginx" "deb-src http://nginx.org/packages/mainline/ubuntu/ trusty nginx" >>
/etc/apt/sources.list  
RUN wget -qO - http://nginx.org/keys/nginx_signing.key | apt-key add -  
# php7  
RUN LC_ALL=C.UTF-8 add-apt-repository -y ppa:ondrej/php  
# mariadb begin  
RUN groupadd -r mysql && useradd -r -g mysql mysql  
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0xcbcb082a1bb943db  
RUN add-apt-repository 'deb [arch=amd64,i386]
http://sfo1.mirrors.digitalocean.com/mariadb/repo/10.2/ubuntu trusty main'  
ENV MARIADB_MAJOR 10.2  
RUN { \  
echo mariadb-server-$MARIADB_MAJOR mysql-server/root_password password
'unused'; \  
echo mariadb-server-$MARIADB_MAJOR mysql-server/root_password_again password
'unused'; \  
} | debconf-set-selections \  
&& apt-get update && apt-get install -y nginx \  
php7.0-cli php7.0-common php7.0 php7.0-mysql php7.0-fpm php7.0-curl php7.0-gd
\  
php7.0-intl php7.0-mcrypt php7.0-readline php7.0-tidy php7.0-json
php7.0-sqlite3 \  
php7.0-bz2 php7.0-mbstring php7.0-xml php7.0-zip php7.0-opcache php7.0-bcmath
\  
mariadb-server lsof\  
&& rm -rf /var/lib/apt/lists/*  
#&& apt-get clean && apt-get autoclean && apt-get remove  
COPY my.cnf /etc/mysql/my.cnf  
  
COPY nginx/default.conf /etc/nginx/conf.d/default.conf  
COPY nginx/nginx.conf /etc/nginx/nginx.conf  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY pathfinder.sql /pathfinder.sql  
run mkdir /var/www  
RUN chown -R www-data:www-data /var/www  
  
VOLUME ["/var/lib/mysql"]  
ENV MYSQL_USER=admin \  
MYSQL_PASS=**Random**\  
MYSQL_DATABASE=pathfinder  
  
COPY init.sh /  
EXPOSE 80  
ENTRYPOINT ["/init.sh"]  

