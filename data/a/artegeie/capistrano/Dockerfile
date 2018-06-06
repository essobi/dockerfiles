# Capistrano image to be used with https://github.com/marmelab/make-docker-
command  
FROM ubuntu:14.04  
  
ENV HOME /root  
  
# install deps  
RUN apt-get update -qq && \  
apt-get install -y -qq ruby-dev make ssh && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# install capistrano  
RUN gem install --no-rdoc --no-ri capistrano -v 3.2.1  
  
# install deps  
RUN gem install --no-rdoc --no-ri capistrano-symfony -v 0.4.0  
  
WORKDIR /srv

