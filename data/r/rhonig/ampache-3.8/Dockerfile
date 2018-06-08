FROM ubuntu:14.04  
MAINTAINER Afterster  
  
RUN echo 'deb http://download.videolan.org/pub/debian/stable/ /' >>
/etc/apt/sources.list  
RUN echo 'deb-src http://download.videolan.org/pub/debian/stable/ /' >>
/etc/apt/sources.list  
RUN echo 'deb http://archive.ubuntu.com/ubuntu trusty main multiverse' >>
/etc/apt/sources.list  
  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install wget  
RUN wget -O - http://download.videolan.org/pub/debian/videolan-apt.asc|sudo
apt-key add -  
RUN apt-get update  
  
# Need this environment variable otherwise mysql will prompt for passwords  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install mysql-server apache2
wget php5 php5-json php5-curl php5-mysqlnd pwgen lame libvorbis-dev vorbis-
tools flac libmp3lame-dev libavcodec-extra* libfaac-dev libtheora-dev libvpx-
dev libav-tools  
  
# For local testing / faster builds  
# COPY master.tar.gz /opt/master.tar.gz  
ADD https://github.com/ampache/ampache/archive/3.8.0-beta2.tar.gz
/opt/master.tar.gz  
  
# extraction / installation  
RUN rm -rf /var/www/* && \  
tar -C /var/www -xf /opt/master.tar.gz ampache-3.8.0-beta2 --strip=1 && \  
chown -R www-data /var/www  
  
# setup mysql like this project does it: https://github.com/tutumcloud/tutum-
docker-mysql  
# Remove pre-installed database  
RUN rm -rf /var/lib/mysql/*  
ADD create_mysql_admin_user.sh /create_mysql_admin_user.sh  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
ENV MYSQL_PASS **Random**  
# Add VOLUMEs to allow backup of config and databases  
VOLUME ["/etc/mysql", "/var/lib/mysql"]  
  
# setup apache with default ampache vhost  
ADD 001-ampache.conf /etc/apache2/sites-available/  
RUN rm -rf /etc/apache2/sites-enabled/*  
RUN ln -s /etc/apache2/sites-available/001-ampache.conf /etc/apache2/sites-
enabled/  
RUN a2enmod rewrite  
  
VOLUME ["/media"]  
VOLUME ["/var/www/config"]  
VOLUME ["/var/www/themes"]  
EXPOSE 80  
CMD ["/run.sh"]  

