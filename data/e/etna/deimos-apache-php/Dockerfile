FROM debian:wheezy  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -qq update  
RUN apt-get install -y locales  
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen  
RUN echo "fr_FR.UTF-8 UTF-8" >> /etc/locale.gen  
RUN locale-gen en_US.UTF-8 fr_FR.UTF-8  
  
ENV HOME /root  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV TZ Europe/Paris  
  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y wget  
  
# Installation de PHP depuis Dotdeb  
RUN echo 'deb http://packages.dotdeb.org wheezy all' >> /etc/apt/sources.list  
RUN echo 'deb-src http://packages.dotdeb.org wheezy all' >>
/etc/apt/sources.list  
RUN echo 'deb http://packages.dotdeb.org wheezy-php55 all' >>
/etc/apt/sources.list  
RUN echo 'deb-src http://packages.dotdeb.org wheezy-php55 all' >>
/etc/apt/sources.list  
RUN wget -O - http://www.dotdeb.org/dotdeb.gpg | apt-key add -  
RUN apt-get update  
RUN apt-get install -y php5-cli php5-mysql php5-curl libapache2-mod-php5  
  
RUN echo 'date.timezone = "Europe/Paris"' >> /etc/php5/cli/conf.d/timezone.ini  
RUN echo 'date.timezone = "Europe/Paris"' >>
/etc/php5/apache2/conf.d/timezone.ini  
  
# Installation et configuration d'Apache  
RUN apt-get install -y apache2-mpm-prefork  
RUN a2enmod headers  
RUN a2enmod rewrite  
RUN a2enmod php5  
COPY apache.conf /etc/apache2/sites-enabled/000-default  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2/  
  
# Crée le /app  
RUN ln -s /tmp/mesos-sandbox /app  
  
RUN wget
https://godist.herokuapp.com/projects/ddollar/forego/releases/current/linux-
amd64/forego -O /usr/local/bin/forego  
RUN chmod +x /usr/local/bin/forego  
  
EXPOSE 80  
WORKDIR /app  
ENTRYPOINT ["/usr/local/bin/forego", "start"]  
CMD ["web"]  

