FROM alpine:3.4  
MAINTAINER "Miles Goodings <miles.goodings@gmail.com>"  
RUN apk update && apk upgrade && apk --update add \  
ruby ruby-irb ruby-rake ruby-io-console ruby-bigdecimal ruby-json ruby-bundler
\  
libstdc++ tzdata bash mariadb-client-libs && \  
echo 'gem: --no-document' > /etc/gemrc  
  
ADD Gemfile /app/  
ADD Gemfile.lock /app/  
  
RUN apk --update add --virtual build_deps \  
build-base ruby-dev libc-dev linux-headers \  
openssl-dev mysql-dev libxml2-dev libxslt-dev libffi-dev && \  
cd /app ; bundle install && \  
apk del build_deps  
  
ADD . /app  
RUN chown -R nobody:nogroup /app  
USER nobody  
  
ENV RAILS_ENV production  
WORKDIR /app  
  
CMD ["bin/rails", "s", "-p", "3000", "-b", "0.0.0.0"]

