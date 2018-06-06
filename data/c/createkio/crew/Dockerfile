FROM ruby:2.5.0-alpine3.7  
MAINTAINER CreatekIO  
  
ENV BUILD_PACKAGES='build-base git nodejs nodejs-npm postgresql-dev
postgresql-client tzdata'  
RUN \  
apk add --update --upgrade $BUILD_PACKAGES && \  
npm install --global yarn && \  
find / -type f -iname \\*.apk-new -delete && \  
rm -rf /var/cache/apk/* && \  
rm -rf /usr/lib/lib/ruby/gems/*/cache/*  
  
WORKDIR /crew  
  
COPY Gemfile Gemfile.lock ./  
  
RUN \  
bundle install --jobs 20  

