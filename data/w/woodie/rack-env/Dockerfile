FROM ruby:2.3.0  
EXPOSE 9292  
RUN mkdir /app  
WORKDIR /app  
COPY Gemfile .  
COPY config.ru .  
  
RUN bundle install  
  
ENTRYPOINT ["rackup", "--host", "0.0.0.0"]  

