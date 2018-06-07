############################################################  
# Dockerfile to build SSHD container images  
# Based on Debian Wheezy  
############################################################  
  
FROM debian:wheezy  
MAINTAINER TheCreeper <loxoko[at]gmail.com>  
  
################## BEGIN INSTALLATION ######################  
  
# Disable installing of recommends and suggests  
RUN echo 'APT::Install-Recommends "0";' > /etc/apt/apt.conf.d/90recommends  
RUN echo 'APT::Install-Suggests "0";' >> /etc/apt/apt.conf.d/90recommends  
  
# Dont perform binary diffs  
RUN echo 'Acquire { Retries "0"; Pdiffs "false"; };' >
/etc/apt/apt.conf.d/50pdiffs  
  
# Update sources and upgrade system  
RUN apt-get update  
RUN apt-get upgrade --yes  
  
# Install some useful utilitys  
RUN apt-get install -y apt-utils supervisor openssh-server vim bzip2 htop
manpages curl sudo libpam-cracklib  
  
# Create dirs  
RUN mkdir -p /var/run/sshd  
RUN mkdir -p /var/log/supervisor  
  
# Add config files  
ADD sshd_config /etc/ssh/sshd_config  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
## Create an administrator user and set password  
RUN groupadd sshusers  
RUN useradd -b /home -m -G sudo,sshusers -s /bin/bash administrator # Generate
a password and print it instead?  
RUN echo administrator:Tc7fjro4 | chpasswd  
################### INSTALLATION END #####################  
  
# Expose some ports  
EXPOSE 22  
  
# Set default container command  
CMD ["/usr/bin/supervisord"]

