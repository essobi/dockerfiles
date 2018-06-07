# use nodejs in China mainland, according to the silly network environment  
  
FROM epsilony/baseimage  
  
MAINTAINER Man YUAN <epsilony@epsilony.net>  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Install Java.  
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold"
&& apt-get install -y openjdk-7-jdk  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

