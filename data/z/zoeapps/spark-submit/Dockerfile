FROM ubuntu:14.04  
MAINTAINER Daniele Venzano <venza@brownhat.org>  
  
RUN apt-get update && apt-get install -y --force-yes software-properties-
common python-software-properties  
RUN apt-add-repository -y ppa:webupd8team/java  
RUN /bin/echo debconf shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections  
  
RUN apt-get update && apt-get -y install oracle-java7-installer oracle-
java7-set-default curl  
  
ARG SPARK_VERSION  
ENV SPARK_VERSION ${SPARK_VERSION:-1.6.2}  
  
ARG HADOOP_VERSION  
ENV HADOOP_VERSION ${HADOOP_VERSION:-hadoop2.6}  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle/  
  
RUN curl -s
http://mirrors.ircam.fr/pub/apache/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-${HADOOP_VERSION}.tgz
| tar -xz -C /opt/  
  
WORKDIR /opt  
  
RUN ln -s spark-${SPARK_VERSION}-bin-${HADOOP_VERSION} spark  
ENV SPARK_HOME /opt/spark  
ENV PATH /opt/spark/bin:/opt/spark/sbin:${PATH}  
  
RUN apt-get update && apt-get install -y --force-yes --no-install-recommends \  
wget \  
build-essential \  
python-dev \  
ca-certificates \  
bzip2 \  
pandoc \  
libopenblas-dev \  
libjpeg-dev \  
&& apt-get clean  
  
# Configure environment  
ENV CONDA_DIR /opt/conda  
ENV HADOOP_HOME /opt/hadoop  
ENV HADOOP_CONF_DIR $HADOOP_HOME/etc/hadoop  
ENV PATH $HADOOP_HOME/bin:$CONDA_DIR/bin:$PATH  
ENV SHELL /bin/bash  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV PYTHONPATH $SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.9-src.zip  
  
RUN cd /tmp && \  
mkdir -p $CONDA_DIR && \  
wget http://repo.continuum.io/miniconda/Miniconda3-3.9.1-Linux-x86_64.sh && \  
echo "6c6b44acdd0bc4229377ee10d52c8ac6160c336d9cdd669db7371aa9344e1ac3
*Miniconda3-3.9.1-Linux-x86_64.sh" | sha256sum -c - && \  
/bin/bash Miniconda3-3.9.1-Linux-x86_64.sh -f -b -p $CONDA_DIR && \  
rm Miniconda3-3.9.1-Linux-x86_64.sh && \  
$CONDA_DIR/bin/conda install --yes conda==3.14.1  
  
# Install Python 3 packages  
RUN conda install --yes \  
'pandas=0.17*' \  
'matplotlib=1.4*' \  
'scipy=0.16*' \  
'seaborn=0.6*' \  
'scikit-learn=0.16*' \  
'statsmodels=0.6.1' \  
'pillow' \  
'basemap' \  
&& conda clean -yt  
  
# Add Spark JARs  
RUN curl http://central.maven.org/maven2/com/databricks/spark-
csv_2.10/1.3.0/spark-csv_2.10-1.3.0.jar -o /opt/spark/com.databricks_spark-
csv_2.10-1.3.0.jar  
RUN curl http://central.maven.org/maven2/org/apache/commons/commons-
csv/1.2/commons-csv-1.2.jar -o /opt/spark/org.apache.commons_commons-
csv-1.2.jar  
RUN curl http://central.maven.org/maven2/com/univocity/univocity-
parsers/1.5.6/univocity-parsers-1.5.6.jar -o
/opt/spark/com.univocity_univocity-parsers-1.5.6.jar  
  
ENV HADOOP_VERSION_DL 2.6.1  
RUN curl
http://apache.mirrors.ovh.net/ftp.apache.org/dist/hadoop/common/hadoop-${HADOOP_VERSION_DL}/hadoop-${HADOOP_VERSION_DL}.tar.gz
| tar -xz -C /opt/  
  
RUN ln -s /opt/hadoop-${HADOOP_VERSION_DL} /opt/hadoop  
  
COPY files/* /opt/  
RUN chmod +x /opt/*.sh  
EXPOSE 4040  
ENV ZOE_WORKSPACE /mnt/workspace  
ENV HADOOP_HOME /opt/hadoop  
  
VOLUME /mnt/workspace  
WORKDIR /mnt/workspace  
  
ENTRYPOINT ["/opt/submit.sh"]  

