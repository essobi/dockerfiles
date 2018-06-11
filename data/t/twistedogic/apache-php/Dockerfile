FROM google/debian:wheezy  
MAINTAINER Jordan Li <twistedogic@gmail.com>  
  
# Install packages  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y upgrade && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install supervisor pwgen && \  
apt-get -y install git apache2 libapache2-mod-php5 php5-mysql php5-pgsql
php5-gd php-pear php-apc curl && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin && \  
mv /usr/local/bin/composer.phar /usr/local/bin/composer  
  
# Install OpenSSH Server  
RUN \  
apt-get -q -y install openssh-server ;\  
mkdir -p /var/run/sshd ;\  
echo 'root:passw0rd' | chpasswd ;\  
\  
true  
  
# Override default apache conf  
ADD apache.conf /etc/apache2/sites-enabled/000-default.conf  
  
# Enable apache rewrite module  
RUN a2enmod rewrite  
  
EXPOSE 80 22 443  
CMD ["/usr/sbin/sshd","-D"]  

