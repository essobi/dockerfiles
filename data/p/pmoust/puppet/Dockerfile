FROM ubuntu:trusty  
MAINTAINER Panagiotis Moustafellos <pmoust@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y wget && \  
wget http://apt.puppetlabs.com/puppetlabs-release-trusty.deb && \  
dpkg -i puppetlabs-release-trusty.deb && \  
rm puppetlabs-release-trusty.deb && \  
apt-get update && \  
apt-get install -y puppet librarian-puppet && \  
apt-get clean  
WORKDIR ['/etc/puppet']  

