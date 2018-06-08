FROM ruby:2.4.1-alpine  
MAINTAINER Nan Liu <nan.liu@gmail.com>  
  
# Install docker, see:  
# https://raw.githubusercontent.com/docker-
library/docker/master/17.03/Dockerfile  
RUN apk add --no-cache \  
ca-certificates \  
curl \  
openssl  
  
ENV DOCKER_BUCKET get.docker.com  
ENV DOCKER_VERSION 17.03.1-ce  
ENV DOCKER_SHA256
820d13b5699b5df63f7032c8517a5f118a44e2be548dd03271a86656a544af55  
  
RUN set -x \  
&& curl -fSL
"https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz" -o
docker.tgz \  
&& echo "${DOCKER_SHA256} *docker.tgz" | sha256sum -c - \  
&& tar -xzvf docker.tgz \  
&& mv docker/* /usr/local/bin/ \  
&& rmdir docker \  
&& rm docker.tgz \  
&& docker -v  
  
COPY docker-entrypoint.sh /usr/local/bin/  
  
# Install our gem dependencies:  
COPY Gemfile /Gemfile  
  
RUN bundle config build.nokogiri --use-system-libraries  
  
RUN apk add --update \  
build-base \  
libxml2-dev \  
libxslt-dev \  
postgresql-dev \  
git \  
&& cd / && bundle install \  
&& apk del build-base postgresql-dev git \  
&& rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["sh"]  

