FROM debian:jessie  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
ca-certificates \  
build-essential \  
wget \  
curl && \  
echo 'deb http://packages.dotdeb.org jessie all' >> /etc/apt/sources.list && \  
echo 'deb-src http://packages.dotdeb.org jessie all' >> /etc/apt/sources.list
&& \  
wget https://www.dotdeb.org/dotdeb.gpg && \  
apt-key add dotdeb.gpg && \  
curl --silent --location https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install -y --no-install-recommends \  
wget \  
unzip \  
mysql-client \  
rsync \  
openssh-client \  
apache2 \  
libapache2-mod-php7.0 \  
php7.0-mbstring \  
php7.0-mcrypt \  
php7.0-mysql \  
php7.0-curl \  
php7.0-gd \  
php7.0-imagick \  
nodejs \  
ssmtp \  
git && \  
npm install -g gulp grunt-cli bower && \  
a2enmod headers rewrite && \  
addgroup --system --gid 1000 user && \  
adduser --system --uid 1000 \--gid 1000 \--shell /bin/bash user && \  
mv /etc/apache2/apache2.conf /etc/apache2/apache2.conf.dist && \  
rm -r /etc/apache2/conf-enabled/ /etc/apache2/sites-enabled/ && \  
mkdir -p /mnt/conf/apache /mnt/www  
  
COPY apache2.conf /etc/apache2/apache2.conf  
COPY start.sh /usr/local/bin/  
COPY index.php /mnt/www/  
  
EXPOSE 80  
CMD ["start.sh"]  

