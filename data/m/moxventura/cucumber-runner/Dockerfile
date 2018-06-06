FROM ruby:2.5.1-alpine3.7  
MAINTAINER Jesper Jeeninga <jesper.jeeninga@trimm.nl>  
RUN \  
apk update && \  
apk upgrade && \  
apk add build-base bash --no-cache && \  
gem install selenium-webdriver -v 3.12.0 && \  
gem install cucumber -v 3.1.0 && \  
gem install gmail -v 0.6.0 && \  
gem install htmlentities -v 4.3.4 && \  
apk del build-base --purge && \  
rm -rf /var/cache/apk/*  
ENTRYPOINT ["bash", "-c"]  

