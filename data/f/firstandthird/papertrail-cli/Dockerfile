FROM alpine:3.5  
  
RUN apk --no-cache --update add \  
ca-certificates \  
build-base \  
ruby \  
ruby-irb \  
ruby-dev && \  
echo 'gem: --no-document' >> /etc/gemrc && \  
gem install papertrail && \  
gem install json && \  
apk del build-base ruby-dev && \  
rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /usr/lib/ruby/gems/*/cache/*.gem  
  
ENTRYPOINT ["papertrail"]  

