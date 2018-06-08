FROM pradeepmuntha/hadoop:latest  
RUN yum install -y which tar sudo openssh-server openssh-clients rsync  
ENV HADOOP_PREFIX /usr/local/hadoop  
ENV JAVA_HOME /usr/local/jdk  
RUN cd /usr/local && curl -SL -k
"http://archive.cloudera.com/cdh5/cdh/5/hadoop-2.6.0-cdh5.7.0.tar.gz" | tar xz
\  
&& ln -s /usr/local/hadoop-2.6.0-cdh5.7.0 /usr/local/hadoop  
RUN cd /usr/local && curl -SL -k "http://download.oracle.com/otn-
pub/java/jdk/8u66-b17/jdk-8u66-linux-x64.tar.gz" -b "oraclelicense=a" \  
| tar xz \  
&& ln -s /usr/local/jdk1.8.0_66 /usr/local/jdk  
COPY config/ /usr/local/hadoop/etc/hadoop/  
RUN groupadd hdfs && useradd -g hdfs -d /home/hdfs -m hdfs && chmod +x
/usr/local/hadoop/etc/hadoop/*env.sh  

