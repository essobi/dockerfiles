FROM alpine:3.7  
  
MAINTAINER Dave Hall <skwashd@gmail.com>  
  
# We do all this in one line to reduce the layers and so the image size  
RUN apk update \  
&& apk upgrade \  
&& apk add --no-cache \  
curl \  
git \  
openssl \  
openssh-client \  
php7 \  
php7-curl \  
php7-dom \  
php7-json \  
php7-mbstring \  
php7-mcrypt \  
php7-openssl \  
php7-phar \  
php7-tokenizer \  
python2 \  
py2-pip \  
rsync \  
wget \  
&& rm -rf /var/cache/apk/* \  
&& wget -O /usr/local/bin/composer
https://getcomposer.org/download/1.6.2/composer.phar \  
&& echo
"6706b9ba03e5f1db57285f701e89fc54f2a1b3d6aa64a921699fcd0725a6e80bf659b7aaf7a49fd6a7b3f3521180ea2db2a59282b5b817812635f69d2969d73e
/usr/local/bin/composer" | sha512sum -c - \  
&& chmod +x /usr/local/bin/composer  

