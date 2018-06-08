FROM debian:jessie  
  
LABEL maintainer "opsxcq@strm.sh"  
  
RUN bash -c 'debconf-set-selections <<< "mariadb-server mysql-
server/root_password password rootpass" '  
RUN bash -c 'debconf-set-selections <<< "mariadb-server mysql-
server/root_password_again password rootpass" '  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
apache2 \  
php5 php5-gd php5-mysql \  
mysql-server \  
zip \  
libxml2-dev libpng-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN service mysql start; mysql --password=rootpass -e 'create database smf;'  
  
COPY src /var/www  
RUN cd /var/www && \  
  
RUN useradd --system --uid 666 -M --shell /usr/sbin/nologin forum  
  
USER forum  
  
EXPOSE 80  
CMD service mysql start; apache2-foreground  

