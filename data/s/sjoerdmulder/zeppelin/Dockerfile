FROM ubuntu:14.04  
# Users with other locales should set this in their derivative image  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN apt-get update \  
&& apt-get install -y curl unzip \  
python3 python3-setuptools \  
&& ln -s /usr/bin/python3 /usr/bin/python \  
&& easy_install3 pip py4j \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# http://blog.stuart.axelbrooke.com/python-3-on-spark-return-of-the-
pythonhashseed  
ENV PYTHONHASHSEED 0  
ENV PYTHONIOENCODING UTF-8  
ENV PIP_DISABLE_PIP_VERSION_CHECK 1  
# JAVA  
ARG JAVA_MAJOR_VERSION=8  
ARG JAVA_UPDATE_VERSION=112  
ARG JAVA_BUILD_NUMBER=15  
ENV JAVA_HOME /usr/jdk1.${JAVA_MAJOR_VERSION}.0_${JAVA_UPDATE_VERSION}  
  
ENV PATH $PATH:$JAVA_HOME/bin  
RUN curl -sL --retry 3 --insecure \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie;" \  
"http://download.oracle.com/otn-
pub/java/jdk/${JAVA_MAJOR_VERSION}u${JAVA_UPDATE_VERSION}-b${JAVA_BUILD_NUMBER}/server-
jre-${JAVA_MAJOR_VERSION}u${JAVA_UPDATE_VERSION}-linux-x64.tar.gz" \  
| gunzip \  
| tar x -C /usr/ \  
&& ln -s $JAVA_HOME /usr/java \  
&& rm -rf $JAVA_HOME/man  
  
# HADOOP  
ENV HADOOP_VERSION 3.0.0-alpha1  
ENV HADOOP_HOME /usr/hadoop-$HADOOP_VERSION  
ENV HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop  
ENV PATH $PATH:$HADOOP_HOME/bin  
RUN curl -sL --retry 3 \  
"http://archive.apache.org/dist/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz"
\  
| gunzip \  
| tar -x -C /usr/ \  
&& rm -rf $HADOOP_HOME/share/doc \  
&& chown -R root:root $HADOOP_HOME  
  
# SPARK  
ENV SPARK_VERSION 2.1.0  
ENV SPARK_PACKAGE spark-${SPARK_VERSION}-bin-without-hadoop  
ENV SPARK_HOME /usr/spark-${SPARK_VERSION}  
ENV
SPARK_DIST_CLASSPATH="$HADOOP_HOME/etc/hadoop/*:$HADOOP_HOME/share/hadoop/common/lib/*:$HADOOP_HOME/share/hadoop/common/*:$HADOOP_HOME/share/hadoop/hdfs/*:$HADOOP_HOME/share/hadoop/hdfs/lib/*:$HADOOP_HOME/share/hadoop/hdfs/*:$HADOOP_HOME/share/hadoop/yarn/lib/*:$HADOOP_HOME/share/hadoop/yarn/*:$HADOOP_HOME/share/hadoop/mapreduce/lib/*:$HADOOP_HOME/share/hadoop/mapreduce/*:$HADOOP_HOME/share/hadoop/tools/lib/*"  
ENV PATH $PATH:${SPARK_HOME}/bin  
RUN curl -sL --retry 3 \  
"http://d3kbcqa49mib13.cloudfront.net/${SPARK_PACKAGE}.tgz" \  
| gunzip \  
| tar x -C /usr/ \  
&& mv /usr/$SPARK_PACKAGE $SPARK_HOME \  
&& chown -R root:root $SPARK_HOME  
  
WORKDIR $SPARK_HOME  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libsnappy-java \  
&& rm -rf /var/lib/apt/lists/*  
  
# Zeppelin  
ENV ZEPPELIN_PORT 8080  
ENV ZEPPELIN_HOME /usr/zeppelin  
ENV ZEPPELIN_CONF_DIR $ZEPPELIN_HOME/conf  
ENV ZEPPELIN_NOTEBOOK_DIR $ZEPPELIN_HOME/notebook  
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:$HADOOP_HOME/lib/native  
  
WORKDIR $ZEPPELIN_HOME  
  
RUN mkdir -p $ZEPPELIN_HOME \  
&& curl
http://mirrors.supportex.net/apache/zeppelin/zeppelin-0.7.0/zeppelin-0.7.0-bin-
netinst.tgz | tar xz -C $ZEPPELIN_HOME \--strip-components=1 \  
&& bin/install-interpreter.sh --name
md,shell,cassandra,elasticsearch,angular,jdbc  
  
CMD ["bin/zeppelin.sh"]  

