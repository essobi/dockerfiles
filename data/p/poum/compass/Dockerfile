FROM alpine:latest  
LABEL maintainer "Philippe Poumaroux <poum@cpan.org>"  
  
RUN apk add \--update curl ruby ruby-dev make gcc libc-dev ruby-rdoc ruby-irb
libffi-dev && \  
curl -o /rubygems.gem https://rubygems.org/downloads/rubygems-update-2.7.2.gem
&& \  
gem install --local /rubygems.gem && \  
update_rubygems --no-ri \--no-rdoc && \  
gem uninstall rubygems-update -x && \  
gem install compass && \  
apk del ruby-dev make gcc libc-dev curl libffi-dev && \  
rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["/usr/bin/compass"]  

