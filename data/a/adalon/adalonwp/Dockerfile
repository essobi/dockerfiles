# Wordpress 4.7.1 alap telepítés  
FROM ubuntu  
MAINTAINER Szivós Tamás <szivos.tamas@it-droid.hu>  
LABEL Description="Wordpress 4.7.1 alap telepítése nginx, php7.0, mysql, ssh
és supervisor csomagokkal" Vendor="Adalon Solutions Kft." Version="1.0"  
  
# Néhány előkészület a telepítéshez  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
RUN mkdir -p /var/run/sshd  
RUN mkdir -p /run/php  
RUN mkdir -p /var/tmp  
RUN mkdir -p /var/log/supervisor  
  
# Környezeti változók beállítása  
ENV DEBIAN_FRONTEND noninteractive  
ENV INITRD No  
ENV TERM dumb  
  
# Aptitude repo beállítása  
RUN echo "deb http://archive.ubuntu.com/ubuntu xenial main universe" >
/etc/apt/sources.list  
RUN rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
# Alkalmazások telepítése (apache2,php7.0,mariadb10.0,ssh,supervisor)  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get -y install pwgen python-setuptools curl git nano sudo unzip
openssh-server openssl  
RUN apt-get -y install mysql-server mysql-client supervisor nginx php-fpm php-
mysql  
  
# Wordpress követelmények telepítése  
RUN apt-get -y install --force-yes php-xml php-mbstring php-bcmath php-zip
php-pdo-mysql php-curl php-gd php-intl php-pear php-imap php-mcrypt php-
memcache php-apcu php-pspell php-recode php-tidy php-xmlrpc  
  
# SSH login fix. Hogy ne dobjon ki azonnal bejelentkezéskor  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
RUN sed -i "s/PermitRootLogin without-password/PermitRootLogin yes/"
/etc/ssh/sshd_config  
  
# MySQL beállítása  
RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/explicit_defaults_for_timestamp
= true\nbind-address = 0.0.0.0/" /etc/mysql/mysql.conf.d/mysqld.cnf  
  
# nginx beállítása  
RUN sed -i -e"s/user\s*www-data;/user wordpress www-data;/"
/etc/nginx/nginx.conf  
RUN sed -i -e"s/keepalive_timeout\s*65/keepalive_timeout 2/"
/etc/nginx/nginx.conf  
RUN sed -i -e"s/keepalive_timeout 2/keepalive_timeout
2;\n\tclient_max_body_size 100m/" /etc/nginx/nginx.conf  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# php-fpm beállítása  
RUN sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g"
/etc/php/7.0/fpm/php.ini  
RUN sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g"
/etc/php/7.0/fpm/php.ini  
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.0/fpm/php-
fpm.conf  
RUN sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g"
/etc/php/7.0/fpm/pool.d/www.conf  
RUN sed -i -e "s/user\s*=\s*www-data/user = wordpress/g"
/etc/php/7.0/fpm/pool.d/www.conf  
# replace # by ; RUN find /etc/php/7.0/mods-available/tmp -name "*.ini" -exec
sed -i -re 's/^(\s*)#(.*)/\1;\2/g' {} \;  
# nginx site beállítása  
ADD ./wordpress.conf /etc/nginx/sites-available/default  
  
# Supervisor beállítása  
RUN /usr/bin/easy_install supervisor  
RUN /usr/bin/easy_install supervisor-stdout  
ADD ./supervisord.nginx.conf /etc/supervisord.conf  
  
# Rendszer felhasználó létrehozása a Wordpress számára  
RUN useradd -m -d /home/wordpress -p $(openssl passwd -1 'wordpress') -G root
-s /bin/bash wordpress \  
&& usermod -a -G www-data wordpress \  
&& usermod -a -G sudo wordpress \  
&& ln -s /var/www /home/wordpress/www  
  
# Legfrissebb Wordpress telepítése  
ADD http://wordpress.org/latest.tar.gz /var/tmp/latest.tar.gz  
RUN cd /var/tmp/ \  
&& tar xvf latest.tar.gz \  
&& rm latest.tar.gz  
  
RUN mv /var/tmp/wordpress/* /var/www \  
&& chown -R wordpress:www-data /var/www \  
&& chmod -R 775 /var/www  
  
# Wordpress inicializálás és indítás  
ADD ./start.sh /start.sh  
RUN chmod 755 /start.sh  
  
# aptitude tisztítása  
RUN apt-get clean  
RUN rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
# VOLUME meghatározása  
VOLUME ["/var/lib/mysql", "/var/www", "/var/run/sshd"]  
WORKDIR /var/www  
  
# portmappek beállítása  
EXPOSE 9011 3306 80 22  
# Supervisord elindítása  
CMD ["/bin/bash", "/start.sh"]  

