FROM ubuntu:14.04  
  
RUN printf 'deb http://apt.puppetlabs.com trusty main\ndeb
http://apt.puppetlabs.com trusty dependencies\n'
>/etc/apt/sources.list.d/puppetlabs.list && \  
apt-key adv --keyserver keyserver.ubuntu.com \--recv-key 7F438280EF8D349F && \  
apt-get update && \  
apt-get install --assume-yes --no-install-recommends \  
mcollective-client \  
mcollective-puppet-client && \  
mco --version | grep -F 'mco 2.'  

