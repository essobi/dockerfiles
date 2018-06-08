FROM gliderlabs/alpine:3.3  
MAINTAINER Nick Stenning  
  
RUN apk add \--no-cache g++ icu-dev make nodejs python  
RUN addgroup -S slackirc && adduser -S -H -G slackirc slackirc  
  
RUN HOME=/tmp npm install -g --production slack-irc  
  
ADD start /start  
  
USER slackirc  
CMD ["/start"]  

