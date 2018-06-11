FROM zetaron/magento-1.9_php-apache  
  
ENTRYPOINT /bin/bash  
  
RUN apt-get update && apt-get install -y \  
wget \  
gzip \  
mysql-client \  
git \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN wget https://getcomposer.org/download/1.2.2/composer.phar \  
&& mv composer.phar /usr/bin/composer \  
&& chmod +x /usr/bin/composer  
  
RUN wget https://files.magerun.net/n98-magerun.phar \  
&& mv n98-magerun.phar /usr/bin/magerun \  
&& chmod +x /usr/bin/magerun  
  
RUN wget -q --no-check-certificate -O /tmp/modman-installer
https://raw.github.com/colinmollenhour/modman/master/modman-installer \  
&& bash < /tmp/modman-installer \  
&& mv ~/bin/modman /usr/bin/modman \  
&& rm /tmp/modman-installer  
  
RUN apt-get update \  
&& curl -sL https://deb.nodesource.com/setup_7.x | bash - \  
&& apt-get install -y \  
nodejs \  
build-essential \  
&& rm -rf /var/lib/apt/lists/*  

