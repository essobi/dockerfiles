FROM ruby:2.4-alpine3.6  
LABEL vendor="0+X"  
LABEL maintainer="Sebastian Mandrean <sebastian@0x.se>"  
  
WORKDIR /src  
  
# Install dependencies  
RUN apk --no-cache add \  
git \  
make \  
curl \  
curl-dev \  
nodejs \  
ruby-dev \  
build-base && \  
apk --no-cache del wget  
  
ADD entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 4567  

