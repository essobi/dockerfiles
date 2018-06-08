FROM ruby:2.2  
  
MAINTAINER Christian Inzinger <christian@inz.io>  
  
# Install NodeJS, rsync  
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash - \  
&& apt-get update && apt-get install --no-install-recommends -y \  
nodejs \  
rsync \  
&& rm -rf node_modules \  
&& rm -rf /var/lib/apt/lists/*  
# Workaround for Nokogiri build failure,  
# see: https://github.com/sparklemotion/nokogiri/issues/1370  
RUN bundle config build.nokogiri --use-system-libraries  

