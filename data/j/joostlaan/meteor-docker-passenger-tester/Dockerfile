# Use phusion/passenger-full as base image. To make your builds reproducible,
make  
# sure you lock down to a specific version, not to `latest`!  
# See https://github.com/phusion/passenger-docker/blob/master/Changelog.md for  
# a list of version numbers.  
FROM phusion/passenger-nodejs:0.9.14  
MAINTAINER Joost van der Laan  
  
# Set correct environment variables.  
ENV HOME /root  
  
# Use baseimage-docker's init process.  
CMD ["/sbin/my_init"]  
  
# install meteor (Only required when NOT using a meteor bundle / build)  
# RUN curl https://install.meteor.com | /bin/sh  
# If you're using the 'customizable' variant, you need to explicitly opt-in  
# for features. Uncomment the features you want:  
# Node.js and Meteor support.  
RUN /build/nodejs.sh  
#RUN /pd_build/nodejs.sh # 0.9.15  
#### DOCKER IN DOCKER START  
# Let's start with some basic stuff.  
RUN apt-get update -qq && apt-get install -qqy \  
apt-transport-https \  
ca-certificates \  
curl \  
lxc \  
iptables  
  
# Install Docker from Docker Inc. repositories.  
RUN curl -sSL https://get.docker.com/ubuntu/ | sh  
####  
# ...put your own build instructions here...  
RUN node -v  
RUN npm -v  
RUN npm cache clean -f && npm install -g n && n 0.10.36  
RUN node -v  
RUN npm -v  
RUN npm install phantomjs  
  
RUN npm install fibers@1.0.5  
RUN npm install underscore  
RUN npm install source-map-support  
RUN npm install semver  
RUN npm install bson  
  
# Add some testing tools  
RUN npm install jshint -g  
  
# Add some deployment tools  
RUN npm install mup  
  
# Deploy the Nginx configuration file for webapp  
#ADD docker/webapp.conf /etc/nginx/sites-enabled/webapp.conf  
#ADD docker/meteor-env.conf /etc/nginx/main.d/meteor-env.conf  
# Remove default nginx host to make the app listen on all domain names  
#RUN rm /etc/nginx/sites-enabled/default  
RUN mkdir /home/app/webapp  
#RUN ...commands to place your web app bundle in /home/app/webapp...  
#ADD ./deploy /home/app/webapp  
# enable NGINX  
#RUN rm -f /etc/service/nginx/down  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

