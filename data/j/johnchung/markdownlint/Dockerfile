FROM alpine:3.7  
MAINTAINER John Chung <john.chung@geminiopencloud.com>  
  
COPY . /tmp/markdownlint  
COPY .mdlrc /root/  
RUN ls /tmp && apk update && \  
apk add --no-cache ruby git && \  
gem install --no-rdoc --no-ri rake bundler && \  
mkdir /data && cd /tmp/markdownlint && \  
rake install && cd .. && rm -rf markdownlint  
  
VOLUME /data  
WORKDIR /data  
  
ENTRYPOINT ["mdl"]  

