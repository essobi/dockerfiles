FROM alpine:edge  
  
RUN apk add --no-cache ruby ruby-dev ruby-rdoc ruby-irb ruby-io-console gcc
g++ make && \  
gem install package_cloud  
  
COPY entrypoint.sh /usr/local/bin/  
  
ENTRYPOINT ["entrypoint.sh"]  
  

