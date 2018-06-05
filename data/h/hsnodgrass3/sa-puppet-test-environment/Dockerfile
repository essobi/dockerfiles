FROM ruby:2.4.3-alpine3.7  
LABEL "maintainer"="Heston Snodgrass heston.snodgrass@connexta.com"  
  
RUN gem install puppet puppet-lint puppet-syntax rake rspec rspec-puppet
rspec-puppet-facts rspec-puppet-utils  
  
RUN mkdir -p /test  
  
WORKDIR /test  
  
ENTRYPOINT ["rake","spec"]  

