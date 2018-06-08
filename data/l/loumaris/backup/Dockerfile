FROM ruby:2.3-alpine  
LABEL maintainer="christian.heimke@loumaris.com"  
  
RUN apk update && apk --update add --virtual build-dependencies build-base
postgresql-dev linux-headers \  
&& apk add tar openssl postgresql  
  
RUN gem install backup -v '~> 4.0' \  
&& gem install rufus-scheduler tzinfo-data  
  
RUN apk del build-dependencies  
  
ADD Backup /backup  
  
WORKDIR /backup  
  
CMD ruby ./scheduler.rb

