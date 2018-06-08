FROM twistedogic/spark-mesos  
MAINTAINER Jordan Li  
ENV SPARKLING_URL http://h2o-release.s3.amazonaws.com/sparkling-
water/rel-1.4/3/sparkling-water-1.4.3.zip  
ENV SPARK_HOME /opt/spark/  
RUN apt-get update && \  
apt-get install -y --no-install-recommends curl tar wget unzip ca-certificates
openjdk-7-jre python2.7 && \  
apt-get clean autoclean && \  
apt-get autoremove --yes && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  
ENV SPARKLING_VERSION 1.4.3  
RUN wget "${SPARKLING_URL}" -O /opt/sparkling-water-${SPARKLING_VERSION}.zip
--no-check-certificate  
RUN cd /opt && unzip sparkling-water-${SPARKLING_VERSION}.zip && rm -rf
sparkling-water-${SPARKLING_VERSION}.zip  

