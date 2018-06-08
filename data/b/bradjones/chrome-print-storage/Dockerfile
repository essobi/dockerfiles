# Chrome Print - storage  
#
==============================================================================  
# This container provides some shared storage space for our other containers.  
# Out of the box all communication is done via unix sockets not tcp.  
# For smaller single host setups this should work fine. For larger deployments  
# you may like to reconfigure the services to talk via TCP.  
FROM fedora:latest  
MAINTAINER Brad Jones <brad@bjc.id.au>  
  
# Ensure the chrome user can read and write to the /mnt/printed volume  
RUN mkdir -p /mnt/printed && chmod -R 0777 /mnt/printed  
RUN mkdir -p /var/run/xvfb-pool && chmod -R 0777 /var/run/xvfb-pool  
  
# The main php REST api lives in /var/www/html  
# All logs from all containers should end up in /var/log,  
# you may like to setup something like: : http://logstash.net/  
# Our shared sockets will reside in /var/run  
VOLUME ["/var/www/html", "/var/log", "/var/run", "/var/run/xvfb-pool",
"/tmp/.X11-unix", "/mnt/printed"]  
  
# Add some intial data to the shared volumnes above.  
ADD ["container-files","/"]  
  
# Even though we never actually run this container,  
# docker build/create still likes to see a valid executable.  
CMD ["/bin/true"]  

