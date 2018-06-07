FROM ruby:2.4-alpine  
MAINTAINER William Durand <will+git@drnd.me>  
  
ADD Gemfile /app/  
ADD Gemfile.lock /app/  
  
RUN apk update && apk --update add git openssh build-base ruby-dev tzdata \  
libc-dev libxml2-dev libxslt-dev nodejs && \  
rm -rf /var/cache/apk/* && \  
cd /app ; bundle config build.nokogiri --use-system-libraries ; \  
bundle install --without development test && \  
gem install bundler  
  
WORKDIR /app  
VOLUME ["/app"]  
  
EXPOSE 3030  
CMD ["bundle", "exec", "dashing", "start"]  

