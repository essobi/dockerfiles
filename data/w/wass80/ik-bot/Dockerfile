FROM ruby:2.3.0  
EXPOSE 80  
ADD ./Gemfile /app/  
WORKDIR /app  
RUN bundle install  
ADD ./app.rb /app/  
ADD ./views /app/views/  

