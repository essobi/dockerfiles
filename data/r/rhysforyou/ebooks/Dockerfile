FROM ruby:2.2-alpine  
  
RUN apk update && apk add alpine-sdk  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY . /usr/src/app  
RUN bundle install  
  
CMD [ "bundle", "exec", "ebooks", "start" ]  

