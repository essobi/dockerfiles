# Reference URL: https://runnable.com/docker/java/dockerize-your-java-
application  
# Reference URL: https://www.howtoforge.com/tutorial/how-to-create-docker-
images-with-dockerfile/  
# Reference URL:
https://hub.docker.com/r/mcpayment/ubuntu1404-java8/~/dockerfile/  
# Reference URL: https://github.com/TexaiCognitiveArchitecture/docker-
java8-jenkins-maven-git-nano  
# Reference Command: docker search ubuntu/java  
# Download base image ubuntu 16.04  
FROM ubuntu  
  
MAINTAINER Ankush Goyal <ankush.goyal@prontoitlabs.com>  
  
# Update Software repository  
RUN apt-get update  
  
# Install Git  
RUN apt-get install -y git  
  
# Update the package repository  
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" >
/etc/apt/sources.list  
RUN apt-get -y update  
  
# Install Oracle Java 8  
ENV JAVA_VER 8  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
RUN echo 'deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main' >>
/etc/apt/sources.list && \  
echo 'deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main' >>
/etc/apt/sources.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C2518248EEA14886 && \  
apt-get update && \  
echo oracle-java${JAVA_VER}-installer shared/accepted-oracle-license-v1-1
select true | /usr/bin/debconf-set-selections && \  
apt-get install -y --force-yes --no-install-recommends oracle-
java${JAVA_VER}-installer oracle-java${JAVA_VER}-set-default && \  
apt-get clean && \  
rm -rf /var/cache/oracle-jdk${JAVA_VER}-installer  
  
# Set Oracle Java as the default Java  
RUN update-java-alternatives -s java-8-oracle  
  
RUN echo "export JAVA_HOME=/usr/lib/jvm/java-8-oracle" >> ~/.bashrc  
  
# Clean Up APT when finished  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Update dpkg repositories  
RUN apt-get update  
  
# Install wget  
RUN apt-get install -y wget  
  
# Get maven 3.3.9  
RUN wget --no-verbose -O /tmp/apache-maven-3.3.9-bin.tar.gz http://www-
eu.apache.org/dist/maven/maven-3/3.3.9/binaries/apache-maven-3.3.9-bin.tar.gz  
  
# Install maven  
RUN tar xzf /tmp/apache-maven-3.3.9-bin.tar.gz -C /opt/  
RUN ln -s /opt/apache-maven-3.3.9 /opt/maven  
RUN ln -s /opt/maven/bin/mvn /usr/local/bin  
RUN rm -f /tmp/apache-maven-3.3.9-bin.tar.gz  
ENV MAVEN_HOME /opt/maven  
  
# Update Software repository  
RUN apt-get update  
  
# Install Hadoop  
RUN mkdir /usr/local/hadoop  
RUN wget --no-verbose -O /usr/local/hadoop/hadoop-2.7.2.tar.gz
http://apache.claz.org/hadoop/common/hadoop-2.7.2/hadoop-2.7.2.tar.gz | tar
-xz -C /usr/local/hadoop --strip-components 1  
ENV HADOOP_HOME /usr/local/hadoop  
ENV HADOOP_INSTALL $HADOOP_HOME  
ENV PATH $PATH:$HADOOP_INSTALL/sbin  
ENV HADOOP_MAPRED_HOME $HADOOP_INSTALL  
ENV HADOOP_COMMON_HOME $HADOOP_INSTALL  
ENV HADOOP_HDFS_HOME $HADOOP_INSTALL  
ENV YARN_HOME $HADOOP_INSTALL  
ENV PATH $HADOOP_HOME/bin:$PATH  
  
# Update Software repository  
RUN apt-get update  
  
# Install Hive  
RUN mkdir /usr/local/hive  
RUN wget --no-verbose -O /usr/local/hive/apache-hive-2.1.0-bin.tar.gz
http://apache.mesi.com.ar/hive/hive-2.1.0/apache-hive-2.1.0-bin.tar.gz | tar
-xz -C /usr/local/hive --strip-components 1  
ENV HIVE_HOME /usr/local/hive  
ENV PATH $HIVE_HOME/bin:$PATH  
  
  
# Derby for Hive metastore backend  
RUN cd $HIVE_HOME && $HIVE_HOME/bin/schematool -initSchema -dbType derby  

