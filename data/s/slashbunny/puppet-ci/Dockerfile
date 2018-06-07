FROM ubuntu:16.04  
# Update and Install Packages  
RUN apt-get update -y && apt-get install -y \  
ant \  
git \  
openssh-client \  
rubygems \  
wget  
  
# Install Official Puppet Repository  
RUN wget https://apt.puppetlabs.com/puppetlabs-release-pc1-xenial.deb && \  
dpkg -i puppetlabs-release-pc1-xenial.deb && \  
rm puppetlabs-release-pc1-xenial.deb  
  
# Install Puppet  
RUN apt-get update -y && apt-get install -y puppet-agent  
  
# Install puppet-lint  
RUN gem install puppet-lint  
  
# Clean up unneeded directories  
RUN rm -rf /var/lib/apt/lists/*  
  
# Disable host key checking from within builds as we cannot interactively
accept them  
# TODO: It might be a better idea to bake ~/.ssh/known_hosts into the
container  
RUN mkdir -p ~/.ssh  
RUN printf "Host *\n\tStrictHostKeyChecking no\n\n" > ~/.ssh/config  
  

