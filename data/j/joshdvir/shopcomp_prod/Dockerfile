FROM alpine:3.3  
MAINTAINER Shuky Dvir <shuky@devops.co.il>  
  
RUN mkdir -p /shopcomp  
WORKDIR /shopcomp  
  
ADD Gemfile /shopcomp/Gemfile  
ADD Gemfile.lock /shopcomp/Gemfile.lock  
  
RUN apk add --update \  
ca-certificates \  
supervisor \  
bash \  
ruby-dev \  
ruby-raindrops \  
libxml2 \  
libxml2-dev \  
libxslt \  
libxslt-dev \  
nodejs \  
ruby-nokogiri \  
ruby-io-console \  
ruby-mysql2 \  
ruby-irb \  
ruby-bigdecimal \  
git  
  
RUN apk add --update \  
curl-dev \  
mariadb-dev \  
openssl-dev \  
build-base \  
&& gem install bundler --no-document \  
&& bundle config --global path "$GEM_HOME" \  
&& bundle config --global bin "$GEM_HOME/bin" \  
&& bundle config --global \--jobs 32 \  
&& bundle install --without test development doc --deployment --retry=3 \  
&& apk del --update build-base openssl-dev curl-dev mariadb-dev \  
&& apk add --update libstdc++ \  
&& rm -rf /var/cache/apk/*  
  
RUN curl -Ls https://github.com/fgrehm/docker-
phantomjs2/releases/download/v2.0.0-20150722/dockerized-phantomjs.tar.gz \  
| tar xz -C /  

