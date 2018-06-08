# docker build -f Dockerfile-ubuntu-14.04-puppet4 -t
syseleven/ubuntu-14.04-puppet4 .  
FROM ubuntu:14.04  
MAINTAINER Stefan Andres <s.andres@syseleven.de>  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y \--no-install-recommends ruby2.0
ruby2.0-dev wget \  
# install puppet  
&& wget https://apt.puppetlabs.com/puppetlabs-release-pc1-trusty.deb -O
/tmp/puppet.deb \  
&& dpkg -i /tmp/puppet.deb && apt-get update \  
&& apt-get -y install --no-install-recommends puppet-agent \  
&& rm /etc/init.d/puppet \  
# install sys11 deps  
&& apt-get -y install --no-install-recommends rsyslog nagios-nrpe-server
nagios-plugins-basic nagios-plugins-standard nagios-nrpe-plugin \  
pwgen apt-transport-https software-properties-common cron-apt python bc git
rsync \  
# install kitchen deps  
&& apt-get -y install --no-install-recommends sudo openssh-server curl lsb-
release net-tools locales \  
&& locale-gen en_US.UTF-8 && update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
\  
&& apt-get -y upgrade  
  
ADD myinit /myinit  

