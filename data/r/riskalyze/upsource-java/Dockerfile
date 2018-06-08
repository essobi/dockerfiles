FROM java:openjdk-8-jre  
  
MAINTAINER Jesse Bye <jbye@riskalyze.com>  
  
ENV UPSOURCE_VERSION 2017.2.2197  
ENV DEBIAN_FRONTEND=noninteractive  
  
WORKDIR /opt  
RUN mkdir -p /home/upsource \  
&& groupadd -g 13001 upsource \  
&& useradd -u 13001 -g upsource -d /home/upsource upsource \  
&& chown -R upsource:upsource /home/upsource \  
&& wget -nv
http://download.jetbrains.com/upsource/upsource-$UPSOURCE_VERSION.zip \  
&& unzip upsource-$UPSOURCE_VERSION.zip \  
&& mv upsource-$UPSOURCE_VERSION /opt/upsource \  
&& rm -rf upsource-$UPSOURCE_VERSION.zip \  
&& chown -R upsource:upsource upsource \  
&& apt-get update && apt-get install -y apt-transport-https \  
lsb-release ca-certificates \  
&& wget -O /etc/apt/trusted.gpg.d/php.gpg
https://packages.sury.org/php/apt.gpg \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- \  
&& echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" >
/etc/apt/sources.list.d/php.list \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update \  
&& apt-get install -y php7.1 \  
&& apt-get install -y python-pip python3 python3-pip libapache2-mod-php7.1 \  
&& apt-get install -y yarn \  
&& curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get install -y nodejs \  
&& php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \  
&& php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" \  
&& php composer-setup.php \  
&& php -r "unlink('composer-setup.php');"  
USER upsource  
EXPOSE 8080  
WORKDIR /opt/upsource  
VOLUME ["/opt/upsource/conf", "/opt/upsource/data", "/opt/upsource/logs",
"/opt/upsource/backups"]  
CMD ["bin/upsource.sh", "run"]  

