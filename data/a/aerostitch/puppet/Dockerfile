####################################  
# Docker box used for puppet client  
####################################  
  
FROM ruby:latest  
  
Maintainer Joseph Herlant<herlantj@gmail.com>  
  
WORKDIR /root  
ENV DEBIAN_FRONTEND "noninteractive"  
  
RUN apt-get update && apt-get dist-upgrade -y -qq && apt-get install wget vim-
nox git -y -qq  
  
RUN wget https://apt.puppetlabs.com/puppetlabs-release-pc1-jessie.deb && \  
dpkg -i puppetlabs-release-pc1-jessie.deb && \  
apt-get update && apt-get install puppet-agent  
  
RUN echo 'PATH="$PATH:/opt/puppetlabs/puppet/bin"' >> /etc/bash.bashrc  
ENTRYPOINT [ "/bin/bash" ]  

