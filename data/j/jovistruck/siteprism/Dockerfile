FROM ruby:2.3  
MAINTAINER Joviano Dias <joviano.dias@springer.com>  
  
RUN apt-get update && apt-get install -y apt-utils libfontconfig1-dev libjpeg-
dev  
  
RUN apt-get update  
RUN apt-get install -y curl bzip2 libfreetype6 libfontconfig  
  
# ENV VARS  
ENV PHANTOM_JS_VERSION 2.1.1-linux-x86_64  
  
# PHANTOM JS - Install from source & symlink  
RUN curl -sSL
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOM_JS_VERSION.tar.bz2
| tar xjC /  
RUN ln -s /phantomjs-$PHANTOM_JS_VERSION/bin/phantomjs /usr/bin/phantomjs  
  
###########  
# Below is from
https://github.com/tgjonestx/capybaraDemo/blob/master/dockerImage/Dockerfile  
# Get the basic set of dev tools  
# Add more(firefox,chrome) from this link as and when needed  
RUN apt-get update -qq && apt-get install -y -q build-essential wget unzip
make libxml2 libxslt1-dev libxml2-dev zlib1g-dev  
  
# Install Ruby, Cucumber, Capybara and the other gems we need  
RUN gem install cucumber -v 2.3.2  
RUN gem install nokogiri -v 1.6.7.2  
RUN gem install capybara -v 2.6.2  
RUN gem install capybara-screenshot -v 1.0.11  
RUN gem install poltergeist -v 1.9.0  
RUN gem install rspec -v 3.4.0  
RUN gem install rspec-expectations -v 3.4.0  
RUN gem install selenium-webdriver -v 2.52.0  
RUN gem install site_prism -v 2.9  
RUN gem install pry -v 0.10.3  
RUN gem install phantomjs -v 2.1.1.0  
RUN gem install websocket -v 1.2.2  
RUN gem install multi_json -v 1.11.2  
  
# Install the xvfb for firefox and chrome so they can run on a headless system  
RUN apt-get update -qq && apt-get install -y -q xvfb  
CMD (service xvfb start; export DISPLAY=:99;)  

