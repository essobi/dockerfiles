# docker build -t ahoy-api .  
FROM ruby:2.4  
RUN apt-get update && apt-get install -y build-essential nodejs  
# for mysql:  
RUN apt-get install -y mysql-client libmysqlclient-dev  
# clean apt  
RUN apt-get clean  
  
RUN mkdir /ahoy  
WORKDIR /ahoy  
  
ADD Gemfile /ahoy/Gemfile  
ADD Gemfile.lock /ahoy/Gemfile.lock  
  
RUN bundle install  
RUN rails new . --database=mysql --api --skip  

