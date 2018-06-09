FROM ruby:2.1  
RUN echo mysql-server-10.0 mysql-server/root_password password
'supers3curePaSswd' | debconf-set-selections  
RUN echo mysql-server-10.0 mysql-server/root_password_again password
'supers3curePaSswd' | debconf-set-selections  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update && apt-get install -y \  
nodejs \  
mariadb-server \  
apache2 \  
apache2-dev \  
libapache2-mod-passenger \  
ruby-dev && rm -rf /var/lib/apt/lists/*  
  
RUN git clone https://github.com/SUSE/Portus.git /portus  
COPY docker-entrypoint.sh /  
  
WORKDIR /portus  
  
# Uncomment these lines and adjust settings in the source repo files to
personalize portus install.  
#COPY portus-config/config.yml /portus/config/config.yml  
#COPY portus-config/database.yml /portus/config/database.yml  
#COPY portus-config/secrets.yml /portus/config/secrets.yml  
# If you already have certificates including intermediate certs, create a
certs folder and move both the key and certs.  
# Uncomment below lines that generate self singed ssl.  
COPY ssl.conf /portus/ssl.conf  
RUN mkdir certs && openssl req -config ssl.conf \  
-new -x509 -nodes -sha256 -days 365 -newkey rsa:4096 \  
-keyout certs/domain.key -out certs/domain.crt  
  
RUN bundle config build.nokogiri --use-system-libraries  
RUN bundle install --retry=3  
RUN gem install passenger:5.0.7 bundler  
RUN chmod o+rw -R /usr/local/bundle  
  
COPY apache-config/sysconfig_apache2 /etc/sysconfig/apache2  
COPY apache-config/httpd.conf /etc/apache2/httpd.conf  
COPY apache-config/portus.conf /etc/apache2/sites-available/000-ssl.conf  
COPY apache-config/000-default.conf /etc/apache2/sites-
available/000-default.conf  
RUN a2enmod rewrite && a2enmod ssl && a2enmod headers && a2enmod proxy &&
a2ensite 000-ssl.conf  
EXPOSE 80 443  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  
  

