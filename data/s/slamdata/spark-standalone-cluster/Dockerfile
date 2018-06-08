FROM java:8u111-jre  
  
COPY bin/wrapper_script.sh wrapper_script.sh  
  
ARG SPARK_VERSION="2.2.0"  
ARG SCALA_VERSION="2.11.11"  
RUN curl -L http://www-
us.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-
hadoop2.7.tgz | tar -xz -C /opt/  
RUN curl -L
https://downloads.lightbend.com/scala/${SCALA_VERSION}/scala-${SCALA_VERSION}.tgz
| tar -xz -C /opt  
  
# scala setup  
RUN mv /opt/scala-${SCALA_VERSION} /opt/scala  
RUN export SCALA_HOME=/opt/scala  
RUN export PATH=$PATH:$SCALA_HOME/bin  
  
# spark setup  
RUN mv /opt/spark-${SPARK_VERSION}-bin-hadoop2.7 /opt/spark  
RUN export SPARK_HOME=/opt/spark  
RUN export PATH=$PATH:$SPARK_HOME/bin  
RUN export SPARK_NO_DAEMONIZE=true  
  
EXPOSE 7077 8080 6066  
CMD ./wrapper_script.sh  

