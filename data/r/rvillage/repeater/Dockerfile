# before setup  
FROM ruby:2.5-alpine3.7 AS gem  
  
RUN set -ex \  
&& apk \--update --upgrade add --no-cache \  
build-base \  
libxml2-dev \  
libxslt-dev \  
linux-headers \  
postgresql-dev \  
nodejs \  
yarn \  
tzdata  
  
WORKDIR /usr/src/app  
  
COPY Gemfile Gemfile.lock ./  
RUN bundle install --jobs=4  
  
# setup docker image  
FROM ruby:2.5-alpine3.7  
  
ENV LANG ja_JP.UTF-8  
  
COPY \--from=gem /usr/local/bundle /usr/local/bundle  
COPY \--from=gem /usr/share/zoneinfo/ /usr/share/zoneinfo/  
  
RUN set -ex \  
&& apk \--update --upgrade add --no-cache \  
postgresql-dev \  
nodejs \  
yarn \  
&& cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \  
&& echo "Asia/Tokyo" > /etc/timezone  
  
WORKDIR /usr/src/app  

