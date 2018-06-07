FROM ubuntu:trusty  
MAINTAINER Alex Sherwin <alex.sherwin@gmail.com>  
  
# Taken from https://github.com/tripit/slate  
# Modified to not include source directly into this image, making it a
reusable authentication server  
RUN apt-get update  
RUN apt-get install -yq ruby ruby-dev build-essential git  
RUN gem install --no-ri --no-rdoc bundler  
ADD Gemfile /app/Gemfile  
ADD Gemfile.lock /app/Gemfile.lock  
RUN cd /app; bundle install  
  
EXPOSE 4567  
WORKDIR /app  
  
CMD ["bundle", "exec", "middleman", "server"]  

