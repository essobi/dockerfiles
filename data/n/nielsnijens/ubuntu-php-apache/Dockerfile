FROM ubuntu:trusty  
  
RUN apt-get update && apt-get install -y \  
libapache2-mod-php5 \  
php-pear php5-apcu php5-cli php5-common php5-curl php5-gd php5-imagick \  
php5-imap php5-intl php5-json php5-ldap php5-mongo php5-mysql php5-pgsql \  
php5-readline php5-tidy php5-xdebug php5-xsl php5-dev \  
libcurl4-openssl-dev \  
&& pecl install pecl_http-1.7.6  
  
RUN locale-gen \--purge en_US.UTF-8 && locale-gen en_US && locale-gen
en_US.ISO-8859-15 && locale-gen en_GB.UTF-8 && locale-gen en_GB && locale-gen
en_GB.ISO-8859-15 && locale-gen es_ES && locale-gen es_ES.UTF-8 && locale-gen
es_ES@euro && locale-gen de_DE && locale-gen de_DE.UTF-8 && locale-gen
de_DE@euro && locale-gen fr_FR && locale-gen fr_FR.UTF-8 && locale-gen
fr_FR@euro && locale-gen nl_BE && locale-gen nl_BE.UTF-8 && locale-gen
nl_BE@euro && locale-gen nl_NL && locale-gen nl_NL.UTF-8 && locale-gen
nl_NL@euro && locale-gen pt_BR && locale-gen pt_BR.UTF-8 && locale-gen pt_PT
&& locale-gen pt_PT.UTF-8 && locale-gen pt_PT@euro && locale-gen zh_CN &&
locale-gen zh_CN.GB18030 && locale-gen zh_CN.GBK && locale-gen zh_CN.UTF-8  
  
RUN echo 'extension=http.so' > /etc/php5/mods-available/http.ini  
RUN ln -s ../../mods-available/http.ini /etc/php5/apache2/conf.d/20-http.ini  
  
RUN a2enmod filter deflate mime expires rewrite  
  
COPY resources/etc/apache2-additional.conf /etc/apache2/conf-available/  
RUN ln -s ../conf-available/apache2-additional.conf /etc/apache2/conf-
enabled/z-apache2-additional.conf  
COPY resources/etc/apache2-srv-include.conf /etc/apache2/sites-available/  
RUN ln -s ../sites-available/apache2-srv-include.conf /etc/apache2/sites-
enabled/999-apache2-srv-include.conf  
COPY resources/etc/php5-additional.ini /etc/php5/mods-available/  
RUN ln -s ../../mods-available/php5-additional.ini
/etc/php5/apache2/conf.d/40-php5-additional.ini  
RUN ln -s ../../mods-available/php5-additional.ini
/etc/php5/cli/conf.d/40-php5-additional.ini  
  
RUN rm -R /var/www/ && ln -s /srv/www/ /var/www  
  
COPY resources/bin/apache2-foreground /usr/local/bin/  
RUN chmod +x /usr/local/bin/apache2-foreground  
  
CMD ["apache2-foreground"]  

