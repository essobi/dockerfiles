FROM ruby:2.1  
MAINTAINER Vladimir Smyshlyaev <v@vforvova.ru>  
  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -  
  
RUN apt-get update  
RUN apt-get install openssh-client xvfb build-essential libssl-dev
libcurl4-openssl-dev libreadline-dev libqtwebkit-dev qt4-qmake nodejs -y  
RUN apt-get clean -qq  
  
RUN gem install bundler --no-ri --no-rdoc  

