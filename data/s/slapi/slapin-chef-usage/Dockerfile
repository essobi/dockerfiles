FROM ruby:2.4-alpine  
  
MAINTAINER SLAPI Devs  
  
LABEL "description"="Displays Chef Node Usage by Org"  
  
RUN mkdir -p /chef-usage && chmod 777 /chef-usage  
WORKDIR /chef-usage  
  
COPY .gemrc /root/.gemrc  
# Copy pager cli to container  
COPY . ./  
# Install dependencies  
RUN apk update && apk add \  
git &&\  
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
  
ENTRYPOINT ["/chef-usage/node_usage.rb"]

