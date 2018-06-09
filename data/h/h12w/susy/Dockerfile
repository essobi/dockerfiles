FROM ruby:alpine  
MAINTAINER Hǎiliàng Wáng <w@h12.me>  
  
RUN apk add --no-cache \  
build-base  
  
RUN gem install --no-document \  
compass \  
susy \  
breakpoint  
  
WORKDIR /work  
  
ENTRYPOINT [ "compass", "compile", "--force", "--trace", "--output-
style=compressed" ]  

