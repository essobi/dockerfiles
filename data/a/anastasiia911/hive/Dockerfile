FROM anastasiia911/debian-jdk-8:latest  
  
RUN mkdir /home/hive && \  
cd /home/hive && \  
wget http://archive.apache.org/dist/hive/hive-0.12.0/hive-0.12.0-bin.tar.gz &&
\  
tar -xzf hive-0.12.0-bin.tar.gz && \  
rm hive-0.12.0-bin.tar.gz  
  
ENV HIVE_HOME=/home/hive/hive-0.12.0-bin  
CMD ["/bin/bash"]

