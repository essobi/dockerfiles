FROM bigboards/java-8-x86_64  
  
MAINTAINER robinvers <https://github.com/robinvers>  
USER root  
  
# Install Python to support PySpark  
RUN apt-get update && \  
apt-get install -y -q python && \  
curl -s https://d3kbcqa49mib13.cloudfront.net/spark-2.1.1-bin-hadoop2.7.tgz |
tar -xz -C /opt && \  
ln -s /opt/spark-2.1.1-bin-hadoop2.7 /opt/spark && \  
apt-get clean && \  
apt-get autoclean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/*  
# Install pip package manager to include the neo4j-driver  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
python2.7 get-pip.py && \  
pip install neo4j-driver  
  
# master worker  
# +---------+---------+  
EXPOSE 7077 8080 7078 8081  
  
CMD ["/bin/bash"]

