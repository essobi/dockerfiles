FROM ubuntu:15.10  
# Repo  
#RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
# Java 7 installation from Oracle  
RUN apt install --no-install-recommends software-properties-common -y && apt-
add-repository ppa:webupd8team/java  
  
# Upgrade package index  
RUN apt-get update  
# RUN apt-get -y upgrade  
# automatically accept oracle license  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
  
# and install java 7 oracle jdk  
RUN apt-get -y install oracle-java7-installer --no-install-recommends && apt-
get clean  
RUN apt-get -y install oracle-java7-set-default --no-install-recommends  
  
# Install additional tools  
RUN apt-get -y install --no-install-recommends \  
less \  
curl \  
vim-tiny \  
sudo \  
openssh-server \  
unzip  
  
# Install Spark 1.5.2  
RUN curl -s https://archive.apache.org/dist/spark/spark-1.6.1/spark-1.6.1-bin-
cdh4.tgz | tar -xz -C /opt && \  
ln -s /opt/spark-1.6.1-bin-cdh4 /opt/spark && \  
mkdir /opt/spark/work && \  
chmod 0777 /opt/spark/work  
  
# Install Sparkling water latest version  
RUN curl -s http://h2o-release.s3.amazonaws.com/sparkling-
water/rel-1.6/1/sparkling-water-1.6.1.zip --output sw.zip && \  
unzip sw.zip -d /opt/ && \  
ln -s /opt/sparkling-water-1.5.6 /opt/sparkling-water && \  
rm -f sw.zip  
  
# Setup environment  
ENV SPARK_HOME /opt/spark  
ENV SPARKLING_WATER_HOME /opt/sparkling-water  
#ENV MASTER spark://spark-master:7077  
RUN echo "import org.apache.spark.h2o._" > ${SPARK_HOME}/flow.scala  
RUN echo "val hc = new H2OContext(sc).start()" >> ${SPARK_HOME}/flow.scala  
  
#CMD ${SPARKLING_WATER_HOME}/bin/sparkling-shell -i ${SPARK_HOME}/flow.scala  
CMD tree {$SPARKLING_WATER_HOME}  
  
WORKDIR ${SPARKLING_WATER_HOME}  
  

