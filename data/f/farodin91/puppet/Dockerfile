FROM ubuntu:trusty  
  
RUN apt-get update -y  
RUN apt-get install -y wget  
RUN mkdir /puppet  
  
WORKDIR /puppet  
  
RUN wget -q http://apt.puppetlabs.com/puppetlabs-release-trusty.deb  
RUN dpkg -i puppetlabs-release-trusty.deb  
RUN apt-get install -y puppetmaster-passenger  
RUN puppet resource package hiera ensure=installed && puppet resource package
hiera-puppet ensure=installed  
  
ADD hiera.yaml /etc/puppet/hiera.yaml  
  
CMD puppet agent --no-daemonize --verbose

