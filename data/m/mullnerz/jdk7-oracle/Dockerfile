#  
# Oracle Java 7 Dockerfile  
#  
# https://github.com/mullnerz/docker-images/  
# https://github.com/mullnerz/docker-images/tree/master/jdk7-oracle  
#  
  
FROM mullnerz/ubuntu  
  
MAINTAINER Zoltán Müllner <mullner.zoltan@gmail.com>  
  
# Install oracle-jdk7 and dependencies  
RUN add-apt-repository -y ppa:webupd8team/java && apt-get update && \  
echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install \  
oracle-java7-installer && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk7-installer && \  
echo "JAVA_HOME=/usr/lib/jvm/java-7-oracle" >> /etc/environment  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  
# Define default command  
CMD ["java", "-version"]

