FROM ubuntu:15.04  
MAINTAINER Yi Jin "http://jinyi.me" "Fork From
https://github.com/gettyimages/docker-spark"  
ENV SPARK_VERSION=1.5.2 \  
HADOOP_PROFILE=2.6  
ENV HADOOP_VERSION=2.6.3  
LABEL SPARK_VERSION="$SPARK_VERSION" \  
HADOOP_VERSION="$HADOOP_VERSION"  
# Users with other locales should set this in their derivative image  
RUN locale-gen "en_US.UTF-8"  
  
ENV LANG=en_US.UTF-8 \  
LANGUAGE=en_US:en \  
LC_ALL=en_US.UTF-8  
RUN apt-get update \  
&& apt-get install -y curl unzip \  
python3 python3-setuptools \  
&& easy_install3 pip py4j \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# http://blog.stuart.axelbrooke.com/python-3-on-spark-return-of-the-
pythonhashseed  
ENV PYTHONHASHSEED=0 \  
PYTHONIOENCODING=UTF-8  
# JAVA  
ENV JAVA_HOME=/usr/jdk1.8.0_31 \  
PATH=$PATH:$JAVA_HOME/bin  
RUN curl -L --retry 3 --insecure \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie;" \  
"http://download.oracle.com/otn-pub/java/jdk/8u31-b13/server-
jre-8u31-linux-x64.tar.gz" \  
| gunzip \  
| tar x -C /usr/ \  
&& ln -s $JAVA_HOME /usr/java \  
&& rm -rf $JAVA_HOME/man  
  
# HADOOP  
ENV HADOOP_HOME=/usr/hadoop-$HADOOP_VERSION \  
HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop \  
PATH=$PATH:$HADOOP_HOME/bin  
RUN curl -L --retry 3 \  
"http://archive.apache.org/dist/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz"
\  
| gunzip \  
| tar -x -C /usr/ \  
&& rm -rf $HADOOP_HOME/share/doc  
  
# SPARK  
ENV SPARK_DIST=spark-$SPARK_VERSION-bin-hadoop$HADOOP_PROFILE \  
SPARK_HOME=/usr/spark-$SPARK_VERSION \  
PYSPARK_PYTHON=python3 \  
SPARK_DIST_CLASSPATH="$HADOOP_HOME/etc/hadoop/*:$HADOOP_HOME/share/hadoop/common/lib/*:$HADOOP_HOME/share/hadoop/common/*:$HADOOP_HOME/share/hadoop/hdfs/*:$HADOOP_HOME/share/hadoop/hdfs/lib/*:$HADOOP_HOME/share/hadoop/hdfs/*:$HADOOP_HOME/share/hadoop/yarn/lib/*:$HADOOP_HOME/share/hadoop/yarn/*:$HADOOP_HOME/share/hadoop/mapreduce/lib/*:$HADOOP_HOME/share/hadoop/mapreduce/*:$HADOOP_HOME/share/hadoop/tools/lib/*"
\  
PATH=$PATH:$SPARK_HOME/bin  
RUN curl -L --retry 3 \  
"http://apache.mirror.rafal.ca/spark/spark-$SPARK_VERSION/$SPARK_DIST.tgz" \  
| gunzip \  
| tar x -C /usr/ \  
&& mv /usr/$SPARK_DIST $SPARK_HOME  
  
EXPOSE 8080 4040 8081  
WORKDIR $SPARK_HOME  
CMD ["bin/spark-class", "org.apache.spark.deploy.master.Master"]

