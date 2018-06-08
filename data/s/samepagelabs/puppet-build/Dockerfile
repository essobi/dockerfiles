FROM debian:jessie  
MAINTAINER Petr Baloun <pbaloun@samepage.io>  
  
VOLUME [ "/src" ]  
WORKDIR /src  
  
ENV HOME /tmp  
  
RUN \  
echo "deb http://apt.puppetlabs.com wheezy main" >
/etc/apt/sources.list.d/puppetlabs.tmp.list && \  
apt-get -y --force-yes update && \  
apt-get -y --force-yes install puppetlabs-release && \  
rm /etc/apt/sources.list.d/puppetlabs.tmp.list && \  
apt-get -y update && \  
apt-get -y install ruby puppet && \  
rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*  
  
RUN \  
echo "gem: --no-ri --no-rdoc" > ~/.gemrc && \  
gem install librarian-puppet rake rspec rspec-puppet puppetlabs_spec_helper  

