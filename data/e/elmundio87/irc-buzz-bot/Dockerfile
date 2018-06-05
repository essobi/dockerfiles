FROM ubuntu:14.04  
MAINTAINER elmundio87  
  
ADD bot.rb /root/bot.rb  
ADD Gemfile /root/Gemfile  
  
RUN apt-get update  
RUN apt-get install build-essential ruby-full simpleproxy -y  
RUN gem install bundle  
RUN cd /root && bundle install  
  
CMD simpleproxy -L 4000 -R localhost:2000 -d && ruby /root/bot.rb  
  
EXPOSE 4000  

