FROM ubuntu  
  
# Make sure we get a colorful command prompt.  
ENV TERM xterm-color  
  
# Set apt-get frontend to "non-interactive" by default.  
ENV DEBIAN_FRONTEND noninteractive  
  
# Disable installing "recommended" and "suggested" packages by default.  
COPY files/no-add-pkg.conf /etc/apt/apt.conf.d/  
  
# Installing the 'apt-utils' package gets rid of the 'debconf: delaying
package configuration, since apt-utils is not installed'  
# error message when installing any other package with the apt-get package
manager.  
RUN apt-get update && apt-get install -y apt-utils  

