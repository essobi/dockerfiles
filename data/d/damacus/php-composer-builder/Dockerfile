FROM php:7.1.8-alpine  
  
WORKDIR /opt  
COPY install-composer.sh install-composer.sh  
  
ENV BUILD_PACKAGES bash curl-dev build-base libffi-dev ca-certificates openssl
git openssh  
RUN apk add --no-cache $BUILD_PACKAGES &&\  
update-ca-certificates &&\  
addgroup -S composer &&\  
adduser -S -g composer composer  
RUN chmod +x install-composer.sh  
RUN ./install-composer.sh  
  
USER $user  
WORKDIR /project  
  
ARG PROJECT  
ARG DATE  
ARG DESCRIPTION  
ARG URL  
ARG COMMIT  
ARG user='root'  
LABEL "io.damacus.title"=$PROJECT \  
"io.damacus.created"=$DATE \  
"io.damacus.description"=$DESCRIPTION \  
"io.damacus.url"=$URL \  
"io.damacus.revision"=$COMMIT  

