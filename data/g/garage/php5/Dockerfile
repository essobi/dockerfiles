FROM garage/base  
  
MAINTAINER Reinaldo Junior <juniorz@gmail.com>  
  
RUN apt-get update && apt-get upgrade -y  
  
RUN /var/garage/install php5-cli  
  
RUN /var/garage/install php5-json php5-readline &&\  
/var/garage/install php5-dev libcurl3-openssl-dev  
  
# Enable creation of phar  
ADD 99-garage.ini /etc/php5/cli/conf.d/99-garage.ini  
  
# Composer  
RUN cd /tmp &&\  
curl -k -sS https://getcomposer.org/installer | php &&\  
mv composer.phar /usr/local/bin/composer &&\  
chmod 0755 /usr/local/bin/composer  
  
# BOX  
#RUN cd /tmp &&\  
# curl -v -L -s http://box-project.org/installer.php | php &&\  
# mv box.phar /usr/local/bin/box &&\  
# chmod 0755 /usr/local/bin/box  
# Boris (it doesn't work on a container)  
#RUN /var/garage/install git-core &&\  
# git clone git://github.com/d11wtq/boris.git /tmp/boris &&\  
# cd /tmp/boris &&\  
# box build &&\  
# mv boris.phar /usr/local/bin/boris &&\  
# chmod 0755 /usr/local/bin/boris  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV GARAGE_PROVIDES php php-config phpize composer

