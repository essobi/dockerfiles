FROM ruby:2.3-alpine  
MAINTAINER mdouchement  
  
ARG BUILD_DEPENDENCIES='build-base'  
ENV LANG c.UTF-8  
ENV RAILS_ENV production  
ENV RACK_ENV production  
  
RUN apk upgrade  
RUN apk add --update --no-cache $BUILD_DEPENDENCIES zlib-dev libxml2-dev
libxslt-dev tzdata yaml-dev sqlite-dev mysql-dev  
  
RUN mkdir /data  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
RUN gem install puma  
RUN gem install sqlite3  
RUN gem install pact_broker  
  
RUN apk del $BUILD_DEPENDENCIES  
  
COPY config.ru config.ru  
  
EXPOSE 80  
CMD puma -p 80 config.ru

