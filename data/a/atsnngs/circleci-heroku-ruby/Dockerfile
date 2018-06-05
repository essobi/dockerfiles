FROM circleci/ruby:2.4.1-node  
MAINTAINER Atsushi Nagase<a@ngs.io>  
  
RUN sudo sh -c 'wget https://cli-assets.heroku.com/branches/stable/heroku-
linux-amd64.tar.gz -O heroku.tar.gz && \  
mkdir -p /usr/local/lib && \  
tar -xvzf heroku.tar.gz -C /usr/local/lib && \  
rm -f heroku.tar.gz && \  
/usr/local/lib/heroku/install'  
  
RUN heroku update  
RUN sudo npm install -g yarn  

