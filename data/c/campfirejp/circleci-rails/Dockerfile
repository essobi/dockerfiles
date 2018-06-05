FROM circleci/ruby:2.5.1-node  
MAINTAINER Atsushi Nagase<ngs@hiinc.jp>  
  
ENV PHANTOMJS_VERSION 2.1.1  
RUN sudo npm install -g yarn  
RUN curl --location --silent
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-${PHANTOMJS_VERSION}-linux-x86_64.tar.bz2
| sudo tar xj -C /usr --strip-components=1  
RUN sudo apt-get install -y fonts-migmix  
RUN sudo npm install -g jshint  
RUN sudo gem update --system 2.7.4 # https://git.io/vAB1b  
RUN sudo gem install bundler --no-rdoc --no-ri  

