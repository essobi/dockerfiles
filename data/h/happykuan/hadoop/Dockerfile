FROM happykuan/centos  
  
ENV HADOOP_VERSION 2.7.1  
RUN cd /tmp/ && wget http://www-
us.apache.org/dist/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}-src.tar.gz  
  
RUN cd /tmp/ && tar -zxvf hadoop-${HADOOP_VERSION}-src.tar.gz  
  
RUN cd /tmp/hadoop-${HADOOP_VERSION}-src && mvn clean  
  
RUN wget
http://jaist.dl.sourceforge.net/project/findbugs/findbugs/3.0.1/findbugs-3.0.1.tar.gz
-O /tmp/findbugs-3.0.1.tar.gz  
  
RUN tar -zxvf /tmp/findbugs-3.0.1.tar.gz -C /usr/local/  
  
ENV FINDBUGS_HOME=/usr/local/findbugs-3.0.1  
RUN cd /tmp/hadoop-${HADOOP_VERSION}-src && mvn -Pdist,native,docs -DskipTests
-Dtar -Drequire.snappy -Dbundle.snappy -Dsnappy.lib=/usr/lib64 package  

