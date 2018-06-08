FROM alpine:3.2  
MAINTAINER John Doe <john@doe.com>  
  
RUN apk update && apk upgrade  
RUN apk add bash curl-dev ruby-dev build-base  
RUN apk add ruby ruby-bundler ruby-io-console  
  
RUN rm -rf /var/cache/apk/*  
  
RUN mkdir /usr/app  
WORKDIR /usr/app  
  
#COPY Gemfile /usr/app/  
#COPY Gemfile.lock /usr/app/  
#RUN bundle install  
RUN ruby -v  
RUN gem -v  
#RUN gem install rdoc  
RUN gem install license_finder  
RUN license_finder  
  
COPY . /usr/app  

