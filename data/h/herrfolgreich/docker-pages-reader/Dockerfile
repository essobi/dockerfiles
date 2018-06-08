FROM ruby:2.3-alpine  
  
RUN mkdir -p /var/bundle  
RUN gem install bundler  
  
RUN set -ex \  
&& apk add --no-cache --virtual .run-deps \  
nginx \  
wget \  
ca-certificates \  
tar \  
&& update-ca-certificates  
  
RUN mkdir /app  
  
WORKDIR /app  
  
COPY Gemfile /app/  
  
RUN set -ex \  
&& apk add --no-cache --virtual .build-deps \  
build-base \  
&& bundle install --path /var/bundle \  
\--jobs=2 \  
&& apk del .build-deps  
  
COPY nginx.conf /etc/nginx/nginx.conf  

