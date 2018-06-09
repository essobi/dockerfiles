FROM stickystyle/ubuntu  
MAINTAINER Ryan Parrish <ryan@stickystyle.net>  
  
# Install Java.  
RUN \  
echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
apt-add-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java7-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk7-installer  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  
ADD security/* /usr/lib/jvm/java-7-oracle/jre/lib/security/  
  
CMD ["/bin/bash"]  

