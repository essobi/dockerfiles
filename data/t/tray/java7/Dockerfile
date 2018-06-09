# 12.04 is the latest LTS release, see https://wiki.ubuntu.com/LTS  
FROM ubuntu:12.04  
# Oracle Java 7  
RUN apt-get update && apt-get install -y python-software-properties  
RUN add-apt-repository ppa:webupd8team/java && apt-get update && echo oracle-
java7-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && apt-get install -y oracle-java7-installer
&& rm -f /var/cache/oracle-jdk7-installer/*.tar.gz
/usr/lib/jvm/java-7-oracle/src.zip  

