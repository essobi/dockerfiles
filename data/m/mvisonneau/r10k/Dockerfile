FROM ruby:2.4.2-alpine3.6  
ENV R10K_VERSION='2.5.5'  
RUN \  
apk add --no-cache git openssh make ;\  
gem install --no-ri -no-doc minitar-cli r10k:${R10K_VERSION} ;\  
ln -s /usr/local/bundle/gems/r10k-${R10K_VERSION}/bin/r10k /usr/local/bin ;\  
mkdir -p /opt/r10k  
  
ADD Makefile /opt/r10k/Makefile  
  
WORKDIR /opt/r10k  
CMD ["make"]  

