FROM ruby:2.5  
WORKDIR /app  
EXPOSE 3000  
ADD Gemfile Gemfile.lock /app/  
  
RUN bundle install  
  
ADD . /app/  
  
CMD rails s  

