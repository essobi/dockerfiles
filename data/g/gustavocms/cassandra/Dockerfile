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
  
# Install pre-requisite packages  
RUN apt-get update  
RUN apt-get install -y curl libjna-java  
  
# Add Java 7 repo  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee /etc/apt/sources.list.d/webupd8team-java.list  
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty
main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886  
RUN apt-get update  
  
# Preemptively accept the Oracle License  
RUN /bin/echo debconf shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections  
  
# Install Java 7  
RUN apt-get -y install oracle-java7-installer oracle-java7-set-default  
  
# Install Cassandra  
RUN echo "deb http://debian.datastax.com/community stable main" >
/etc/apt/sources.list.d/cassandra.list  
RUN curl -L https://debian.datastax.com/debian/repo_key | apt-key add -  
RUN apt-get update  
RUN apt-get install -y dsc20  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 7199 7000 7001 9160 9042  
# Cassandra has to know the exact local IP it's configured on so we rewrite  
# the configuration at runtime to include it  
CMD ["LOCAL_IP=`ip a s dev eth0 | grep 'inet ' | cut -d/ -f1 | awk '{print
$2}'`"]  
CMD ["sed -i 's/localhost/$LOCAL_IP/' /etc/cassandra/cassandra.yaml"]  
CMD ["sed -i 's/127.0.0.1/$LOCAL_IP/' /etc/cassandra/cassandra.yaml"]  
CMD ["./etc/cassandra/cassandra-env.sh"]  
  
ENTRYPOINT ["/usr/sbin/cassandra -f"]  

