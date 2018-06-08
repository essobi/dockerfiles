FROM ruby:2.3.1-alpine  
MAINTAINER andy@betacode.io  
  
RUN apk add --update build-base cmake git && rm -rf /var/cache/apk/*  
  
# Define where the working directory for pronto. This is where the source
codes will be mapped  
ENV PRONTO_ROOT /data  
WORKDIR $PRONTO_ROOT  
  
RUN gem install pronto:${PRONTO_VERSION:-0.7.0}  
RUN gem install pronto-rubocop:${PRONTO_RUBOCOP_VERSION:-0.7.0}  
RUN gem install pronto-flay:${PRONTO_FLAY_VERSION:-0.7.0}  
  
RUN gem install rubocop:${RUBOCOP_VERSION:-0.47.0}  
RUN gem install flay:${FLAY_VERSION:-2.8.1}  
  
CMD [ "pronto", "run" ]  

