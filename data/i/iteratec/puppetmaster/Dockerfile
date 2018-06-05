FROM debian:7  
MAINTAINER infrastruktur-ham@iteratec.de  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
RUN apt-get update && \  
apt-get install -y wget apt-utils ca-certificates locales locales-all  
  
RUN wget https://apt.puppetlabs.com/puppetlabs-release-wheezy.deb && \  
dpkg -i puppetlabs-release-wheezy.deb && \  
apt-get update  
  
RUN apt-get install -y puppetserver=1.0.0-1puppetlabs1 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY puppet.conf /etc/puppet/puppet.conf  
  
VOLUME ["/etc/puppet"]  
VOLUME ["/var/lib/puppet"]  
  
EXPOSE 8140  
ENTRYPOINT [ "/usr/bin/puppet", "master", "--no-daemonize", "--verbose" ]  

