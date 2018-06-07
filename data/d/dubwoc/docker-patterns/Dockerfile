FROM debian:stable  
MAINTAINER dubwoc <scottz@clevar.me>  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANG en_US.UTF-8  
ENV LC_ALL C.UTF-8  
ENV LANGUAGE en_US.UTF-8  
USER root  
RUN apt-get update && apt-get dist-upgrade -y  
# Make note of current base system packages.  
RUN dpkg --get-selections > /tmp/selections.before  
# Install all the packages you need for development.  
RUN apt-get install -y build-essential  
# Note current state of the system.  
RUN dpkg --get-selections > /tmp/selections.after  
# Diff the two files and produce a list of packages only in the second file.  
RUN grep -F -x -v -f /tmp/selections.before /tmp/selections.after >
/tmp/selections.delete  
# Set all package status to deinstall from install.  
RUN sed -i 's/install/deinstall/' /tmp/selections.delete  
# Perform the following only after you have used the packages that were
installed.  
RUN dpkg --set-selections < /tmp/selections.delete  
RUN apt-get -u dselect-upgrade -y  
  

