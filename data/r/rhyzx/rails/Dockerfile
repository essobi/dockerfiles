FROM ruby:2.5.1-alpine  
# fix bundle bin?  
# https://github.com/docker-library/ruby/pull/191  
ENV BUNDLE_BIN_DIR="$BUNDLE_BIN" \  
BUNDLE_BIN=  
  
# https://github.com/arwineap/docker-rubyalpine-
nokogiri/blob/master/Dockerfile  
# https://github.com/andrius/alpine-ruby/blob/master/Dockerfile-3.7  
# pre install native extensions like nokogiri pg bcrypt node-sass  
RUN apk add --no-cache --virtual .build-deps \  
build-base \  
libxml2-dev libxslt-dev \  
&& apk add --no-cache tzdata postgresql-dev \  
&& gem install rails -v 5.2.0 \  
&& gem install bcrypt \  
&& rails new /tmp/dummy --database=postgresql --skip-sprockets --webpack
--skip-bundle \  
&& cd /tmp/dummy \  
&& bundle install --without development test \  
&& cp Gemfile.lock / \  
&& cd - \  
&& gem cleanup \  
&& apk del .build-deps \  
&& rm -rf /usr/lib/ruby/gems/*/cache/* \  
/var/cache/apk/* \  
/tmp/* \  
/var/tmp/* \  
~/.bundle/cache  

