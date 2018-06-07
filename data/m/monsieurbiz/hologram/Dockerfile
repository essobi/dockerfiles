FROM ruby:alpine  
  
RUN apk add --update alpine-sdk  
RUN gem install hologram  
  
VOLUME /work  
WORKDIR /work  
  
ENTRYPOINT ["hologram"]  

