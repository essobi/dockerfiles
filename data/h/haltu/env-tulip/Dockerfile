FROM ubuntu:trusty  
MAINTAINER Ilkka Hakkari <ilkka@haltu.fi>  
ENV USER=root DEBIAN_FRONTEND=noninteractive  
RUN echo "%sudo ALL=(ALL:ALL) NOPASSWD: ALL" > /etc/sudoers.d/sudo_nopasswd  
ADD . /srv/salt/base  
VOLUME ["/srv/salt/base"]  
RUN echo 'APT::Install-Recommends "false";' > /etc/apt/apt.conf.d/80haltu  
RUN echo 'APT::Install-Suggests "false";' >> /etc/apt/apt.conf.d/80haltu  
RUN apt-key add /srv/salt/base/SALTSTACK-GPG-KEY.pub &&\  
echo "deb http://repo.saltstack.com/apt/ubuntu/ubuntu14/2015.8 trusty main" >>
/etc/apt/sources.list.d/saltstack.list &&\  
apt-get update &&\  
apt-get install -y --no-install-recommends mercurial salt-minion &&\  
apt-get clean  
RUN ln -s /srv/salt/base/minion.conf /etc/salt/minion.d/base.conf &&\  
salt-call state.highstate &&\  
apt-get clean  
USER foo  
ENV USER=foo  
WORKDIR /home/foo/foo  
CMD /bin/bash  

