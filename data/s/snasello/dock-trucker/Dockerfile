FROM seapy/ruby:2.1.2  
MAINTAINER ChangHoon Jeong <iamseapy@gmail.com>  
  
# Install AWS and lftp Command Line Interface  
RUN apt-get install -y awscli lftp  
  
WORKDIR /app  
  
#(required) Install App  
ADD Gemfile /app/Gemfile  
ADD Gemfile.lock /app/Gemfile.lock  
RUN bundle install --without development test  
ADD . /app  
  
CMD clockwork clock.rb  

