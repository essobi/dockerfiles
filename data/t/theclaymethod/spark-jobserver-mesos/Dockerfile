FROM theclaymethod/ansible-base  
MAINTAINER Clay Kim <clayton.kim@gmail.com>  
  
ENV SPARK_HOME /spark  
ENV SPARK_LOCATION hdfs://foundry/tmp/spark.tgz  
ENV MESOS_MASTER zk://mesos-master.foundry.project.com:2181/mesos  
ENV SPARK_SERVER_HOME /spark-jobserver/runner  
ENV ZK_ENDPOINT zk://mesos-master:2181  
ENV SPARK_BUILD spark-1.1.0-bin-cdh4  
ENV MESOS_HOME /usr/local/lib/libmesos.so  
ENV DEB_VERSION_MESOS 0.21.0-1.0.debian77  
ENV PORT 8090  
#Install the repository  
ENV PATH
/tmp/ansible/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:$PATH  
  
RUN echo "deb http://repos.mesosphere.io/debian wheezy main" >
/etc/apt/sources.list.d/mesosphere.list && \  
apt-key adv --keyserver keyserver.ubuntu.com \--recv E56151BF && \  
apt-get install -y curl && \  
curl -O http://apt.typesafe.com/repo-deb-build-0002.deb && \  
dpkg -i repo-deb-build-0002.deb && \  
apt-get update && \  
apt-get install -y --no-install-recommends sbt \  
git-core \  
build-essential \  
apt-utils \  
mesos=$DEB_VERSION_MESOS && \  
rm repo-deb-build-0002.deb  
#Install SBT  
RUN mkdir -p /root/.sbt/.lib/0.13.5  
WORKDIR /root/.sbt/.lib/0.13.5  
RUN curl -O http://typesafe.artifactoryonline.com/typesafe/ivy-
releases/org.scala-sbt/sbt-launch/0.13.5/sbt-launch.jar  
#clone jobserver repo  
RUN git clone https://github.com/spark-jobserver/spark-jobserver.git
/tmp/spark-jobserver && \  
cd /tmp/spark-jobserver && \  
sbt job-server/assembly && \  
mkdir -p $SPARK_SERVER_HOME && \  
cp /tmp/spark-jobserver/bin/server_start.sh $SPARK_SERVER_HOME && \  
cp /tmp/spark-jobserver/bin/server_stop.sh $SPARK_SERVER_HOME && \  
cp /tmp/spark-jobserver/job-server/target/spark-job-server.jar
$SPARK_SERVER_HOME && \  
rm -rf /tmp/spark-jobserver  
  
  
EXPOSE 8090  
  
WORKDIR /tmp  
RUN curl -O http://d3kbcqa49mib13.cloudfront.net/$SPARK_BUILD.tgz && \  
tar -xvf $SPARK_BUILD.tgz && \  
mv $SPARK_BUILD /spark && \  
rm $SPARK_BUILD.tgz  
  
  
WORKDIR /tmp  
#clone ansible playbook  
RUN git clone https://github.com/theclaymethod/docker-containers /tmp/docker-
playbooks  
WORKDIR /tmp/docker-playbooks/spark-jobserver  
CMD ansible-playbook -i inventory playbook.yml  

