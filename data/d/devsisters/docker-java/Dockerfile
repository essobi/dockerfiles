FROM ubuntu:16.04  
  
ENV DEBIAN_FRONTEND="noninteractive"  
# Install Java.  
RUN \  
# Accept Oracle Java 8 license  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
  
# Add PPA manually without `add-apt-repository` to minimize repo size  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >
/etc/apt/sources.list.d/webupd8team-java-trusty.list && \  
echo "# deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main"
>> /etc/apt/sources.list.d/webupd8team-java-trusty.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 && \  
apt-get update && \  
  
# Install Java  
apt-get install -y --no-install-recommends oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
  
# Define working directory.  
WORKDIR /data  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
# Define default command.  
CMD ["bash"]  

