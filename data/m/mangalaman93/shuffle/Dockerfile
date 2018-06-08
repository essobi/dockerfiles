FROM mangalaman93/spark:2.1.0  
MAINTAINER Aman Mangal <mangalaman93@gmail.com>  
  
# explicitly set user/group IDs  
RUN groupadd -r hadoop --gid=1000 && useradd -r -g hadoop -d /home/hadoop
--uid=1000 hadoop  
  
# grab gosu for easy step-down from root  
ENV GOSU_VERSION=1.9  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 && \  
curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-amd64" && \  
curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-amd64.asc" && \  
gpg --verify /usr/local/bin/gosu.asc && \  
rm /usr/local/bin/gosu.asc && \  
rm -r /root/.gnupg/ && \  
chmod +x /usr/local/bin/gosu && \  
gosu nobody true  
  
ADD docker-entrypoint.sh /  
  
VOLUME /opt/spark/tmp  
WORKDIR $SPARK_HOME  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["./bin/spark-class",
"org.apache.spark.deploy.mesos.MesosExternalShuffleService"]  

