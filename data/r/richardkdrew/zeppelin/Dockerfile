# DOCKER-VERSION 1.6.2  
#  
# Zeppelin Notebook Dockerfile  
#  
# https://github.com/richardkdrew/docker-zeppelin  
#  
FROM richardkdrew/maven  
  
MAINTAINER Richard Drew <richardkdrew@gmail.com>  
  
# install dependencies  
RUN buildDeps='curl build-essential git python python-setuptools python-dev
python-numpy' \  
&& apt-get update \  
&& apt-get install -y $buildDeps \--no-install-recommends \  
&& apt-get clean  
  
RUN easy_install py4j  
  
# SPARK  
ENV APACHE_SPARK_VERSION=1.5.0 \  
SPARK_HOME=/usr/local/spark  
ENV PATH $PATH:$SPARK_HOME/bin  
  
# install Spark/Hadoop Client support  
RUN mkdir -p ${SPARK_HOME} \  
&& curl -sSL -o /Spark-${APACHE_SPARK_VERSION}.tar.gz
http://d3kbcqa49mib13.cloudfront.net/spark-${APACHE_SPARK_VERSION}-bin-
hadoop2.6.tgz \  
&& tar zxf /Spark-${APACHE_SPARK_VERSION}.tar.gz -C /usr/local \  
&& mv /usr/local/spark-${APACHE_SPARK_VERSION}-bin-hadoop2.6/* ${SPARK_HOME} \  
# do some clean-up  
&& rm -f /Spark-${APACHE_SPARK_VERSION}.tar.gz \  
&& rm -fr /usr/local/spark-${APACHE_SPARK_VERSION}-bin-hadoop2.6  
# ZEPPELIN  
ENV ZEPPELIN_HOME /usr/local/zeppelin  
  
# get Zeppelin  
RUN mkdir -p ${ZEPPELIN_HOME} \  
&& mkdir -p ${ZEPPELIN_HOME}/logs \  
&& mkdir -p ${ZEPPELIN_HOME}/run \  
&& mkdir -p ${ZEPPELIN_HOME}/data \  
&& cd /usr/local \  
&& git clone https://github.com/apache/incubator-zeppelin.git \  
&& mv /usr/local/incubator-zeppelin/* ${ZEPPELIN_HOME} \  
# do some clean-up  
&& rm -fr /usr/local/incubator-zeppelin  
  
# install and configure Zeppelin  
RUN git config --global url.https://github.com/.insteadOf git://github.com/ \  
&& cd ${ZEPPELIN_HOME} \  
&& mvn package -Dspark.version=${APACHE_SPARK_VERSION} -Pspark-1.5
-Dhadoop.version=2.6.0 -Phadoop-2.6 -Pyarn -DskipTests \  
#&& mvn clean package -DskipTests \  
# do some clean-up  
&& apt-get purge -y --auto-remove $buildDeps \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR ${ZEPPELIN_HOME}  
  
VOLUME [${ZEPPELIN_HOME}/notebook, ${ZEPPELIN_HOME}/logs]  
  
EXPOSE 8080 8081 4040  
CMD ["/usr/local/zeppelin/bin/zeppelin.sh"]

