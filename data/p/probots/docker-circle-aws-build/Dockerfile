FROM phusion/baseimage  
  
RUN apt-get update \  
&& apt-get -y upgrade \  
&& apt-get update --fix-missing \  
&& apt-get install -y --no-install-recommends \  
git \  
python \  
python-pip \  
python-setuptools \  
groff \  
less \  
wget \  
jq \  
php7.0 \  
php7.0-fpm \  
php7.0-common \  
php7.0-cli \  
php7.0-mcrypt \  
php7.0-curl \  
php7.0-bcmath \  
php7.0-mbstring \  
php7.0-json \  
php7.0-xml \  
php7.0-dom \  
php7.0-pdo\  
&& pip install --upgrade setuptools awscli wheel \  
&& wget -qO- https://get.docker.com/ | sh \  
&& usermod -aG docker $(whoami) \  
&& curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  

