FROM ruby:2.4  
WORKDIR /app  
  
ADD Gemfile Gemfile.lock /app/  
  
ADD . /app  
  
RUN bundle install --deployment  
  
EXPOSE 80  

