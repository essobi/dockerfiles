FROM openjdk:8-jre-slim  
  
ARG BUILD_DATE  
ARG SPARK_VERSION=2.3.0  
  
LABEL org.label-schema.name="Apache Spark ${SPARK_VERSION}" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.version=$SPARK_VERSION  
  
ENV SPARK_HOME /usr/spark  
ENV PATH="/usr/spark/bin:${PATH}"  
RUN apt-get update && \  
apt-get install -y wget && \  
wget -q
"http://apache.cs.uu.nl/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-
hadoop2.7.tgz" && \  
tar xzf "spark-${SPARK_VERSION}-bin-hadoop2.7.tgz" && \  
rm "spark-${SPARK_VERSION}-bin-hadoop2.7.tgz" && \  
mv "spark-${SPARK_VERSION}-bin-hadoop2.7" /usr/spark && \  
apt-get remove -y wget && \  
apt-get autoremove -y && \  
apt-get clean  
  
ENTRYPOINT ["spark-submit"]  
CMD ["--help"]

