FROM ruby:2.4.1-alpine3.6  
MAINTAINER CreatekIO  
  
ENV BUILD_PACKAGES='build-base git mysql-dev nodejs nodejs-npm tzdata inotify-
tools curl'  
RUN \  
apk add --update --upgrade $BUILD_PACKAGES && \  
npm install --global yarn && \  
find / -type f -iname \\*.apk-new -delete && \  
rm -rf /var/cache/apk/* && \  
rm -rf /usr/lib/lib/ruby/gems/*/cache/*  
  
WORKDIR /flight_plan  
  
COPY package.json yarn.lock ./  
RUN yarn install  
  
COPY Gemfile Gemfile.lock ./  
RUN bundle install --jobs 20  

