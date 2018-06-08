FROM centos:7  
MAINTAINER Aman Mangal <mangalaman93@gmail.com>  
  
RUN yum -y --setopt=tsflags=nodocs install git java-1.8.0-openjdk && \  
yum clean all  
ENV JAVA_HOME=/usr/lib/jvm/jre  
  
# explicitly set user/group IDs  
RUN groupadd -r hadoop --gid=1000 && useradd -r -g hadoop -d /opt/dspark
--uid=1000 hadoop  
  
# We need mesosphere libs for running spark with mesos  
RUN rpm -Uvh http://repos.mesosphere.com/el/7/noarch/RPMS/mesosphere-el-
repo-7-1.noarch.rpm && \  
yum -y install mesos && \  
yum clean all  
  
# grab gosu for easy step-down from root  
ENV GOSU_VERSION 1.9  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-amd64" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-amd64.asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& rm -r /root/.gnupg/ \  
&& chmod +x /usr/local/bin/gosu  
  
ENV SBT_VERSION=0.13.13  
RUN mkdir -p /opt/sbt && \  
curl -o /opt/sbt/sbt-launch.jar -SL https://repo.typesafe.com/typesafe/ivy-
releases/org.scala-sbt/sbt-launch/$SBT_VERSION/sbt-
launch.jar?_ga=1.74838295.421857403.1412028471 && \  
echo "java -Xms512M -Xmx1536M -Xss1M -XX:+CMSClassUnloadingEnabled -jar
/opt/sbt/sbt-launch.jar \"\$@\"" > /usr/bin/sbt && \  
chmod +x /usr/bin/sbt  
  
RUN mkdir /opt/dspark && \  
chown -R hadoop:hadoop /opt/dspark  
  
WORKDIR /opt/dspark  
RUN git clone https://github.com/mangalaman93/dspark && \  
cd dspark/images/dspark/app && \  
sbt assembly && \  
cp target/scala-2.11/dspark-assembly-0.1.0.jar ../../../../dspark.jar && \  
cd ../../../../ && \  
rm -rf dspark  
  
ADD docker-entrypoint.sh /  
  
VOLUME /opt/spark/tmp  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  
CMD [ "java", "-jar", "dspark.jar" ]  

