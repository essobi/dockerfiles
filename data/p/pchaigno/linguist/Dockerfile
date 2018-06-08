# linguist  
#  
# VERSION 4.5.5  
FROM debian:stable  
MAINTAINER Paul Chaignon <paul.chaignon@gmail.com>  
  
RUN apt-get update  
RUN apt-get -y install curl libicu-dev cmake bash bundler locales git npm  
  
# Alias for Linguist to work.  
RUN cp /usr/bin/nodejs /usr/bin/node  
  
# Update locales:  
ENV LANG C.UTF-8  
ENV LANGUAGE C.UTF-8  
ENV LC_ALL C.UTF-8  
# Use Bash shell (for 'source').  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Install Ruby using RVM:  
RUN command curl -sSL https://rvm.io/mpapis.asc | gpg --import -  
RUN \curl -sSL https://get.rvm.io | bash -s stable --ruby  
RUN source /etc/profile.d/rvm.sh  
  
# Install and set up Linguist:  
ADD . /linguist  
WORKDIR /linguist  
RUN bundle install  
RUN bundle exec rake samples  
  
# Run tests.  
RUN bundle exec rake  

