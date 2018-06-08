FROM mineset/spark:1.6.1-hadoop-2.6_scala-2.11  
# Overall ENV vars  
ENV SBT_VERSION 0.13.11  
ENV SCALA_VERSION 2.11.6  
ENV SPARK_VERSION 1.6.1  
ENV MESOS_BUILD_VERSION 0.28.0-2.0.16  
ENV SPARK_JOBSERVER_BRANCH v0.6.2  
RUN apt-get clean && \  
mv /var/lib/apt/lists /tmp && \  
mkdir -p /var/lib/apt/lists/partial && \  
apt-get clean && \  
apt-get update && \  
apt-get install -y curl  
  
# SBT install  
RUN wget --no-check-certificate
https://bintray.com/artifact/download/sbt/debian/sbt-$SBT_VERSION.deb && \  
dpkg -i sbt-$SBT_VERSION.deb && \  
rm sbt-$SBT_VERSION.deb && \  
sbt sbtVersion  
  
# Mesos install  
RUN wget
http://repos.mesosphere.com/ubuntu/pool/main/m/mesos/mesos_$MESOS_BUILD_VERSION.ubuntu1404_amd64.deb
&& \  
dpkg -i mesos_$MESOS_BUILD_VERSION.ubuntu1404_amd64.deb && \  
rm mesos_$MESOS_BUILD_VERSION.ubuntu1404_amd64.deb  
  
# Set native Mesos library path  
ENV MESOS_NATIVE_JAVA_LIBRARY /usr/local/lib/libmesos.so  
  
# H2 Database folder for Spark JobServer  
RUN mkdir -p /database  
  
# Clone Spark-Jobserver repository  
ENV SPARK_JOBSERVER_BUILD_HOME /spark-jobserver  
ENV SPARK_JOBSERVER_APP_HOME /app  
RUN git clone \--branch $SPARK_JOBSERVER_BRANCH https://github.com/spark-
jobserver/spark-jobserver.git  
RUN mkdir -p $SPARK_JOBSERVER_APP_HOME  
RUN mkdir -p /tmp/spark-jobserver  
  
# Add custom files, set permissions  
Add docker.conf $SPARK_JOBSERVER_BUILD_HOME/config/docker.conf  
Add setenv.sh $SPARK_JOBSERVER_BUILD_HOME/bin/setenv.sh  
ADD docker.sh $SPARK_JOBSERVER_BUILD_HOME/config/docker.sh  
#ADD log4j-docker.properties
$SPARK_JOBSERVER_BUILD_HOME/config/log4j-server.properties  
ADD server_deploy.sh $SPARK_JOBSERVER_BUILD_HOME/bin/server_deploy.sh  
ADD server_start.sh $SPARK_JOBSERVER_BUILD_HOME/bin/server_start.sh  
RUN chmod +x $SPARK_JOBSERVER_BUILD_HOME/bin/server_deploy.sh  
RUN chmod +x $SPARK_JOBSERVER_BUILD_HOME/bin/server_start.sh  
RUN chmod +x $SPARK_JOBSERVER_BUILD_HOME/bin/server_stop.sh  
RUN chmod +x $SPARK_JOBSERVER_BUILD_HOME/bin/setenv.sh  
  
# Build Spark-Jobserver  
WORKDIR $SPARK_JOBSERVER_BUILD_HOME  
RUN bin/server_deploy.sh docker && \  
cd / && \  
rm -rf -- $SPARK_JOBSERVER_BUILD_HOME && \  
rm -rf /root/.ivy2  
ADD user_server_start.sh $SPARK_JOBSERVER_APP_HOME/user_server_start.sh  
RUN chmod +x $SPARK_JOBSERVER_APP_HOME/user_server_start.sh  
# Cleanup files, folders and variables  
RUN unset SPARK_VERSION_STRING && \  
unset SPARK_DOWNLOAD_URL && \  
unset SPARK_JOBSERVER_BRANCH && \  
unset SPARK_JOBSERVER_BUILD_HOME && \  
unset MESOS_BUILD_VERSION  
  
EXPOSE 8090 9999  
#ENTRYPOINT ["/app/server_start.sh"]  

