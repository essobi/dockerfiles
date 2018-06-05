FROM circleci/ruby:2.3  
MAINTAINER brendinc <g-creators@brend.co.jp>  
  
RUN echo 'deb http://repo.mysql.com/apt/debian jessie mysql-5.7' | sudo tee
/etc/apt/sources.list.d/mysql57.list && \  
sudo apt-key adv --keyserver pgp.mit.edu --recv-key 5072E1F5 && \  
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash - && \  
sudo apt-get update && \  
sudo apt-get upgrade &&\  
sudo apt-get install curl wget bash git nodejs tzdata libc-dev libxml2-dev
libxslt-dev mysql-client && \  
bundle config build.nokogiri --use-system-libraries && \  
sudo update-alternatives --install /usr/bin/node node /usr/bin/nodejs 10 && \  
gem install bundler --no-document  
  
RUN mkdir ~/repo  
WORKDIR ~/repo  

