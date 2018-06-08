# Builder  
  
FROM ubuntu:15.04  
MAINTAINER Nick Zahn <hi@cloudunder.io>  
  
RUN mkdir ~/.ssh && \  
chmod 0700 ~/.ssh  
  
COPY ssh-config /root/.ssh/config  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh && \  
apt-get update && \  
apt-get install -y \  
curl git rsync ruby libpng-dev \  
php5 php5-cli php5-curl php5-mcrypt && \  
rm -rf /var/lib/apt/lists/* && \  
ln -s /etc/php5/mods-available/mcrypt.ini /etc/php5/cli/conf.d/20-mcrypt.ini
&& \  
gem install sass && \  
curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer  
  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.26.1/install.sh | bash &&
\  
cp -f ~/.nvm/nvm.sh ~/.nvm/nvm-tmp.sh; \  
echo "nvm install 0.12.7; nvm alias default 0.12.7; npm install -g gulp bower"
>> ~/.nvm/nvm-tmp.sh; \  
sh ~/.nvm/nvm-tmp.sh; \  
rm ~/.nvm/nvm-tmp.sh  
  
WORKDIR /code  

