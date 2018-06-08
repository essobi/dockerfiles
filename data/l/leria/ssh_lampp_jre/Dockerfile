FROM debian:jessie  
MAINTAINER Jean-Mathieu Chantrein jean-mathieu.chantrein@univ-angers.fr  
  
# Installation des packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get -yq install \  
apache2 \  
libapache2-mod-php5 \  
makepasswd \  
mysql-server \  
net-tools \  
openjdk-7-jre \  
openssh-server \  
php-apc \  
php5-curl \  
php5-ldap \  
php5-mcrypt \  
php5-mysql \  
postgresql \  
supervisor \  
vim && \  
# Répertoire indispensable au fonctionnement du serveur ssh  
mkdir /var/run/sshd && \  
# Réduction de la taille de l'image  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
# Suppression des bases de données pré-installé  
rm -rf /var/lib/mysql/*  
  

