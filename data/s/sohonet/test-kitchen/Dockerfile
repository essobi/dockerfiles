FROM debian:8  
MAINTAINER johan.vandendorpe@sohonet.co.uk  
  
RUN apt-get update  
RUN apt-get install -y sudo openssh-server curl lsb-release wget  
RUN apt-get upgrade -y  
  
# Kitchen user  
RUN useradd -d /home/kitchen -m -s /bin/bash kitchen  
RUN echo kitchen:kitchen | chpasswd  
RUN echo 'kitchen ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
# Puppet  
RUN wget http://apt.puppetlabs.com/puppetlabs-release-precise.deb  
RUN dpkg -i puppetlabs-release-precise.deb  
RUN apt-get update  
RUN apt-get -y install facter puppet-common puppet  
  
# Install chef client - needed to run tests  
RUN curl -L https://www.opscode.com/chef/install.sh | bash  
  
# Prepare gem cache for kitchen & busser  
RUN GEM_HOME=/tmp/verifier/gems \  
GEM_PATH=/tmp/verifier/gems \  
GEM_CACHE=/tmp/verifier/gems/cache \  
/opt/chef/embedded/bin/gem install \  
\--no-rdoc --no-ri --no-format-executable \  
\--bindir /tmp/verifier/bin --no-user-install \  
bundler \  
busser \  
busser-bash \  
busser-serverspec \  
serverspec \  
serverspec_extensions  
  
RUN mkdir /tmp/verifier/suites  
RUN chown -R kitchen.kitchen /tmp/verifier  

