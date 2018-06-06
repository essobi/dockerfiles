FROM docker/compose:1.17.1  
  
MAINTAINER John Allen <john.allen@technekes.com>  
  
RUN \  
apk --no-cache add --virtual .rundeps \  
ca-certificates \  
curl \  
docker \  
git \  
openssh-client \  
openssl \  
parallel \  
ruby \  
ruby-bundler \  
ruby-json && \  
gem install danger --no-document  

