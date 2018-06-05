# jgillmanjr/graphNav  
FROM tutum/apache-php:latest  
  
MAINTAINER Jason Gillman Jr. <jason@rrfaae.com>  
  
RUN apt-get update  
#RUN apt-get -y upgrade  
RUN apt-get -y install npm php5-curl  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN npm install -g bower  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin  
  
# Get rid of the default app and install graphNav in development  
RUN rm -rf /app && git clone https://github.com/jgillmanjr/graphNav -b
development /app  
  
# Install dependencies  
WORKDIR /app  
  
RUN bower --allow-root install  
RUN composer install  
  
EXPOSE 80  
WORKDIR /  
CMD ['/run.sh']  

