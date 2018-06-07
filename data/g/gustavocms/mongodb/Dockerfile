# Use phusion/baseimage as base image. To make your builds reproducible, make  
# sure you lock down to a specific version, not to `latest`!  
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for  
# a list of version numbers.  
FROM phusion/baseimage:0.9.10  
# Set correct environment variables.  
ENV HOME /root  
  
# Regenerate SSH host keys. baseimage-docker does not contain any, so you  
# have to do that yourself. You may also comment out this instruction; the  
# init system will auto-generate one during boot.  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Add mongodb org official apt source to the sources list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927  
RUN echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2
multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list  
  
# Install MongoDB  
RUN apt-get update  
RUN apt-get install -y mongodb-org  
  
# Create the MongoDB data directory  
RUN mkdir -p /data/db  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 27017  
EXPOSE 28017  
ENTRYPOINT ["usr/bin/mongod"]  
  

