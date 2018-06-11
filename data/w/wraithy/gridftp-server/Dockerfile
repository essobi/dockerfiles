FROM phusion/baseimage  
MAINTAINER wraith.andrew@gmail.com  
  
# Download and install the globus toolkit  
RUN apt-get update  
RUN apt-get install -y wget  
WORKDIR /tmp  
RUN wget http://www.globus.org/ftppub/gt6/installers/repo/globus-toolkit-
repo_latest_all.deb  
RUN dpkg -i globus-toolkit-repo_latest_all.deb  
RUN apt-get update  
RUN apt-get install -y \  
globus-gridftp  
  
# Enable gridftp  
RUN globus-gridftp-server-enable-sshftp  
  
# Enable SSH  
RUN rm -f /etc/service/sshd/down  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
WORKDIR /  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  

