FROM ubuntu:latest  
  
RUN apt-get update; apt-get install -y git build-essential ruby-dev ruby-rails
libz-dev libmysqlclient-dev  
  
ADD ./ /data/src/  
  
WORKDIR /data/src/  
  
RUN bundle install  
  
CMD rails db:create db:migrate && rails s -b 0.0.0.0  

