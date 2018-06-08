FROM ruby:2.1-alpine  
  
RUN apk add --update \  
bash \  
vim \  
&& gem install --no-ri --no-rdoc puppet -v '~> 3.0' \  
&& gem install --no-ri --no-rdoc puppet-lint puppet-check reek rubocop \  
&& rm -rf /var/cache/apk/*  
  
WORKDIR /build  
COPY scripts/ /usr/local/bin  

