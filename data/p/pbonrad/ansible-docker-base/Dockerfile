# Dockerfile for creating a docker image which can be used as a base server  
# for Ansible targets. The image does not contain Ansible itself since it  
# is only a target server which should be provisioned by Ansible. Mainly this  
# is a original distribution with Python installed.  
FROM debian:wheezy  
  
MAINTAINER Peter Bonrad <peter@bonrad.org>  
  
ENV DEBIAN_FRONTEND=noninteractive  
RUN apt-get -qq update && \  
apt-get install -y python sudo apt-transport-https apt-utils  
  
CMD ["/sbin/init"]  

