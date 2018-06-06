FROM radmas/iyc-prod  
  
MAINTAINER fernando.moro@radmas.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
USER root  
  
#################################################  
# PHPUNIT  
  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y \  
phpunit && \  
rm -rf /var/lib/apt/lists/*  
  
#################################################  
# BLACKFIRE.IO  
  
RUN \  
wget -O - https://packagecloud.io/gpg.key | sudo apt-key add -  
  
RUN \  
echo "deb http://packages.blackfire.io/debian any main" | sudo tee
/etc/apt/sources.list.d/blackfire.list  
  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y \  
blackfire-agent \  
blackfire-php && \  
rm -rf /var/lib/apt/lists/*  
  
#################################################  
# SQLITE3  
  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y \  
libsqlite3-dev && \  
rm -rf /var/lib/apt/lists/*  
  
#################################################  
# RUBY (development gems)  
  
RUN gem install bundle mailcatcher --no-rdoc --no-ri  
RUN gem install net-ssh -v 2.9.2 \--no-rdoc --no-ri  
RUN gem install capistrano -v 3.4.0 \--no-rdoc --no-ri  
  
#################################################  
# COMPOSER  
  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
#################################################  
# PHPMETRICS  
  
RUN wget
https://github.com/Halleck45/PhpMetrics/raw/master/build/phpmetrics.phar && \  
chmod +x phpmetrics.phar && \  
mv phpmetrics.phar /usr/local/bin/phpmetrics  
  
#################################################  
# PHP-CODE-FIXER  
  
RUN wget http://get.sensiolabs.org/php-cs-fixer.phar -O php-cs-fixer && \  
chmod a+x php-cs-fixer && \  
mv php-cs-fixer /usr/local/bin/php-cs-fixer  
  
#################################################  
# SSH  
  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y \  
openssh-server && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /var/run/sshd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
#################################################  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
ENV DEBIAN_FRONTEND newt  
  
USER radmas  
  
CMD ["sudo", "/usr/bin/supervisord"]  

