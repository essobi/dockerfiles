FROM alpine:3.5  
  
LABEL maintainer Steve Crabb <steve@crabb.io>  
  
ENV GITHUB_PAGES_VERSION 138  
  
RUN apk add --update --no-cache \  
build-base \  
libcurl \  
libffi \  
libffi-dev \  
libxml2 \  
libxml2-dev \  
nodejs \  
readline \  
readline-dev \  
ruby \  
ruby-dev \  
ruby-io-console \  
ruby-json \  
ruby-rake \  
yaml \  
yaml-dev \  
zlib \  
zlib-dev  
  
RUN gem install --no-document \  
bundler \  
github-pages:${GITHUB_PAGES_VERSION}  
  
RUN addgroup -g 1000 -S jekyll && \  
adduser -u 1000 -S -H -D -g jekyll -G jekyll jekyll  
  
USER jekyll  
  
VOLUME /srv/jekyll  
  
WORKDIR /srv/jekyll  
  
EXPOSE 4000  
  
CMD github-pages --version && \  
github-pages versions  

