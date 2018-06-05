## Reference:  
## https://github.com/yahoo/CaffeOnSpark/wiki/GetStarted_local  
## https://github.com/yahoo/CaffeOnSpark/blob/master/caffe-
grid/src/test/python/PythonTest.sh  
FROM ubuntu:14.04  
MAINTAINER Fahmi Akbar Wildana <fahmi.akbar.w@mail.ugm.ac.id>  
  
ENV pwd /root  
  
## Install git, wget, bc and dependencies  
# https://github.com/Kaixhin/dockerfiles/blob/master/caffe/deps/Dockerfile  
RUN apt-get update && apt-get install -y \  
git \  
wget \  
bc \  
cmake \  
libatlas-base-dev \  
libatlas-dev \  
libboost-all-dev \  
libopencv-dev \  
libprotobuf-dev \  
libgoogle-glog-dev \  
libgflags-dev \  
protobuf-compiler \  
libhdf5-dev \  
libleveldb-dev \  
liblmdb-dev \  
libsnappy-dev \  
python-dev \  
python-pip \  
python-numpy \  
maven \  
software-properties-common \  
gfortran > /dev/null && \  
pip install --upgrade pip  
  
## Install Oracle Java 8  
# https://github.com/dockerfile/java/blob/master/oracle-java8/Dockerfile  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
# Get CaffeOnSpark  
RUN cd ${pwd} && git clone https://github.com/cimenx/CaffeOnSpark.git
--recursive  
ENV CAFFE_ON_SPARK ${pwd}/CaffeOnSpark  
  
# Configure CaffeOnSpark  
ADD requirements.txt ${CAFFE_ON_SPARK}/caffe-public/python/  
RUN cd ${CAFFE_ON_SPARK}/caffe-public/ && \  
pip install -U -r python/requirements.txt  
  
# Install Spark and Hadoop  
ADD Makefile.config ${CAFFE_ON_SPARK}/caffe-public/  
RUN cd ${pwd} && bash ${CAFFE_ON_SPARK}/scripts/local-setup-hadoop.sh && \  
bash ${CAFFE_ON_SPARK}/scripts/local-setup-spark.sh \  
  
ENV HADOOP_HOME=${pwd}/hadoop-2.6.4  
ENV SPARK_HOME=${pwd}/spark-1.6.0-bin-hadoop2.6  
## Integrate jupyter notebook  
# https://github.com/jupyter/docker-stacks/blob/master/pyspark-
notebook/Dockerfile  
ENV PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.9-src.zip  
# ENV IPYTHON_ROOT=<your python installation>  
ENV PYSPARK_PYTHON=${IPYTHON_ROOT}/bin/python  
ENV IPYTHON_OPTS="notebook --no-browser --ip=`hostname`"  
ENV
PATH=${IPYTHON_ROOT}/bin:${HADOOP_HOME}/bin:${SPARK_HOME}/bin:${SPARK_HOME}/sbin:${PATH}  
  
# Build CaffeOnSpark  
RUN cd ${CAFFE_ON_SPARK} && \  
make build  
  
ENV LD_LIBRARY_PATH ${CAFFE_ON_SPARK}/caffe-
public/distribute/lib:${CAFFE_ON_SPARK}/caffe-distri/distribute/lib  
# ENV LD_LIBRARY_PATH
${LD_LIBRARY_PATH}:/usr/local/cuda-7.0/lib64:/usr/local/mkl/lib/intel64/  
RUN cd ${CAFFE_ON_SPARK}/data/ && unzip ${CAFFE_ON_SPARK}/caffe-
grid/target/caffeonsparkpythonapi.zip  
  
EXPOSE 8080 7077 8081  
# Set ~/caffe as working directory  
WORKDIR ${CAFFE_ON_SPARK}  
  
ENTRYPOINT ["IPYTHON=1 pyspark", \  
"--driver-library-path", "${CAFFE_ON_SPARK}/caffe-grid/target/caffe-
grid-0.1-SNAPSHOT-jar-with-dependencies.jar", \  
"--driver-class-path", "${CAFFE_ON_SPARK}/caffe-grid/target/caffe-
grid-0.1-SNAPSHOT-jar-with-dependencies.jar", \  
"--jars", "${CAFFE_ON_SPARK}/caffe-grid/target/caffe-grid-0.1-SNAPSHOT-jar-
with-dependencies.jar", \  
"--py-files", "${CAFFE_ON_SPARK}/caffe-grid/target/caffeonsparkpythonapi.zip",
\  
"--files", "${CAFFE_ON_SPARK}/data/caffe/_caffe.so", \  
"--conf", "spark.driver.extraLibraryPath=${LD_LIBRARY_PATH}", \  
"--conf", "spark.executorEnv.LD_LIBRARY_PATH=${LD_LIBRARY_PATH}", \  
"--conf", "spark.executorEnv.DYLD_LIBRARY_PATH=${LD_LIBRARY_PATH}"  
]  

