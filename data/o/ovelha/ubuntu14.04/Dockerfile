FROM ubuntu:14.04  
MAINTAINER Fernando Ribeiro <fernando@finer.com.br>  
  
# Rodando em segundo plano, caso falhe.  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
  
# Update  
RUN apt-get update  
RUN apt-get install -y vim  
  
# Requisitos basicos  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install apache2 libapache2-mod-
php5 php5-mysql php-apc curl git unzip vim-tiny  
  
# Requisitos PHP  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install php5-curl php5-gd
php5-intl php-pear php5-imagick php5-imap php5-mcrypt php5-memcache php5-ming
php5-ps php5-pspell php5-recode php5-sqlite php5-tidy php5-xmlrpc php5-xsl
php5-pgsql  
  
# Configuracao apache  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
RUN chown -R www-data:www-data /var/www/  
  
# Template  
ADD ./template/apache2.conf /etc/apache2/apache2.conf  
ADD ./template/php.ini /etc/php5/apache2/  
ADD ./template/localhost.com.br.conf /etc/apache2/sites-
available/localhost.com.br.conf  
ADD ./template/localhost.com.br.conf /etc/apache2/sites-
available/000-default.conf  
ADD ./template/start.sh /start.sh  
  
# a2enmod & a2ensite  
RUN a2enmod rewrite  
RUN a2ensite localhost.com.br.conf  
  
RUN mkdir -p /var/www/localhost.com.br/public_html/  
RUN usermod -u 1000 www-data  
RUN chown -R www-data:www-data /var/www/localhost.com.br/public_html  
RUN chmod -R 775 /var/www/localhost.com.br/public_html  
RUN chmod +x /start.sh  
RUN a2enmod setenvif headers deflate filter expires rewrite include  
  
# Timezone  
RUN sed -i "s/;date.timezone =.*/date.timezone = America\/Sao_Paulo/"
/etc/php5/apache2/php.ini  
  
# Pegar os Logs de saidas  
RUN ln -sf /dev/stdout /var/log/apache2/localhost.com.br_access.log  
RUN ln -sf /dev/stderr /var/log/apache2/localhost.com.br_error.log  
  
# fix for php5-mcrypt  
RUN /usr/sbin/php5enmod mcrypt  
  
# Instalando JAVA  
RUN \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu precise main" | tee
-a /etc/apt/sources.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu precise main" |
tee -a /etc/apt/sources.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 &&
\  
apt-get update --fix-missing  
  
RUN \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
apt-get install -y oracle-java8-installer &&\  
apt-get clean  
  
RUN echo "JAVA_HOME=/usr/lib/jvm/java-8-oracle" >> /etc/environment  
  
## configurando locale pt_br  
RUN sudo locale-gen "pt_BR.utf8"  
RUN sudo locale-gen "pt_PT.utf8"  
  
EXPOSE 80  
CMD ["/start.sh"]  

