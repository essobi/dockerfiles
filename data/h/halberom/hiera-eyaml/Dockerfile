FROM alpine:latest  
  
MAINTAINER Gerard Lynch <gerard@halberom.co.uk>  
  
RUN apk add --update --no-cache ruby && \  
gem install --no-ri --no-rdoc hiera-eyaml  
  
ENTRYPOINT ["eyaml"]  

