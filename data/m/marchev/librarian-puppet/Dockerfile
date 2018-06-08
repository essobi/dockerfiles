FROM ubuntu:15.04  
# Install puppet  
RUN apt-get -y update  
RUN apt-get -y install rubygems || apt-get -y install ruby ruby-dev  
RUN apt-get -y install build-essential  
RUN echo "gem: --no-ri --no-rdoc" > ~/.gemrc  
RUN gem install puppet  
RUN gem install librarian-puppet  
RUN apt-get -y install lsb-release sudo  
  
# Run puppet  
ONBUILD ADD Puppetfile /  
ONBUILD RUN librarian-puppet install  
ONBUILD ADD manifests/site.pp /  
ONBUILD RUN mkdir -p /etc/puppet; touch /etc/puppet/hiera.yaml  
ONBUILD RUN puppet apply --modulepath=/modules site.pp  
ONBUILD RUN rm -fr /Puppetfile /modules /site.pp  

