FROM ruby:2.4  
MAINTAINER Guilherme Maluf <guimalufb@gmail.com>  
  
# throw errors if Gemfile has been modified since Gemfile.lock  
RUN bundle config --global frozen 1  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY Gemfile /usr/src/app/  
COPY Gemfile.lock /usr/src/app/  
RUN bundle install --without development:test  
  
COPY . /usr/src/app  
  
ENV RAILS_ENV docker  
EXPOSE 3000  
CMD ["/bin/bash", "/usr/src/app/run"]  

