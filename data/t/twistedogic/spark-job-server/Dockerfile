FROM twistedogic/spark-mesos:latest  
MAINTAINER Jordan Li  
ENV SPARK_HOME /opt/spark  
ENV SPARK_SERVER_HOME /opt/job-server  
ENV SBT_VERSION 0.13.8  
ENV SPARK_VERSION 1.4.1  
RUN curl -L -o sbt-$SBT_VERSION.deb
https://dl.bintray.com/sbt/debian/sbt-$SBT_VERSION.deb && \  
dpkg -i sbt-$SBT_VERSION.deb && \  
rm sbt-$SBT_VERSION.deb && \  
apt-get update && \  
apt-get install sbt git -y && \  
apt-get clean autoclean && \  
apt-get autoremove --yes && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  
RUN git clone https://github.com/spark-jobserver/spark-jobserver.git
/tmp/spark-jobserver && \  
cd /tmp/spark-jobserver && \  
sbt job-server/assembly  
RUN mkdir -p $SPARK_SERVER_HOME && \  
cp /tmp/spark-jobserver/job-server/target/scala-2.10/spark-job-server.jar
$SPARK_SERVER_HOME && \  
rm -rf /tmp/spark-jobserver  
ADD ./conf $SPARK_SERVER_HOME  
ADD supervisord.conf /etc/supervisord.conf  
ADD init.sh /init.sh  
CMD /init.sh  

