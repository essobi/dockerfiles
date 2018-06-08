FROM ruby:2.4.2-alpine3.6  
LABEL maintainer: "Sergey Shkarupa <s.shkarupa@gmail.com>"  
  
RUN apk --no-cache add build-base nodejs tzdata git  
RUN gem install middleman -v '~> 4.1'  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  

