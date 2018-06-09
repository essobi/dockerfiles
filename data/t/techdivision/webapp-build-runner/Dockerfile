FROM debian:jessie  
  
RUN apt-get -y update  
  
RUN apt-get -y install g++ make curl git ant php5 php5-curl --fix-missing  
  
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash -  
RUN apt-get install -y nodejs  
  
RUN curl https://install.meteor.com/ | sh  
  
RUN npm install -g node-gyp  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
\  
&& php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'e115a8dc7871f15d853148a7fbac7da27d6c0030b848d9b3dc09e2a0388afed865e6a3d6b3c0fad45c48e2b5fc1196ae')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" \  
&& php composer-setup.php \  
&& php -r "unlink('composer-setup.php');"  
  
RUN echo '#!/bin/bash \n php /composer.phar $*' > /usr/bin/composer  
RUN chmod 755 /usr/bin/composer  
  
RUN echo 'phar.readonly = Off' >> /etc/php5/cli/php.ini  
  
RUN npm install -g bower  
  
RUN npm install -g gulp  
  
# install docker  
RUN apt-get -y install apt-transport-https ca-certificates  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D  
RUN echo "deb https://apt.dockerproject.org/repo debian-jessie main" >
/etc/apt/sources.list.d/docker.list  
RUN apt-get -y update  
RUN apt-cache policy docker-engine  
RUN apt-get -y install docker-engine  
  
#Clean up  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

