# Spoke Dockerfile for {{template}}  
#  
# This is an example Spoke container Dockerfile. If your desired application
is  
# a standard package provided by the radial/distro operating system (Ubuntu  
# Trusty), then this trully is all you would need; just install the package.
All  
# application configuration as well as your application's .ini file is  
# added/cloned/managed by the Hub container.  
FROM radial/spoke-base:latest  
MAINTAINER Brian Clements <radial@brianclements.net>  
  
# Install packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -q update && apt-get -qyV install \  
htop &&\  
apt-get clean  
  
# GH_USER needs to be specified if you have a Github account and want your  
# public keys automatically imported into your container for easy SSH support.  
# This is 'secure' in that use of public keys are always secure, but it is not  
# the wisest strategy to use the same key-pair for multiple venues (server  
# cluster, public website, etc.). More robust key management is a feature for
a  
# future date. For now, this suffices for protypting and development on small  
# clusters. This can be specified here with the ENV instruction, or via  
# commandline at runtime.  
ENV GH_USER brianclements  
  
# A mandatory item is the declaration of the SPOKE_NAME variable. Because the  
# /config/supervisor/conf.d directory is shared by all spokes, individual  
# programs are specifically set to not autostart. As a result, setting this  
# variable will be a unique identifier used by Supervisor to start this Spokes  
# program and not any of the others.  
ENV SPOKE_NAME echos  
  
COPY /entrypoint.sh /entrypoint.sh  
COPY /echos.sh /opt/echos.sh  
# Notice that there is no CMD or ENTRYPOINT. This is because a default  
# ENTRYPOINT is already declared in the 'radial/spoke-base' image. It does
many  
# things that make this container work predictably, so take care when
replacing  
# it in this Spoke Dockerfile.  

