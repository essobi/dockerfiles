FROM debian:jessie  
  
RUN groupadd -r mysql && useradd -r -g mysql mysql  
  
RUN apt-get update \  
&& apt-get -y install software-properties-common wget nano supervisor  
  
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0xcbcb082a1bb943db  
RUN add-apt-repository 'deb [arch=amd64,i386,ppc64el]
http://mariadb.kisiek.net/repo/10.1/ubuntu trusty main'  
  
RUN echo "mariadb-server-10.1 mysql-server/root_password password ''" |
debconf-set-selections  
RUN echo "mariadb-server-10.1 mysql-server/root_password_again password ''" |
debconf-set-selections  
  
RUN apt-get update && apt-get install -y mariadb-server \  
&& sed -ri 's/^user\s/#&/' /etc/mysql/my.cnf /etc/mysql/conf.d/* \  
&& rm -rf /var/lib/mysql && mkdir -p /var/lib/mysql /var/run/mysqld \  
&& chown -R mysql:mysql /var/lib/mysql /var/run/mysqld \  
&& chmod 777 /var/run/mysqld  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_SERVER_NAME localhost  
  
  
  
RUN apt-get update && apt-get install -y apache2  
RUN sed -i 's/APACHE_RUN_USER=www-data/APACHE_RUN_USER=$APACHE_RUN_USER/'
/etc/apache2/envvars  
RUN sed -i 's/APACHE_RUN_GROUP=www-data/APACHE_RUN_GROUP=$APACHE_RUN_GROUP/'
/etc/apache2/envvars  
  
WORKDIR /  
  
RUN mkdir -p $APACHE_RUN_DIR $APACHE_LOCK_DIR $APACHE_LOG_DIR  
  
RUN echo "deb http://packages.dotdeb.org jessie all" >> /etc/apt/sources.list  
RUN echo "deb-src http://packages.dotdeb.org jessie all" >>
/etc/apt/sources.list  
RUN wget https://www.dotdeb.org/dotdeb.gpg  
RUN apt-key add dotdeb.gpg  
  
RUN apt-get update && apt-get install -y libapache2-mod-php7.0 php7.0
php7.0-cgi php7.0-cli php7.0-common php7.0-curl php7.0-dev php7.0-gd
php7.0-gmp php7.0-json php7.0-ldap php7.0-mysql php7.0-odbc php7.0-opcache
php7.0-pgsql php7.0-pspell php7.0-readline php7.0-recode php7.0-snmp
php7.0-sqlite3 php7.0-tidy php7.0-xml php7.0-xmlrpc php-all-dev
libphp7.0-embed php7.0-bcmath php7.0-bz2 php7.0-enchant php7.0-fpm php7.0-imap
php7.0-interbase php7.0-intl php7.0-mbstring php7.0-mcrypt php7.0-phpdbg
php7.0-soap php7.0-sybase php7.0-zip php7.0-xsl  
  
RUN rm -rf /var/lib/apt/lists/*  
  
EXPOSE 80  
EXPOSE 3306  
ADD config/supervisord.conf /etc/webdev/supervisord.conf  
  
ADD config/first_run.sh /first_run.sh  
ADD config/run.sh /run.sh  
  
RUN chmod +x /first_run.sh  
RUN chmod +x /run.sh  
CMD ["bash", "/first_run.sh"]  

