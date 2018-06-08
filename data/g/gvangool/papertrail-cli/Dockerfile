FROM alpine:3.6  
LABEL maintainer="Gert Van Gool <gert@vangool.mx>"  
  
RUN apk add --no-cache ruby ca-certificates  
# install json gem manually  
RUN apk add --no-cache --virtual ruby-build build-base ruby-dev && \  
gem install --no-document json && \  
apk del ruby-build  
RUN gem install --no-document papertrail  
  
ENTRYPOINT ["papertrail"]  

