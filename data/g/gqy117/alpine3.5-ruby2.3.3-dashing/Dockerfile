FROM alpine:3.5  
MAINTAINER Leo.Li <gqy117@gmail.com>  
  
ENV RUBY_PACKAGES ruby ruby-io-console ruby-bundler ruby-dev make g++ libffi-
dev nodejs  
  
RUN apk update \  
&& apk add \--no-cache $RUBY_PACKAGES

