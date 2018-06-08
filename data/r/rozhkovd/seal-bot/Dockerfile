FROM ruby:2.4.1-alpine  
RUN apk add --no-cache build-base  
COPY . /usr/src/app  
WORKDIR /usr/src/app  
RUN bundle install --without development test  
CMD bundle exec bin/seal.rb  

