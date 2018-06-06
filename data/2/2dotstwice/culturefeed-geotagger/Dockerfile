FROM 2dotstwice/php56-cli  
  
MAINTAINER Kristof Coomans "kristof@2dotstwice.be"  
ENV REFRESHED_AT 2016-06-13  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y --fix-missing -q install curl  
  
RUN curl -sS https://getcomposer.org/installer | sudo php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN mkdir -p /usr/local/culturefeed_geotagger;  
  
COPY composer.json /usr/local/culturefeed_geotagger/composer.json  
COPY composer.lock /usr/local/culturefeed_geotagger/composer.lock  
COPY bin /usr/local/culturefeed_geotagger/bin  
COPY config /usr/local/culturefeed_geotagger/config  
COPY src /usr/local/culturefeed_geotagger/src  
COPY config.yml /usr/local/culturefeed_geotagger/config.yml  
  
RUN cd /usr/local/culturefeed_geotagger; composer install;  
  
CMD ["sh", "-c", "cd /usr/local/culturefeed_geotagger; ./bin/culturefeed-
geotagger.php \  
\--session=/session.json \  
\--search-base-url=http://www.uitid.be/uitid/rest/searchv2 \  
\--entry-base-
url=http://www.uitid.be/uitid/rest/entry/rest.uitdatabank.be/api/v2 \  
tag"]  

