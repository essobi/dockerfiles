FROM ruby:2.4  
MAINTAINER Guillermo Guerrero 'guillermo.guerrero@fr.fcm.travel'  
# Install packages  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev curl
imagemagick git  
  
# Install node  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && apt-get install
-y nodejs  
  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update && apt-get install -y yarn  
  
# No rdoc  
RUN echo 'gem: --no-rdoc --no-ri' >> ~/.gemrc  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

