FROM debian:wheezy  
MAINTAINER Pierre Brun <pbrun.pro+github@gmail.com>  
  
ENV RELEASE wheezy  
ENV DEBIAN_FRONTEND noninteractive  
ENV SHELL /bin/bash  
  
RUN echo "deb http://packages.dotdeb.org wheezy-php56 all" >>
/etc/apt/sources.list.d/dotdeb.list;echo "deb-src http://packages.dotdeb.org
wheezy-php56 all" >> /etc/apt/sources.list.d/dotdeb.list;wget
http://www.dotdeb.org/dotdeb.gpg;apt-key add dotdeb.gpg;apt-get update;apt-get
-y upgrade  
  
# Install apache, PHP, and supplimentary programs. curl and lynx-cur are for
debugging the container.  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install apache2 libapache2-mod-
php5 php5-mysql php5-gd php-pear php-apc php5-curl curl php5-adodb php-gettext
git acl php5-mcrypt php5-curl jpegoptim php5-gd php5-intl ruby-full build-
essential  
  
# Enable apache mods and uglify*  
RUN curl --silent --location https://deb.nodesource.com/setup_0.12 | bash
-;DEBIAN_FRONTEND=noninteractive apt-get install --yes nodejs;  
RUN a2enmod php5;a2enmod rewrite;npm install -g bower;npm install -g uglify-
js;npm install -g uglifycss;gem install capifony  
  
# Add MySQL  
RUN groupadd -r mysql && useradd -r -g mysql mysql  
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
A4A9406876FCBD3C456770C88C718D3B5072E1F5  
ENV MYSQL_MAJOR 5.7  
ENV MYSQL_VERSION 5.7.8-rc  
RUN echo "deb http://repo.mysql.com/apt/debian/ wheezy
mysql-${MYSQL_MAJOR}-dmr" > /etc/apt/sources.list.d/mysql.list  
RUN { \  
echo mysql-community-server mysql-community-server/data-dir select ''; \  
echo mysql-community-server mysql-community-server/root-pass password ''; \  
echo mysql-community-server mysql-community-server/re-root-pass password ''; \  
echo mysql-community-server mysql-community-server/remove-test-db select
false; \  
} | debconf-set-selections \  
&& apt-get update && apt-get install -y mysql-server="${MYSQL_VERSION}"* && rm
-rf /var/lib/apt/lists/* \  
&& rm -rf /var/lib/mysql && mkdir -p /var/lib/mysql  
  
# comment out a few problematic configuration values  
RUN sed -Ei 's/^(bind-address|log)/#&/' /etc/mysql/my.cnf  
  
COPY docker-entrypoint.sh /entrypoint.sh  
RUN chmod u+x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
VOLUME ["/var/www", "/var/log/apache2", "/etc/apache2", "/var/lib/mysql",
"/tmp"]  
  
COPY scripts/run.sh /run.sh  
RUN chmod +x /run.sh  
  
EXPOSE 3306  
EXPOSE 80  
CMD ["/run.sh"]  

