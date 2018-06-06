FROM ruby:2.3  
RUN mkdir /credit_cards_ms  
WORKDIR /credit_cards_ms  
ADD Gemfile /credit_cards_ms/Gemfile  
ADD Gemfile.lock /credit_cards_ms/Gemfile.lock  
RUN bundle install  
ADD . /credit_cards_ms  

