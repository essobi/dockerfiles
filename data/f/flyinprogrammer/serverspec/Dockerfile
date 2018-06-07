FROM docker:1.12.2  
RUN apk add --no-cache bash git openssh ruby ruby-io-console ruby-bundler
ruby-json && \  
rm -rf /var/cache/apk/* && \  
echo "gem: --no-rdoc --no-ri" > /etc/gemrc && \  
gem install docker-api rake rspec_junit_formatter rubocop serverspec  
RUN mkdir /workdir /root/.ssh  
COPY config /root/.ssh/config  
VOLUME /workdir  
WORKDIR /workdir  
ENTRYPOINT ["/bin/sh", "-c"]  

