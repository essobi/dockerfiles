FROM gettyimages/spark  
MAINTAINER Paul Beswick  
  
# Add necessary libraries for ipython and git  
RUN apt-get update  
RUN apt-get install -y python-dev python-pip python-numpy python-scipy python-
pandas gfortran  
RUN apt-get install -y git-all  
  
# Download the mongo-hadoop connector library and build it  
RUN git clone https://github.com/mongodb/mongo-hadoop.git  
RUN cd mongo-hadoop && ./gradlew jar  
  
# Create a file to run as the entrypoint which passes a spark master argument
to docker run through  
# This line writes the SPARK environment variables into a spark configuration
file  
RUN echo 'env | grep SPARK | awk '\''{print "export \"" $0 "\""}'\'' >
/usr/spark/conf/spark-env.sh' > /run.sh  
# This line edits the dns resolvers file to point to the docker bridge and
consul dns server  
RUN echo 'echo nameserver 172.17.42.1 > /etc/resolv.conf && echo search
service.consul node.consul >> /etc/resolv.conf' >> /run.sh  
# This line removes anything registered in /etc/hosts on the docker network -
not needed when we run with --net=host  
#RUN echo 'cat /etc/hosts | grep -v 172.17 > tmphosts && cat tmphosts >
/etc/hosts && rm tmphosts' >> run.sh  
# This line starts the master passing in the options we sent with docker run  
RUN echo /usr/spark/bin/spark-class org.apache.spark.deploy.master.Master
\"\$\@\" >> /run.sh  
  
RUN chmod +x /run.sh  
  
ENV SPARK_MASTER_OPTS="-Dspark.driver.port=7001 -Dspark.fileserver.port=7002 \  
-Dspark.broadcast.port=7003 -Dspark.replClassServer.port=7004 \  
-Dspark.blockManager.port=7005 -Dspark.executor.port=7006 \  
-Dspark.ui.port=4040 -Dspark.broadcast.factory=org.apache.spark.broadcast.HttpBroadcastFactory"  
ENV SPARK_WORKER_OPTS="-Dspark.driver.port=7001 -Dspark.fileserver.port=7002 \  
-Dspark.broadcast.port=7003 -Dspark.replClassServer.port=7004 \  
-Dspark.blockManager.port=7005 -Dspark.executor.port=7006 \  
-Dspark.ui.port=4040 -Dspark.broadcast.factory=org.apache.spark.broadcast.HttpBroadcastFactory"  
ENV SPARK_EXECUTOR_OPTS="-Dspark.driver.port=7001 -Dspark.fileserver.port=7002
\  
-Dspark.broadcast.port=7003 -Dspark.replClassServer.port=7004 \  
-Dspark.blockManager.port=7005 -Dspark.executor.port=7006 \  
-Dspark.ui.port=4040 -Dspark.broadcast.factory=org.apache.spark.broadcast.HttpBroadcastFactory"  
ENV SPARK_JAVA_OPTS="-Dspark.driver.port=7001 -Dspark.fileserver.port=7002 \  
-Dspark.broadcast.port=7003 -Dspark.replClassServer.port=7004 \  
-Dspark.blockManager.port=7005 -Dspark.executor.port=7006 \  
-Dspark.ui.port=4040 -Dspark.broadcast.factory=org.apache.spark.broadcast.HttpBroadcastFactory"  
ENV SPARK_MASTER_PORT 7077  
ENV SPARK_MASTER_WEBUI_PORT 8080  
ENV SPARK_WORKER_PORT 8088  
ENV SPARK_WORKER_WEBUI_PORT 8081  
EXPOSE 8080 7077 8088 8081 4040 7001 7002 7003 7004 7005 7006  
ENTRYPOINT ["/bin/bash","/run.sh"]  

