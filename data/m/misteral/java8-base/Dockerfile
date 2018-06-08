# Use phusion/baseimage as base image. To make your builds reproducible, make  
# sure you lock down to a specific version, not to `latest`!  
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for  
# a list of version numbers.  
FROM phusion/baseimage:0.9.15  
# Set correct environment variables.  
ENV HOME /root  
  
# Regenerate SSH host keys. baseimage-docker does not contain any, so you  
# have to do that yourself. You may also comment out this instruction; the  
# init system will auto-generate one during boot.  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
# ---------  
# Install Java.  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
  
# Define working directory.  
WORKDIR /data  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
# Define default command.  
CMD ["bash"]  
  
# ---------  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

