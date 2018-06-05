FROM codelovers/hhvm-mongo  
  
MAINTAINER Daniel Holzmann <daniel@codelovers.at>  
  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -y git sudo  
  
ENV TIMEZONE Europe/Vienna  
  
# update config  
ADD conf/php.ini /etc/hhvm/php.ini  
ADD conf/server.ini /etc/hhvm/server.ini  
RUN echo date.timezone=$TIMEZONE | tee -a /etc/hhvm/server.ini
/etc/hhvm/php.ini  
  
# install nodejs  
RUN curl -sL https://deb.nodesource.com/setup | sudo bash -  
RUN sudo apt-get install -y nodejs ruby  
  
# install coffeescript etc.  
RUN npm install -g coffee-script uglifycss uglify-js bower  
  
# install sass  
RUN gem install sass  
  
# install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN mkdir -p /tmp  
  
RUN git clone https://github.com/CodeLoversAt/search-awesome.git /tmp/search-
awesome  
WORKDIR /tmp/search-awesome  
RUN git checkout hhvm && git pull  
  
# copy config  
ADD conf/parameters.yml /tmp/search-awesome/app/config/parameters.yml  
  
# update config  
ADD conf.sh /tmp/conf.sh  
RUN /tmp/conf.sh  
RUN rm -f /tmp/conf.sh  
  
# make copy of base config  
RUN cp /tmp/search-awesome/app/config/parameters.yml /tmp/search-
awesome/app/config/parameters_base.yml  
  
RUN hhvm /usr/local/bin/composer install  
  
# install bower  
RUN bower install --allow-root  
  
RUN rm -Rf /www  
RUN mv /tmp/search-awesome /www  
  
RUN chown -R www-data:www-data /www  
  
VOLUME /www  
  
WORKDIR /www  

