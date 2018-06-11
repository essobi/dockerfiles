FROM phpdockerio/php71-fpm  
  
ENV HOME /root  
COPY . /build  
WORKDIR /tmp  
  
ENV LANG en_US.UTF-8  
ENV NVM_DIR /usr/local/nvm  
ENV NODE_VERSION v8  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh \  
&& apt-get update \  
&& apt-get install -y git curl make telnet tig htop python-pip ssh \  
&& apt-get install -y php7.1-sqlite php7.1-curl php7.1-gd php7.1-mcrypt
php7.1-intl php7.1-mbstring \  
&& apt-get install -y locales \  
&& sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \  
&& dpkg-reconfigure --frontend=noninteractive locales \  
&& update-locale LANG=en_US.UTF-8 \  
&& apt-get install -y mysql-client php7.1-mysql \  
&& apt-get install -y php7.1-mongo mongodb-clients \  
&& pip install ansible \  
&& pip install boto  
  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.33.2/install.sh | bash  
RUN source $NVM_DIR/nvm.sh \  
&& nvm install $NODE_VERSION \  
&& nvm alias default $NODE_VERSION \  
&& nvm use default \  
&& npm install yarn  
  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& mkdir -p /usr/local/bin \  
&& curl -L https://phar.phpunit.de/phpunit-6.0.phar -o /usr/local/bin/phpunit
\  
&& chmod +x /usr/local/bin/phpunit  
  
RUN mkdir -p ~/.ssh \  
&& echo "Host bitbucket.org\n\tStrictHostKeyChecking no\n" >> ~/.ssh/config \  
&& echo "Host github.com\n\tStrictHostKeyChecking no\n" >> ~/.ssh/config  
  
VOLUME /data  
WORKDIR /data  
  
CMD echo "hello world!"  

