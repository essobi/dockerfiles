FROM ruby:2.3.3  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs  
RUN mkdir /energy_air_bot  
WORKDIR /energy_air_bot  
ADD Gemfile /energy_air_bot/Gemfile  
ADD Gemfile.lock /energy_air_bot/Gemfile.lock  
RUN bundle install  
ADD . /energy_air_bot  

