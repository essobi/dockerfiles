FROM ruby:2.4.1-alpine  
  
MAINTAINER SLAPI Devs  
  
ENV APP_HOME /adapter  
  
RUN mkdir -p $APP_HOME && chmod 777 $APP_HOME  
  
WORKDIR /adapter  
  
COPY supervisord.conf /etc/supervisor.d/supervisord.conf  
  
# Copy app into container  
COPY . $APP_HOME  
  
RUN apk update && apk add \  
supervisor \  
openssl &&\  
runDeps="$( \  
scanelf --needed --nobanner --recursive /usr/local \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" &&\  
if [ -f Gemfile.lock ]; then rm -f Gemfile.lock; fi &&\  
apk add --virtual .ruby-builddeps $runDeps \  
ruby-dev \  
build-base \  
linux-headers &&\  
echo 'gem: --no-document' >> /root/.gemrc &&\  
if [ -f Gemfile.lock ]; then rm -f Gemfile.lock; fi &&\  
bundle install &&\  
apk del .ruby-builddeps &&\  
rm -rf /var/cache/apk/* &&\  
rm -rf /tmp/*  
  
EXPOSE 4700  
ENTRYPOINT ["supervisord", "-c", "/etc/supervisor.d/supervisord.conf", "-n"]  

