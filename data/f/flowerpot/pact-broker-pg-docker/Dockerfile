FROM ruby:latest  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY Gemfile /usr/src/app/  
RUN bundle install  
  
COPY . /usr/src/app  
  
EXPOSE 5000  
CMD bundle exec thin start -p 5000  
  

