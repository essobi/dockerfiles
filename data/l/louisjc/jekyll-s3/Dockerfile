FROM ruby  
MAINTAINER louisjc  
  
RUN apt-get update \  
&& apt-get install -y \  
default-jre-headless \  
nodejs npm \  
&& ln -s /usr/bin/nodejs /usr/bin/node \  
&& npm install uglify-js -g \  
&& gem install jekyll \  
&& gem install s3_website \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

