FROM alpine:3.5  
MAINTAINER the-mast@thoughtworks.com  
  
RUN apk add --update --no-cache gcc g++ make git curl  
RUN apk add --no-cache python nodejs  
RUN apk add --no-cache php5 php5-curl php5-openssl php5-json php5-phar
php5-dom  
RUN npm install --unsafe -g gulp-cli bower node-sass yarn  
RUN apk add --no-cache fontconfig && \  
mkdir -p /usr/share && \  
cd /usr/share \  
&& curl -L https://github.com/Overbryd/docker-phantomjs-
alpine/releases/download/2.11/phantomjs-alpine-x86_64.tar.bz2 | tar xj \  
&& ln -s /usr/share/phantomjs/phantomjs /usr/bin/phantomjs  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer  
  
CMD ["/bin/sh"]  

