#  
# Puppet Master running with Apache/Passenger and Librarian-Puppet. No
dashboard, no PuppetDB.  
#  
# This work is based on https://github.com/arcus-io/docker-puppetmaster  
#  
FROM ubuntu:trusty  
MAINTAINER Uri Savelchev <alterrebe@gmail.com>  
  
# Ignore APT warnings about not having a TTY  
ENV DEBIAN_FRONTEND noninteractive  
  
# Ensure UTF-8 locale  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
RUN dpkg-reconfigure locales  
  
# Initialize Ubuntu package system  
RUN echo "deb http://us-east-1.ec2.archive.ubuntu.com/ubuntu/ trusty
multiverse" > /etc/apt/sources.list.d/multiverse.list && \  
echo "deb http://us-east-1.ec2.archive.ubuntu.com/ubuntu/ trusty-updates
multiverse" >> /etc/apt/sources.list.d/multiverse.list && \  
apt-get update -qq && \  
apt-get install -y -qq htop wget  
  
# Install PuppetLabs repo  
RUN wget -q http://apt.puppetlabs.com/puppetlabs-release-trusty.deb -O
/tmp/puppetlabs.deb && \  
dpkg -i /tmp/puppetlabs.deb && rm -f /tmp/puppetlabs.deb && \  
apt-get update -qq  
  
# Install the required packages  
RUN apt-get -y install puppetmaster-passenger ruby-dev make  
RUN gem install --no-ri --no-rdoc librarian-puppet  
  
ADD hiera.yaml /etc/hiera.yaml  
RUN ln -s /etc/hiera.yaml /etc/puppet/hiera.yaml  
  
RUN tar cC /etc/puppet -jf /root/etc-puppet.tar.bz2 .  
ADD run.sh /usr/local/bin/run  
  
EXPOSE 8140  
CMD ["/usr/local/bin/run"]  
VOLUME /etc/puppet  

