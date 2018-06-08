FROM alpine  
  
RUN set -eux \  
&& apk add --no-cache \  
ca-certificates \  
openssl \  
ruby \  
ruby-bundler \  
ruby-json \  
# dumb-init  
&& VERSION=1.2.0 \  
&& wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v$VERSION/dumb-init_${VERSION}_amd64 \  
&& chmod +x /usr/local/bin/dumb-init  
  
ENTRYPOINT ["dumb-init", "resque-cloudwatch-metrics"]  
WORKDIR /app  
  
COPY Gemfile Gemfile.lock /app/  
RUN bundle install -j4 --frozen  

