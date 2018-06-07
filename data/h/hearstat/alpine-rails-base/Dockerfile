FROM ruby:2.3-alpine  
MAINTAINER Hearst Automation Team  
  
# Working directory  
ENV APP_HOME /usr/src/rails  
RUN mkdir -p $APP_HOME  
WORKDIR $APP_HOME  
  
COPY supervisord.conf /etc/supervisor.d/supervisord.conf  
COPY . .  
  
RUN apk update && apk add \  
bash supervisor git nodejs \  
openssl-dev postgresql-dev libpq postgresql-client \  
libxml2-dev libxslt-dev &&\  
runDeps="$( \  
scanelf --needed --nobanner --recursive /usr/local \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" &&\  
apk add --virtual .ruby-builddeps $runDeps \  
build-base ruby-dev libc-dev linux-headers && \  
gem install bundler rails pg puma devise activeadmin &&\  
  
# set up sendmail  
echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories
&&\  
echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories &&\  
echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories &&\  
apk update && apk add exim &&\  
#mkdir -p /var/spool/exim &&\  
#mkdir -p /usr/lib/exim/ &&\  
mkdir -p /var/log/exim &&\  
touch /var/log/exim/mainlog &&\  
chmod 666 /var/log/exim/mainlog &&\  
  
gem cleanup &&\  
rm -rf /var/cache/apk/* &&\  
rm -rf /tmp/*  
  
EXPOSE 3000  
ONBUILD ADD . $APP_HOME  
  
ONBUILD RUN apk update &&\  
if [ -f Gemfile.lock ]; then rm -f Gemfile.lock; fi &&\  
bundle install --without development --binstubs &&\  
yes | bundle exec rails app:update:bin &&\  
bundle exec rake assets:precompile RAILS_ENV=production &&\  
gem cleanup &&\  
apk del .ruby-builddeps &&\  
rm -rf /var/cache/apk/* &&\  
rm -rf /tmp/*  
  
ONBUILD CMD ["supervisord", "-c", "/etc/supervisor.d/supervisord.conf", "-n"]  

