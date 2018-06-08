FROM ubuntu:14.04.3  
# packages  
RUN apt-get update && apt-get install -yq \--no-install-recommends \--force-
yes \  
wget \  
git \  
openjdk-7-jre \  
libjansi-java \  
libsvn1 \  
libcurl3 \  
libsasl2-modules && \  
rm -rf /var/lib/apt/lists/*  
  
  
# Overall ENV vars  
ENV SCALA_VERSION 2.11.6  
ENV SPARK_VERSION 1.6.1  
  
# Maven  
RUN cd /opt/ \  
&& wget http://apache.cs.uu.nl/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz \  
&& tar xzf apache-maven-3.3.9-bin.tar.gz \  
&& rm apache-maven-3.3.9-bin.tar.gz  
  
ENV PATH /opt/apache-maven-3.3.9/bin:$PATH  
  
ENV MAVEN_OPTS -Xmx2048m  
  
# Scala install  
# remove the documentation  
RUN wget
http://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.deb \  
&& dpkg -i scala-$SCALA_VERSION.deb \  
&& rm scala-$SCALA_VERSION.deb \  
&& rm -rf /usr/share/doc/scala  
# Java  
RUN cd /opt/ \  
&& wget \--no-cookies \--no-check-certificate \--header "Cookie:
gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-
cookie" "http://download.oracle.com/otn-
pub/java/jdk/8u66-b17/jdk-8u66-linux-x64.tar.gz" \  
&& tar xzf jdk-8u66-linux-x64.tar.gz \  
&& rm jdk-8u66-linux-x64.tar.gz \  
&& update-alternatives \--install /usr/bin/java java /opt/jdk1.8.0_66/bin/java
100 \  
&& update-alternatives \--install /usr/bin/jar jar /opt/jdk1.8.0_66/bin/jar
100 \  
&& update-alternatives \--install /usr/bin/javac javac
/opt/jdk1.8.0_66/bin/javac 100  
  
ENV JAVA_HOME /opt/jdk1.8.0_66  
# SPARK  
  
RUN mkdir /opt/spark  
# Spark ENV vars  
ENV SPARK_VERSION_STRING spark-$SPARK_VERSION-bin-hadoop2.6  
ENV SPARK_HOME /opt/spark  
ENV PATH $PATH:/opt/spark/bin  
#remove all cache and tmp files  
RUN git clone https://github.com/apache/spark.git /tmp/spark \  
&& cd /tmp/spark \  
&& git checkout tags/v$SPARK_VERSION \  
&& ./dev/change-scala-version.sh 2.11 \  
&& ./make-distribution.sh \--name hadoop-2.6_scala-2.11 \--tgz -Pyarn
-Phadoop-2.6 -Dscala-2.11 -DskipTests \  
&& rm -rf /root/.m2 \  
&& tar \--strip-components=1 -xzvf /tmp/spark/spark-$SPARK_VERSION-bin-
hadoop-2.6_scala-2.11.tgz -C /opt/spark \  
&& rm /opt/spark/lib/spark-examples-*.jar \  
&& rm -rf /tmp/spark  

