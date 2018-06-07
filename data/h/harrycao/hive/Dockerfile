FROM harrycao/hadoop:latest  
  
MAINTAINER caohui <iamcaohui@gmail.com>  
  
WORKDIR /root  
  
RUN mkdir -p /usr/local/hive/ && \  
curl -LO "https://github.com/harrycao/hive-
docker/releases/download/hive-v1.2.2/apache-hive-1.2.2-bin.tar.gz" && \  
tar -xzf ./apache-hive-1.2.2-bin.tar.gz -C /usr/local/hive/ && \  
rm -f ./apache-hive-1.2.2-bin.tar.gz  
  
ENV HIVE_HOME=/usr/local/hive/apache-hive-1.2.2-bin  
ENV PATH=$PATH:$HIVE_HOME/bin  
  
COPY hive-site.xml $HIVE_HOME/conf/  
  
CMD service sshd start; bash  

