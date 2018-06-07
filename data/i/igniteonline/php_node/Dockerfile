FROM ubuntu:16.10  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
RUN apt-get update \  
&& apt-get install nodejs npm php7.0 php7.0-fpm php7.0-mysql php7.0-xml
php7.0-zip curl git build-essential libssl-dev -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& ln -s /usr/bin/nodejs /usr/bin/node  
RUN echo '{ "allow_root": true }' > /root/.bowerrc  
RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.24.1/install.sh |
sh;  
RUN cp -f ~/.nvm/nvm.sh ~/.nvm/nvm-tmp.sh; \  
echo "nvm install 6; nvm alias default 6" >> ~/.nvm/nvm-tmp.sh; \  
sh ~/.nvm/nvm-tmp.sh; \  
rm ~/.nvm/nvm-tmp.sh;

