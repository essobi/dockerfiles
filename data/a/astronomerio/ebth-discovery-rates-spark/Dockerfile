FROM java:openjdk-8u66-jdk  
MAINTAINER schnie <greg@astronomer.io>  
  
# packages  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv E56151BF && \  
echo "deb http://repos.mesosphere.io/debian jessie main" | tee
/etc/apt/sources.list.d/mesosphere.list && \  
echo "deb http://dl.bintray.com/sbt/debian /" | tee -a
/etc/apt/sources.list.d/sbt.list && \  
apt-get update && \  
apt-get install --no-install-recommends -y --force-yes
mesos=0.25.0-0.2.70.debian81 \  
wget \  
python \  
make \  
gcc \  
build-essential \  
g++  
  
# Overall ENV vars  
# ENV APP_BASE_PATH /app  
ENV SPARK_VERSION 1.6.3  
ENV MESOS_BUILD_VERSION 0.25.0-0.2.70  
# Install Node.js 5.x  
ENV NODE_VERSION v5.1.0  
RUN wget --no-check-certificate
https://nodejs.org/dist/$NODE_VERSION/node-$NODE_VERSION-linux-x64.tar.gz && \  
tar -C /usr/local \--strip-components 1 -xzf node-$NODE_VERSION-
linux-x64.tar.gz && \  
rm node-$NODE_VERSION-linux-x64.tar.gz  
  
# Spark ENV vars  
ENV SPARK_VERSION_STRING spark-$SPARK_VERSION-bin-hadoop2.6  
ENV SPARK_DOWNLOAD_URL
http://d3kbcqa49mib13.cloudfront.net/$SPARK_VERSION_STRING.tgz  
  
# Download and unzip Spark  
RUN wget $SPARK_DOWNLOAD_URL && \  
mkdir -p /usr/local/spark && \  
tar xvf $SPARK_VERSION_STRING.tgz -C /tmp && \  
cp -rf /tmp/$SPARK_VERSION_STRING/* /usr/local/spark/ && \  
rm -rf -- /tmp/$SPARK_VERSION_STRING && \  
rm spark-$SPARK_VERSION-bin-hadoop2.6.tgz  
  
# Download and unzip Spark  
# ENV SPARK2_VERSION_STRING spark-2.1.0-bin-hadoop2.7  
# ENV SPARK2_DOWNLOAD_URL
http://d3kbcqa49mib13.cloudfront.net/$SPARK2_VERSION_STRING.tgz  
# RUN wget $SPARK2_DOWNLOAD_URL && \  
# mkdir -p /usr/local/spark2 && \  
# tar xvf $SPARK2_VERSION_STRING.tgz -C /tmp && \  
# cp -rf /tmp/$SPARK2_VERSION_STRING/* /usr/local/spark2/ && \  
# rm -rf -- /tmp/$SPARK2_VERSION_STRING && \  
# rm $SPARK2_VERSION_STRING.tgz  
# ENV SPARK_CLASSPATH /usr/local/spark2/jars  
RUN mkdir -p /usr/local/spark-jars  
RUN wget http://central.maven.org/maven2/org/apache/hadoop/hadoop-
aws/2.7.3/hadoop-aws-2.7.3.jar \  
&& mv hadoop-aws-2.7.3.jar /usr/local/spark-jars/  
RUN wget http://central.maven.org/maven2/com/amazonaws/aws-java-sdk/1.7.4/aws-
java-sdk-1.7.4.jar \  
&& mv aws-java-sdk-1.7.4.jar /usr/local/spark-jars/  
  
# Set SPARK_HOME  
ENV SPARK_HOME /usr/local/spark  
  
# Set ASSEMBLY_JAR  
ENV ASSEMBLY_JAR $SPARK_HOME/lib/spark-assembly-$SPARK_VERSION-hadoop2.6.0.jar  
  
# Set native Mesos library path  
ENV MESOS_NATIVE_JAVA_LIBRARY /usr/local/lib/libmesos.so  
  
# TODO: Make these ONBUILD commands when we abstract generic spark container
out.  
ADD lib /usr/local/src/lib  
ADD package.json /usr/local/src/  
ADD .babelrc /usr/local/src/  
  
# Switch to src dir and install node modules.  
WORKDIR /usr/local/src  
RUN ["npm", "install"]  
  
# Execute task-runner installed with the activity with arguments provided from
CMD.  
# We might want to split out the executor and the utils into aries-executor
and aries-utils.  
ENTRYPOINT ["node_modules/.bin/aries-data"]  

