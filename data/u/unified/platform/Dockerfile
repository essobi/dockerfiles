# Use lambdalinux/baseimage-amzn as base image.  
# See https://hub.docker.com/r/lambdalinux/baseimage-amzn/tags/ for  
# a list of version numbers.  
FROM amazonlinux  
  
## Use baseimage-amzn's init system  
#CMD ["/sbin/my_init"]  
  
RUN \  
# Update RPM packages  
yum update  
  
# ...put your own build instructions here...  
  
# Clean up YUM when done  
# yum clean all  
#rm -rf /var/cache/yum/* && \  
#rm -rf /tmp/* && \  
#rm -rf /var/tmp/*

