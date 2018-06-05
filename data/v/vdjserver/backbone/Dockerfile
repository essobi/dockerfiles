# Base Image  
FROM debian:jessie  
  
MAINTAINER Walter Scarborough <wscarbor@tacc.utexas.edu>  
  
# PROXY: uncomment these if building behind UTSW proxy  
#ENV http_proxy 'http://proxy.swmed.edu:3128/'  
#ENV https_proxy 'https://proxy.swmed.edu:3128/'  
#ENV HTTP_PROXY 'http://proxy.swmed.edu:3128/'  
#ENV HTTPS_PROXY 'https://proxy.swmed.edu:3128/'  
# Install OS Dependencies  
RUN apt-get update && apt-get install -y \  
git \  
nodejs \  
nodejs-legacy \  
npm \  
ruby \  
ruby-dev \  
vim \  
xdg-utils  
  
# PROXY: More UTSW proxy settings  
#RUN npm config set proxy http://proxy.swmed.edu:3128  
#RUN npm config set https-proxy http://proxy.swmed.edu:3128  
RUN npm install -g \  
bower \  
grunt \  
grunt-cli \  
phantomjs  
  
# Install sass dependencies  
RUN gem install \  
sass \  
compass  
  
RUN mkdir /var/www && mkdir /var/www/html && mkdir /var/www/html/vdjserver-
backbone  
  
# Install npm dependencies (optimized for cache)  
COPY ./component/package.json /var/www/html/vdjserver-backbone/  
RUN cd /var/www/html/vdjserver-backbone && npm install  
  
# Install bower dependencies  
COPY ./component/.bowerrc /var/www/html/vdjserver-backbone/  
# PROXY: Copy .bowerrc with proxy settings  
#COPY ./component/.bowerrc.proxy /var/www/html/vdjserver-backbone/.bowerrc  
COPY ./component/bower.json /var/www/html/vdjserver-backbone/  
RUN cd /var/www/html/vdjserver-backbone && bower --allow-root install  
  
# Copy project source  
COPY ./component/ /var/www/html/vdjserver-backbone  
RUN cd /var/www/html/vdjserver-backbone/test && bower --allow-root install  
  
WORKDIR /var/www/html/vdjserver-backbone  
RUN ["/usr/local/bin/grunt","build"]  
  
VOLUME ["/var/www/html/vdjserver-backbone"]  

