FROM agileops/centos-javapython:latest  
  
ENV HADOOP_VERSION=2.7.5 \  
HADOOP_HOME=/opt/hadoop \  
SPARK_VERSION=2.3.0 \  
SPARK_HOME=/opt/spark \  
PYTHON_VERSION=36 \  
PYSPARK_PYTHON=python${PYTHON_VERSION} \  
BIND_ADDRESS="127.0.0.1"  
# Download and install hadoop+yarn+hdfs  
RUN yum install -y which && \  
yum clean all && rm -rf /var/cache/yum && \  
curl
http://apache.mirror.iweb.ca/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz
> /opt/hadoop-${HADOOP_VERSION}.tar.gz && \  
mkdir ${HADOOP_HOME} && \  
tar xvfp /opt/hadoop-${HADOOP_VERSION}.tar.gz -C ${HADOOP_HOME} \--strip-
components=1 && \  
rm -fr /opt/hadoop/share/doc/ && \  
rm /opt/hadoop-${HADOOP_VERSION}.tar.gz  
  
# needed to start yarn  
RUN yum install -y rsync openssh-server openssh-clients && \  
yum clean all && rm -rf /var/cache/yum  
  
ADD http://central.maven.org/maven2/org/apache/hadoop/hadoop-
streaming/${HADOOP_VERSION}/hadoop-streaming-${HADOOP_VERSION}.jar
${HADOOP_HOME}/hadoop-streaming.jar  
  
# Download and install spark  
RUN curl
https://archive.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-
bin-without-hadoop.tgz > /opt/spark-$SPARK_VERSION-bin-without-hadoop.tgz && \  
mkdir ${SPARK_HOME} && \  
tar xvfp ${SPARK_HOME}-${SPARK_VERSION}-bin-without-hadoop.tgz -C
${SPARK_HOME} \--strip-components=1 && \  
rm /opt/spark-$SPARK_VERSION-bin-without-hadoop.tgz  
  
# sbins dir of spark and hadoop isn't include in PATH because thereis conflict
on excutables names  
ENV PATH=${SPARK_HOME}/bin:${PATH} \  
PATH=${HADOOP_HOME}/bin:${PATH}  
  
# https://spark.apache.org/docs/latest/hadoop-provided.html  
RUN echo 'export SPARK_DIST_CLASSPATH=$(hadoop classpath)' >>
${SPARK_HOME}/conf/spark-env.sh && chmod +x ${SPARK_HOME}/conf/spark-env.sh  
  
# Configure pyspark  
ENV PYTHONPATH=$SPARK_HOME/python:$PYTHONPATH  
# Set jupyter path  
ENV JUPYTER_DATA_DIR=/usr/local/share/jupyter  
  
# requirements for pytrade and flayers  
RUN yum install -y --setopt=tsflags=nodocs blas atlas gcc-gfortran swig
gcc-c++ mercurial && \  
yum clean all && rm -rf /var/cache/yum  
  
# Install python libraries  
COPY requirements.txt /opt/spark/  
  
# RUN # pip install --no-cache-dir pipenv && \  
RUN pip install --no-cache-dir -r ${SPARK_HOME}/requirements.txt && \  
jupyter toree install --spark_home=${SPARK_HOME}
\--interpreters=Scala,PySpark,SQL  
  
# As suggested for BigDL tutorials  
# https://github.com/intel-analytics/BigDL/blob/master/docker/BigDL/Dockerfile  
RUN python3 -m ipykernel install  
  
# custom dirs :  
# /work-dir - working directory  
# /work-dir/hadoop - hadoop+hdfs datas like configurations, index, storage
blocks  
# /work-dir/sparks - hadoop+hdfs datas  
RUN mkdir /work-dir /work-dir/hadoop /work-dir/spark  
WORKDIR /work-dir  
  
# Volumes are used to persist data  
# Path on the local filesystem where the NameNode stores the namespace and
transactions logs persistently.  
VOLUME /work-dir/hadoop/dfs.name  
# Comma separated list of paths on the local filesystem of a DataNode where it
should store its blocks.  
VOLUME /work-dir/hadoop/dfs.data  
  
# Copy hadoop configs  
COPY ./etc/hadoop/* /opt/hadoop/etc/hadoop/  
  
# HADOOP_OPTS is an env. var. used to configure hadoop's specific java options  
ENV NAMENODE_DATA=/work-dir/hadoop/dfs.name \  
DFS_DATA=/work-dir/hadoop/dfs.data \  
HADOOP_OPTS="-Ddfs.name.dir=${NAMENODE_DATA} -Ddfs.data.dir=${DFS_DATA}"  
COPY ./bin/bootstrap.sh /usr/bin/  
  
# Hdfs ports  
EXPOSE 50010 50020 50070 50075 50090 8020 9000  
# Mapred ports  
EXPOSE 10020 19888  
# Yarn ports  
EXPOSE 8030 8031 8032 8033 8040 8042 8088  
# ^-- taken from https://github.com/sequenceiq/hadoop-
docker/blob/master/Dockerfile  
# Jupyter port  
EXPOSE 8888  
# https://jupyter-notebook.readthedocs.io/en/latest/public_server.html#docker-
cmd  
ENTRYPOINT ["/usr/bin/tini", "--"]  
  
CMD jupyter notebook --port=8888 --no-browser --ip=${BIND_ADDRESS}  

