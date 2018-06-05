FROM debian:jessie  
# Adapted from https://github.com/gettyimages/docker-spark  
MAINTAINER Dennis Bachmann "https://github.com/dennisbachmann"  
RUN apt-get update \  
&& apt-get install -y locales \  
&& dpkg-reconfigure -f noninteractive locales \  
&& locale-gen C.UTF-8 \  
&& /usr/sbin/update-locale LANG=C.UTF-8 \  
&& echo "en_CA.UTF-8 UTF-8" >> /etc/locale.gen \  
&& locale-gen \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Users with other locales should set this in their derivative image  
ENV LANG en_CA.UTF-8  
ENV LANGUAGE en_CA:en  
ENV LC_ALL en_CA.UTF-8  
RUN apt-get update \  
&& apt-get install -y curl unzip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# JAVA  
ARG JAVA_MAJOR_VERSION=8  
ARG JAVA_UPDATE_VERSION=131  
ARG JAVA_BUILD_NUMBER=11  
ARG JAVA_TARBALL_HASH=d54c1d3a095b4ff2b6607d096fa80163  
ENV JAVA_HOME /usr/jdk1.${JAVA_MAJOR_VERSION}.0_${JAVA_UPDATE_VERSION}  
  
ENV PATH $PATH:$JAVA_HOME/bin  
RUN curl -sL --retry 3 --insecure \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie;" \  
"http://download.oracle.com/otn-
pub/java/jdk/${JAVA_MAJOR_VERSION}u${JAVA_UPDATE_VERSION}-b${JAVA_BUILD_NUMBER}/${JAVA_TARBALL_HASH}/server-
jre-${JAVA_MAJOR_VERSION}u${JAVA_UPDATE_VERSION}-linux-x64.tar.gz" \  
| gunzip \  
| tar x -C /usr/ \  
&& ln -s $JAVA_HOME /usr/java \  
&& rm -rf $JAVA_HOME/man  
  
# HADOOP  
ENV HADOOP_VERSION 2.8.0  
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
RUN sed -i "s%\${JAVA_HOME}%${JAVA_HOME}%g" $HADOOP_CONF_DIR/hadoop-env.sh \  
&& sed -i 's%localhost%%g' $HADOOP_CONF_DIR/slaves \  
&& mkdir -p $HADOOP_HOME/hadoop_data/hdfs/namenode \  
&& echo "master" > $HADOOP_CONF_DIR/masters  
ADD files/hadoop/core-site.xml $HADOOP_CONF_DIR/core-site.xml  
ADD files/hadoop/yarn-site.xml $HADOOP_CONF_DIR/yarn-site.xml  
ADD files/hadoop/mapred-site.xml $HADOOP_CONF_DIR/mapred-site.xml  
ADD files/hadoop/hdfs-site.xml $HADOOP_CONF_DIR/hdfs-site.xml  
RUN $HADOOP_HOME/bin/hdfs namenode -format  
  
# SPARK  
ENV SPARK_VERSION 2.0.0  
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
  
# SSH  
RUN apt-get update \  
&& apt-get install -y ssh openssh-server \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
# GENERATE SSH KEY  
RUN ssh-keygen -f ~/.ssh/id_rsa -t rsa -P "" \  
&& cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys  
# IGNORE HOST CHECKING  
ADD files/ssh_config /root/.ssh/config  
RUN chmod 600 /root/.ssh/config \  
&& chown root:root ~/.ssh/config  
RUN service ssh start  
  
# ADD BOOT FILE  
ADD files/boot /usr/local/bin/boot  
RUN chmod a+x /usr/local/bin/boot  
  
WORKDIR /application  
  
EXPOSE 8080 50070  
CMD ["/usr/local/bin/boot", "standalone"]  

