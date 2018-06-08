FROM ruby:2.4  
# FROM ruby:2.4-alpine # fails in
`/usr/local/bundle/gems/nokogiri-1.7.0.1/ext/nokogiri`  
# throw errors if Gemfile has been modified since Gemfile.lock  
# RUN bundle config --global frozen 1  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY Gemfile /usr/src/app/  
# COPY Gemfile.lock /usr/src/app/  
RUN bundle install  
  
COPY . /usr/src/app  

