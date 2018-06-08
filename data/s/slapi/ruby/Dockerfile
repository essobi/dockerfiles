FROM slapi/base:latest  
  
MAINTAINER SLAPI Devs  
  
COPY .gemrc /root  
COPY Gemfile /root  
  
WORKDIR /root  
  
RUN apk update && apk add \  
bash \  
ruby \  
ruby-dev &&\  
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
gem install bundler io-console &&\  
bundle install &&\  
apk del .ruby-builddeps &&\  
rm -rf /var/cache/apk/* &&\  
rm -rf /tmp/*  

