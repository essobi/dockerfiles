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
  
ENV HOME /home/www-data  
RUN mkdir -p /home/www-data  
RUN chown -R www-data:www-data /home/www-data  
  
WORKDIR /www  

