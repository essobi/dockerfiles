# Dockerfile for Ember CLI, PhantomJS, and Bower  
FROM sebp/nodejs  
MAINTAINER Sebastien Pujadas http://pujadas.net  
ENV REFRESHED_AT 2015-05-15  
WORKDIR /tmp  
  
### install Ember CLI, PhantomJS, and Bower  
# prerequisites  
RUN apt-get update \  
&& apt-get install -y libfontconfig libfontconfig-dev libfreetype6-dev \  
&& apt-get clean  
  
RUN npm install -g ember-cli@1.13.1 phantomjs bower  
  
### set up  
# For some strange reason Bower doesn't like running  
# without a /var/www directory! Even if we're running  
# it from a completely different directory! Strange!?  
RUN mkdir -p /data/www /var/www \  
&& chown www-data:www-data /var/www /data/www  
  
VOLUME ["/data"]  
WORKDIR /data/www  
  
USER www-data  
ENV HOME /data/www  
  
ENTRYPOINT ["ember"]  
CMD ["help"]  

