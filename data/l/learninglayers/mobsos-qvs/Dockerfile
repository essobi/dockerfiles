FROM learninglayers/base  
MAINTAINER Andeas Guth <guth ÄT dbis.rwth-aachen.de>  
  
# Let the container know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update base image  
RUN sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list  
  
run apt-get update -y && apt-get upgrade -y  
run apt-get install -y software-properties-common  
  
# Install java8  
run add-apt-repository -y ppa:openjdk-r/ppa  
run apt-get update -y && apt-get install -y \  
ant \  
dos2unix \  
mysql-client \  
openjdk-8-jdk \  
unzip \  
wget  
  
# Set jdk8 as the default JDK  
RUN ln -fs /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java
/etc/alternatives/java  
  
COPY qvs-entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
CMD ["/entrypoint.sh"]  
  
EXPOSE 8080  

