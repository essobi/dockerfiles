FROM ruby:alpine  
MAINTAINER Michon van Dooren <michon1992@gmail.com>  
  
RUN apk add \--update --no-cache \  
build-base \  
libxml2-dev \  
libxslt-dev  
RUN bundle config build.nokogiri --use-system-libraries  
RUN gem install nokogiri  
  
ENV PREMAILER_VERSION 1.10.4  
RUN gem install premailer -v "$PREMAILER_VERSION"  
  
CMD ["premailer", "--help"]  

