FROM php:apache  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927  
RUN echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2
multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list  
  
RUN apt-get update && apt-get install -y --force-yes \  
mongodb-org-tools \  
libssl-dev \  
zlibc  
RUN pecl install mongodb zip && docker-php-ext-enable mongodb && docker-php-
ext-enable zip  
  
RUN a2enmod rewrite  
  
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash -  
RUN apt-get install -y --force-yes nodejs git  
COPY package.json package.json  
RUN npm install bower gulp -g  
RUN npm install  
  
COPY gulpfile.js gulpfile.js  
COPY bower.json bower.json  
RUN bower install --allow-root && gulp build.lib  
  
COPY . /var/www/html/  
RUN mkdir /var/www/html/api/lib/bkp && chmod 777 -R /var/www/html/api/lib/bkp  
RUN gulp build.app  
  
RUN npm uninstall  
RUN apt-get purge -y --force-yes nodejs git && apt-get autoremove -y --force-
yes && apt-get clean all  
  
#RUN a2enmod ssl && a2ensite 000-default default-ssl  
#EXPOSE 443  
ENV MONGO_HOSTNAME mongodb  
ENV MONGO_HOSTPORT 27017

