# Installs and configures a single-node cassandra cluster suitable for dev  
# If you want your data to be persistent, have docker bind mount  
# /var/lib/cassandra to a persistent location on the host filesystem  
FROM jayofdoom/docker-ubuntu-14.04  
MAINTAINER Jay Faulkner "jay.faulkner@rackspace.com"  
# software-properties-common contains "add-apt-repository" command for PPA
conf  
RUN apt-get update && apt-get install -y software-properties-common curl  
  
# Configure java PPA + Datastax cassandra repositories  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN echo "deb http://debian.datastax.com/community stable main" >
/etc/apt/sources.list.d/cassandra.list  
RUN curl -L https://debian.datastax.com/debian/repo_key | apt-key add -  
RUN apt-get update  
  
# Install and set oracle java 7 as default  
RUN echo "oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true" | debconf-set-selections  
RUN apt-get -y install oracle-java7-installer oracle-java7-set-default  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  
  
# Install cassandra and related utilities  
RUN apt-get install -y libjna-java dsc20 python-cql  
RUN ln -s /usr/share/java/jna.jar /usr/share/cassandra/lib  
  
ADD src/launch_cass.sh /launch_cass.sh  
  
EXPOSE 9160  
CMD ["/bin/sh", "-e", "/launch_cass.sh"]  

