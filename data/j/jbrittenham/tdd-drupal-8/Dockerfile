FROM webdevops/php-apache:alpine-php7  
  
RUN touch ~/.bashrc  
  
# Add testing repo to get latest apk packages  
RUN echo "ipv6" >> /etc/modules  
  
# Add repos  
RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/main >>
/etc/apk/prepositories  
RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories  
RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/community >>
/etc/apk/repositories  
  
# We need this repo to install php7-imagick b/c the other repos are not
working properly  
ADD https://php.codecasts.rocks/php-alpine.rsa.pub /etc/apk/keys/php-
alpine.rsa.pub  
RUN echo http://php.codecasts.rocks/7.0 >> /etc/apk/repositories  
  
# Update compu  
RUN apk update  
  
# Add packages  
RUN apk --update add \  
automake \  
autoconf \  
aws-cli \  
bash \  
curl \  
g++ \  
graphicsmagick \  
nasm \  
libtool \  
libjpeg \  
libpng-dev \  
libpng \  
imagemagick-dev \  
imagemagick \  
make \  
nodejs \  
openssh \  
php7-soap \  
php7-imagick \  
python2 \  
rsync \  
zlib \  
yarn  
  
# Install Bower & Gulp  
RUN npm install -g bower gulp  
  
# Install NVM  
RUN wget -qO-
https://raw.githubusercontent.com/creationix/nvm/v0.31.1/install.sh | bash  

