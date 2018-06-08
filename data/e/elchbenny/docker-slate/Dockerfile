FROM ruby:2.4.0-alpine  
MAINTAINER Benjamin Müller <benjamin@7mind.de>  
  
ARG SLATE_VERSION=2.0.0  
RUN apk add --update nodejs && \  
apk add --virtual build-dependencies \  
wget unzip build-base  
  
RUN wget https://github.com/lord/slate/archive/v${SLATE_VERSION}.zip -O
slate.zip && \  
unzip slate.zip -d /slate && \  
cd /slate/slate-${SLATE_VERSION} && \  
bundle install && \  
apk del build-dependencies  
  
WORKDIR /slate/slate-${SLATE_VERSION}  
  
CMD ["bundle", "exec", "middleman", "server"]

