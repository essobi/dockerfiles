FROM redis:3-alpine  
  
MAINTAINER SLAPI Devs  
  
ENV APP_HOME /brain  
  
RUN mkdir -p $APP_HOME && chmod 777 $APP_HOME  
  
WORKDIR /brain  
  
COPY supervisord.conf /etc/supervisor.d/supervisord.conf  
  
# Copy app into container  
COPY . $APP_HOME  
  
RUN apk update && apk add \  
supervisor \  
ruby &&\  
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
if [ -f Gemfile.lock ]; then rm -f Gemfile.lock; fi &&\  
echo 'gem: --no-document' >> /root/.gemrc &&\  
gem install bundle &&\  
bundle install &&\  
apk del .ruby-builddeps &&\  
rm -rf /var/cache/apk/* &&\  
rm -rf /tmp/*  
  
EXPOSE 4700  
ENTRYPOINT ["supervisord", "-c", "/etc/supervisor.d/supervisord.conf", "-n"]  

