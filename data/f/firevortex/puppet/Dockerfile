FROM ubuntu:16.04  
  
ENV
PATH=/opt/puppetlabs/server/bin:/opt/puppetlabs/puppet/bin:/opt/puppetlabs/bin:$PATH  
ENV DEBIAN_FRONTEND noninteractive  
  
LABEL org.label-schema.vendor="Puppet" \  
org.label-schema.name="Puppet Server" \  
org.label-schema.version="2.7.2"  
  
RUN export LANGUAGE=en_US.UTF-8 && \  
export LANG=en_US.UTF-8 && \  
export LC_ALL=en_US.UTF-8 && \  
locale-gen en_US.UTF-8 && \  
apt-get update && \  
apt-get -y install wget && \  
apt-get -y install apt-utils && \  
wget https://apt.puppetlabs.com/puppetlabs-release-pc1-xenial.deb && \  
dpkg -i puppetlabs-release-pc1-xenial.deb && \  
rm -f puppetlabs-release-pc1-xenial.deb && \  
apt-get update && \  
apt-get -y install puppetserver=2.7.2-1puppetlabs1 && \  
apt-get -y install git && \  
puppet resource package puppetdb-termini ensure=latest && \  
puppetserver gem install hiera-regex && \  
/opt/puppetlabs/puppet/bin/gem install r10k && \  
gem install hiera-regex && \  
apt-get clean autoclean && \  
apt-get autoremove -y  
  
RUN echo "export PS1='\e[1;33m[\u@\h:\w]\$\e[m '" >> ~/.bashrc && \  
install -d -o puppet -g puppet -m 771 /etc/puppetlabs-ssl  
  
EXPOSE 8140  
  
ENTRYPOINT [ "puppet", "master", "--no-daemonize", "--verbose" ]

