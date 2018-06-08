FROM ruby:2.2.3  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs  
RUN mkdir /thunderbay  
WORKDIR /thunderbay  
ADD Gemfile /thunderbay/Gemfile  
ADD Gemfile.lock /thunderbay/Gemfile.lock  
RUN bundle install  
ADD . /thunderbay  
ENV RAILS_ENV production  
EXPOSE 3000  
VOLUME /thunderbay  

