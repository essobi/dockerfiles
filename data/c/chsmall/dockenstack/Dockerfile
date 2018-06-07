# Eric Windisch '2014  
# Forked from code by original author: Paul Czarkowski  
FROM ubuntu:xenial  
MAINTAINER Chris Small "christopher.small@hpe.com"  
EXPOSE 80 5000 8773 8774 8776 9292  
# Set DEBIAN_FRONTEND to avoid warning like "debconf: (TERM is not set, so the
dialog frontend is not usable.)"  
ENV DEBIAN_FRONTEND="noninteractive"  
# Setup devstack user  
RUN mkdir -p /opt; \  
useradd -m -s /bin/bash -d /opt/stack devstack  
ADD devstack.sudo /etc/sudoers.d/devstack  
RUN chown root:root /etc/sudoers.d/devstack  
  
# Requirements  
RUN apt-get update  
  
# Install utilities  
RUN apt-get -qqy install git socat curl sudo vim wget net-tools python-
setuptools uuid-runtime  
  
# Install devstack scripts  
RUN git clone https://github.com/openstack-dev/devstack /devstack  
  
# Install six from pip before getting from global-requirements (due to
bugs...)  
#RUN pip install -U pip  
# Install all pip requirements  
#RUN pip install -r
https://raw.github.com/openstack/requirements/master/global-requirements.txt  
#RUN pip install -r
https://raw.github.com/openstack/tempest/master/requirements.txt  
WORKDIR /devstack  
ADD localrc /devstack/localrc  
ADD localrc.d /devstack/localrc.d  
  
# Install prereq packages.  
RUN /devstack/tools/install_prereqs.sh  
  
# start  
RUN su devstack -c '/devstack/stack.sh'  
  

