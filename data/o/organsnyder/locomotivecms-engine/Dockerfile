# Container for the LocomotiveCMS Engine. LocomotiveCMS Engine is the Ruby on
Rails engine used to serve  
# LocomotiveCMS sites in production.  
#  
# This container is entirely self-sufficient, including both the Engine and
MongoDB. It is currently  
# intended for local development - using it in production would require
additional configuration.  
FROM phusion/baseimage:0.9.15  
MAINTAINER Chris Snyder <chris@snyder616.com>  
  
ENV HOME /root  
CMD ["/sbin/my_init"]  
VOLUME ["/var/log"]  
EXPOSE 8080  
# Install dependencies  
RUN apt-get update && \  
apt-get -y dist-upgrade && \  
apt-get -y install mongodb ruby imagemagick ruby-dev build-essential
libxml2-dev libxslt-dev && \  
gem install bundler rake --no-rdoc && \  
gem install rails --version=3.2.19 --no-rdoc  
  
# Set up Rails environment & install Locomotive  
RUN adduser --system --home /srv/locomotivecms --disabled-password --disabled-
login locomotivecms && \  
mkdir -p /srv/locomotivecms && \  
chown locomotivecms /srv/locomotivecms  
USER locomotivecms  
RUN cd /srv && \  
rails new locomotivecms --skip-active-record --skip-test-unit --skip-
javascript --skip-bundle  
COPY locomotivecms-Gemfile /srv/locomotivecms/Gemfile  
USER root  
RUN cd /srv/locomotivecms && \  
bundle install  
USER locomotivecms  
RUN cd /srv/locomotivecms && \  
bundle exec rails g locomotive:install  
  
# Fix for devise error -
https://groups.google.com/forum/#!topic/locomotivecms/98leJ_A2X5k  
RUN sed -i '4,5 d' /srv/locomotivecms/config/initializers/devise.rb  
  
# Set up services && fix ownerships  
USER root  
RUN mkdir -p /srv/mongodb && \  
chown mongodb:mongodb /srv/mongodb && \  
chown -R locomotivecms /srv/locomotivecms && \  
mkdir -p /etc/service/mongodb /etc/service/locomotivecms  
COPY mongodb.sh /etc/service/mongodb/run  
COPY locomotivecms.sh /etc/service/locomotivecms/run  
  
# Clean up  
RUN apt-get -y remove ruby-dev build-essential && \  
apt-get -y autoremove && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

