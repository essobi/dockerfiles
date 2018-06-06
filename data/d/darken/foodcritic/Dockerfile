FROM ruby:alpine  
  
COPY /assets/Gemfile .  
  
RUN apk add --update make g++ ruby-dev libxml2-dev libxslt-dev && rm -rf
/var/cache/apk/* && \  
#bundle config build.nokogiri --use-system-libraries && \  
bundle install  

