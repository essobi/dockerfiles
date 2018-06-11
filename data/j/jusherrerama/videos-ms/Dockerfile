FROM ruby:2.3  
RUN mkdir /videos-ms  
WORKDIR /videos-ms  
ADD Gemfile /videos-ms/Gemfile  
ADD Gemfile.lock /videos-ms/Gemfile.lock  
RUN bundle install  
ADD . /videos-ms  

