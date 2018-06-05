#  
# Oracle Java 8 Dockerfile  
#  
# https://github.com/zishanbilal/beam-dev  
# https://github.com/zishanbilal/beam-dev/tree/master/ci  
#  
# Pull base image.  
FROM ubuntu  
  
  
# Remove any existing JDKs  
RUN apt-get --purge remove openjdk*  
  
  
# Install git and git-lfs.  
RUN \  
apt-get update && \  
apt-get install -y curl git && \  
curl -s https://packagecloud.io/install/repositories/github/git-
lfs/script.deb.sh | bash && \  
apt-get update && \  
apt-get install -y git-lfs=2.3.4  
# Install Java.  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" >
/etc/apt/sources.list.d/webupd8team-java-trusty.list && \  
apt-get update && \  
apt-get install --reinstall ca-certificates && \  
apt-get install -y --no-install-recommends --allow-unauthenticated oracle-
java8-installer  
  
# Cleanup.  
RUN \  
apt-get clean all && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
  
# Define working directory.  
WORKDIR /data  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
ENV GIT_LFS_SKIP_SMUDGE 1  
# Define default command.  
CMD ["bash"]  

