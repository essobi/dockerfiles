# Based on instructions on https://www.dokuwiki.org/install:ubuntu  
  
FROM ubuntu:latest  
  
# Next ARG definition required to remove some debconf warnings during build  
# See http://stackoverflow.com/questions/22466255/is-it-possibe-to-answer-
dialog-questions-when-installing-under-docker  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && \  
apt-get install -y apt-utils \  
wget \  
apache2 \  
libapache2-mod-php7.0 \  
php7.0-xml && \  
apt-get clean && \  
a2enmod rewrite  
  
  
#  
# Install Dokuwiki  
RUN cd /var/www && \  
wget http://download.dokuwiki.org/src/dokuwiki/dokuwiki-stable.tgz && \  
tar xvf dokuwiki-stable.tgz && \  
mv dokuwiki-*/ dokuwiki && \  
rm dokuwiki-stable.tgz && \  
#  
# Modify Apache configuration  
chown -R www-data:www-data /var/www/dokuwiki && \  
cp -p /etc/apache2/sites-enabled/000-default.conf /etc/apache2/sites-
enabled/000-default.conf.orig && \  
sed -r -i 's|^[[:space:]]*DocumentRoot[[:space:]]+/var/www/html|DocumentRoot
/var/www/dokuwiki|1' /etc/apache2/sites-enabled/000-default.conf && \  
sed -r -i 's|^[[:space:]#]*ServerName[[:space:]]+www.example.com|ServerName
wiki.byte13.org|1' /etc/apache2/sites-enabled/000-default.conf  
  
# Alternative tomodify ServerName (or other similar parameters)  
# RUN echo "ServerName localhost" > /etc/apache2/conf-
available/servername.conf && \  
# a2enconf servername  
#  
# Add some files/scripts in image  
# (could be mapped at runtime to a directory containing the files on the
target host)  
RUN mkdir -p /B13/SCRIPTS && \  
chmod -R 750 /B13 /B13/SCRIPTS  
ADD DokuStartup.bash /B13/SCRIPTS  
RUN chmod 750 /B13/SCRIPTS/DokuStartup.bash  
  
#  
# Define container port number for Apache  
EXPOSE 80  
#  
# Define what to start by defaut when running the container  
# ENTRYPOINT ["/usr/sbin/apache2ctl","-D","FOREGROUND","-k","start"]  
CMD ["/usr/sbin/apache2ctl","-D","FOREGROUND","-k","start"]  
# ENTRYPOINT [ "/B13/SCRIPTS/DokuStartup.bash" ]  
# CMD [ "/B13/SCRIPTS/DokuStartup.bash" ]  

