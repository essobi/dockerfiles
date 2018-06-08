FROM hashicorp/packer  
  
ENV SERVERSPEC_SHA 69bccd9c8907125f842b59920dc2b526f6f74717  
RUN wget -O /bin/packer-provisioner-serverspec
https://github.com/flyinprogrammer/packer-provisioner-
serverspec/releases/download/1.0/packer-provisioner-serverspec-linux-amd64 \  
&& echo "$SERVERSPEC_SHA /bin/packer-provisioner-serverspec" | sha1sum -c - \  
&& chmod +x /bin/packer-provisioner-serverspec && \  
apk add --no-cache ansible ruby ruby-io-console ruby-bundler ruby-json && rm
-rf /var/cache/apk/* && echo "gem: --no-rdoc --no-ri" > /etc/gemrc && gem
install rake rubocop serverspec rspec_junit_formatter && \  
mkdir /workdir  
  
VOLUME /workdir  
WORKDIR /workdir  
ENTRYPOINT ["/bin/packer"]

