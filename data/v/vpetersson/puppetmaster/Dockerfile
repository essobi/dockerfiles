# vpetersson/puppetmaster  
#  
# VERSION 0.0.1  
  
FROM ubuntu:14.04  
MAINTAINER Viktor Petersson <vpetersson@wireload.net>  
  
# Refresh apt  
RUN apt-get update && apt-get -y upgrade && apt-get -y install wget && apt-get
clean  
  
# Install Puppet  
RUN wget https://apt.puppetlabs.com/puppetlabs-release-trusty.deb -O
/tmp/puppet-repo.deb && dpkg -i /tmp/puppet-repo.deb && rm /tmp/puppet-
repo.deb && apt-get update && apt-get install -y puppetmaster-passenger &&
apt-get clean  
  
# Clean up certificates  
RUN rm -rf /var/lib/puppet  
  
VOLUME /var/lib/puppet /etc/puppet/modules /etc/puppet/manifests  
  
EXPOSE 8140  
  
ADD start.sh /start.sh  
  
CMD /start.sh  

