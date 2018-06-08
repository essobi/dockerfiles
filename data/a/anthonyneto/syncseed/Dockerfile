FROM alpine:latest  
RUN apk add --update rsync openssh-client ruby bash vim && rm -rf
/var/cache/apk/*  
RUN gem install --no-ri --no-rdoc net-ssh  
RUN gem install --no-ri --no-rdoc rubysl-shellwords  
RUN mkdir -p /data  
RUN mkdir -p /root/.ssh  
ADD run.rb /run.rb  
  
CMD ruby run.rb  

