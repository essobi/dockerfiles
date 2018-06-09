FROM rails:latest  
MAINTAINER Dima Rogov <navydimka@gmail.com>  
  
RUN mkdir /rails-app  
WORKDIR /rails-app  
  
COPY . /rails-app  
RUN bundle install  
  
ENV RAILS_ENV production  
  
CMD bundle exec puma -C config/puma.rb  

