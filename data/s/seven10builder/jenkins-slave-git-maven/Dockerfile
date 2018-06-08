# This Dockerfile is used to build an image containing basic stuff to be used
as a Jenkins slave build node.  
FROM seven10builder/jenkins-slave-base:0.2  
MAINTAINER kmilner "kmilner@seven10storage.com"  
ENV MAVEN_VERSION 3.3.3  
RUN curl -fsSL
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share && \  
mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven && \  
ln -s /usr/share/maven/bin/mvn /usr/bin/mvn && \  
apt-get update -q && \  
apt-get install -y git-all && \  
# clean up tmp install files  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean  
  
# Standard SSH port  
EXPOSE 22  
CMD ["/usr/local/bin/setup-docker-and-start-ssh.sh"]  

