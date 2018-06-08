# Use phusion/baseimage as base image. To make your builds reproducible, make  
# sure you lock down to a specific version, not to `latest`!  
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for  
# a list of version numbers.  
FROM phusion/baseimage:0.9.18  
# Install NFS  
RUN apt-get update && apt-get install -y nfs-common rpcbind  
  
# Copy in init scripts  
ADD init_scripts/* /etc/my_init.d/  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Enable SSH  
#RUN rm -f /etc/service/sshd/down  
# Clean up APT when done.  
#RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

