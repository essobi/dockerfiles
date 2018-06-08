FROM ruby:2-alpine  
RUN apk add --update \  
imagemagick \  
build-base \  
libxml2-dev \  
libxslt-dev \  
postgresql-dev \  
&& rm -rf /var/cache/apk/*  
RUN gem install nokogiri:1.6.7 -- --use-system-libraries  
RUN gem install wraith  
RUN mkdir /app  
VOLUME /app  
WORKDIR /app  
ENTRYPOINT ["sh"]

