#  
# Derived from https://registry.hub.docker.com/u/cmfatih/phantomjs/dockerfile/  
# and adapted to use the official Ruby base image  
# with the addition of ONBUILD triggers to copy the current working directory  
# into a volume and install the bundles.  
#  
# Newer versions of OS have phantomjs available via apt-get  
# but the version used by ruby:1.9.3 [Wheezy] does not.  
#  
# USAGE  
# #####  
# [(re)build the image]  
# docker build -t antonyh/cucumber .  
#  
# [run the image]  
# docker run --rm -it -e HOST="http://server:4503" antonyh/cucumber  
#  
FROM ruby:1.9.3  
MAINTAINER Antony Hutchison <antony@hutchisontechnical.co.uk>  
  
# Env  
ENV PHANTOMJS_VERSION 1.9.7  
# Commands  
RUN \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y git wget libfreetype6 libfontconfig bzip2 && \  
mkdir -p /srv/var && \  
wget -q --no-check-certificate -O /tmp/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2 && \  
tar -xjf /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 -C /tmp && \  
rm -f /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \  
mv /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64/ /srv/var/phantomjs && \  
ln -s /srv/var/phantomjs/bin/phantomjs /usr/bin/phantomjs && \  
git clone https://github.com/n1k0/casperjs.git /srv/var/casperjs && \  
ln -s /srv/var/casperjs/bin/casperjs /usr/bin/casperjs && \  
apt-get autoremove -y && \  
apt-get clean all  
  
RUN gem install cucumber phantomjs bundler capybara selenium-webdriver
poltergeist rspec pry capybara-screenshot  
  
# Define mount points.  
VOLUME ["/data"]  
  
# Define working directory.  
WORKDIR /data  
  
ONBUILD ADD . /data  
# add the requirements to the gem install line instead, otherwise it runs
bundler every single change  
#ONBUILD RUN bundle install  
CMD ["cucumber"]  
  

