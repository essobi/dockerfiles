FROM ruby:2.4-alpine  
  
MAINTAINER SLAPI Devs  
  
LABEL "description"="New Relic plugin - Currently Supports APM and Servers"  
LABEL "apps"="list APM Apps from New Relic"  
LABEL "servers"="List servers in New Relic"  
  
ENV APP_HOME /newrelic  
  
RUN mkdir -p $APP_HOME && chmod 777 $APP_HOME  
  
WORKDIR /newrelic  
  
# Copy app into container  
COPY . $APP_HOME  
  
RUN apk update && apk add \  
bash &&\  
runDeps="$( \  
scanelf --needed --nobanner --recursive /usr/local \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" &&\  
if [ -f Gemfile.lock ]; then rm -f Gemfile.lock; fi &&\  
apk add --virtual .ruby-builddeps $runDeps \  
build-base \  
linux-headers &&\  
bundle install &&\  
apk del .ruby-builddeps &&\  
rm -rf /var/cache/apk/* &&\  
rm -rf /tmp/*  
  
EXPOSE 4700  
ENTRYPOINT ["rackup", "-E", "production", "-o", "0.0.0.0", "-p", "4700"]  

