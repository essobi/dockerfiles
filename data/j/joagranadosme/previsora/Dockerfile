FROM ruby:2.3  
RUN mkdir /previsora_ms  
WORKDIR /previsora_ms  
  
ADD Gemfile /previsora_ms/Gemfile  
ADD Gemfile.lock /previsora_ms/Gemfile.lock  
  
RUN bundle install  
ADD . /previsora_ms  
  
EXPOSE 3000  

