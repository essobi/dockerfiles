FROM smerrill/vagrant-ubuntu-trusty  
MAINTAINER Steven Merrill <steven.merrill@gmail.com>  
  
RUN wget https://apt.puppetlabs.com/puppetlabs-release-trusty.deb -O
/tmp/puppetlabs-release-trusty.deb && \  
dpkg -i /tmp/puppetlabs-release-trusty.deb && \  
apt-get -y update && \  
apt-get -y install puppet=3.4.3-1 puppet-common=3.4.3-1  

