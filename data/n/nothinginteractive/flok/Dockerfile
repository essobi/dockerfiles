# Build a docker container for a test version of Flok  
FROM debian:stable  
MAINTAINER Cast <cast@nothing.ch>  
  
# Install the last nodejs  
COPY nodejs_setup.sh /tmp/  
RUN bash /tmp/nodejs_setup.sh \  
&& apt-get update && apt-get install -y nodejs \  
&& rm -rf /tmp/nodejs_setup.sh  
  
# Install MongoDB  
RUN apt-get update && apt-get install -y mongodb-server \  
&& echo "smallfiles=true" >> /etc/mongodb.conf  
  
# Download and place flok in /srv/http, then install the needed npm module  
RUN mkdir /srv/http && apt-get update && apt-get install -y git bzip2 \  
&& git clone https://github.com/NothingInteractive/flok /tmp/flok \  
&& cd /tmp/flok \  
&& git archive --format=tar --prefix=flok/ HEAD | (cd /srv/http/ && tar xf -)
\  
&& cd /srv/http/flok \  
&& sed 's@https://example.com@@' <config/config-example.js >config/config.js \  
&& npm install \  
&& ./node_modules/.bin/bower --allow-root --silent install \  
&& ./node_modules/.bin/lessc dev/less/flok.less > public/css/flok.css \  
&& rm -rf /tmp/flok && rm -rf dev/ && rm -rf tests/  
  
# Install supervisord to run everything  
RUN apt-get update && apt-get install supervisor -y  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
EXPOSE 3000  
CMD ["/usr/bin/supervisord"]  

