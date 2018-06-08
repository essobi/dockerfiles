FROM gitlab/dind  
  
# Define working directory.  
WORKDIR /data  
  
# Install java  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
# Install git  
RUN apt-get install -y git  
  
# Install maven  
ENV MAVEN_HOME="/usr/share/maven"  
ENV MAVEN_VERSION="3.3.9"  
RUN cd / && \  
wget -q
"http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz" -O - | tar xvzf - && \  
mv /apache-maven-$MAVEN_VERSION /usr/share/maven && \  
ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
# Define default command.  
CMD ["bash"]  

