FROM openjdk:8-alpine  
  
ENV HADOOP_VERSION 2.8.0  
ENV HADOOP_HOME /opt/hadoop  
ENV SPARK_VERSION 2.1.0  
#ENV HADOOP_URL
http://www.us.apache.org/dist/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz  
ENV SPARK_URL
http://www.us.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-
hadoop2.7.tgz  
  
# install hadoop  
ADD hadoop-${HADOOP_VERSION}-alpine-native.tar ${HADOOP_HOME}/  
ADD *.sh /bin/  
  
RUN apk add --update curl py-numpy tar bash \  
# install spark  
&& mkdir -p /opt/spark \  
&& curl ${SPARK_URL} | tar --strip=1 -zx -C /opt/spark \  
&& rm -fr /var/cache/apk/*  
  
ENV LD_LIBRARY_PATH
${LD_LIBRARY_PATH}:${JAVA_HOME}/jre/lib/amd64/server:${HADOOP_HOME}/lib/native  
  
ENTRYPOINT ["sh", "-c", "/bin/start-master.sh"]  

