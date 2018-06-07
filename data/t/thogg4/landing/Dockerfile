FROM ruby:2.3.1-alpine  
  
COPY . /app  
WORKDIR /app  
  
RUN bundle install --jobs 3  
  
CMD ["rackup", "/app/config.ru"]  

