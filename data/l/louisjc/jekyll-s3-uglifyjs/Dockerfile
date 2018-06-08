FROM ruby  
MAINTAINER louisjc  
  
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash - \  
&& apt-get update \  
&& apt-get install -y \  
default-jre-headless \  
nodejs \  
&& npm install uglify-js -g \  
&& gem install jekyll \  
&& gem install s3_website \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

