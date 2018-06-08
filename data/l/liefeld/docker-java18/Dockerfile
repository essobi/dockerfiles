# copyright 2017-2018 Regents of the University of California and the Broad
Institute. All rights reserved.  
FROM ubuntu  
  
COPY common/container_scripts/*.sh /usr/local/bin/  
  
RUN chmod ugo+x /usr/local/bin/*.sh && \  
apt-get update && apt-get upgrade --yes && \  
apt-get install wget --yes && \  
apt-get install build-essential --yes && \  
apt-get install python-dev --yes && \  
apt-get install software-properties-common python-software-properties --yes &&
\  
wget --no-check-certificate https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
pip install awscli && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer && \  
rm -rf /usr/lib/python3 && \  
rm -rf /usr/lib/python3.5 && \  
rm /usr/lib/jvm/java-8-oracle/javafx-src.zip && \  
rm /usr/lib/jvm/java-8-oracle/src.zip && \  
rm -rf /usr/lib/jvm/java-8-oracle/man && \  
rm /get-pip.py && \  
rm -rf /var/cache/* && \  
apt-get auto-remove perl --yes  
  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
  
CMD ["/usr/local/bin/runS3OnBatch.sh" ]  
  

