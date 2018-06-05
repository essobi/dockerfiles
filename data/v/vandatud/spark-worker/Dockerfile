FROM phusion/baseimage:latest  
  
MAINTAINER Thomas Gruender <thomas.gruender@tu-dresden.de>, Brian Rimek
<brian.rimek@tu-dresden.de>  
LABEL version="spark-worker-2.1"  
LABEL release="0.1.4"  
  
ARG JAVA_MAJOR_VERSION=7  
ARG SPARK_VERSION=2.1.0  
ARG HADOOP_MAJOR_VERSION=2.7  
ARG SPARK_WORKDIR=/opt/spark  
ARG SPARK_ARCHIVE=http://www-
eu.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-
hadoop${HADOOP_MAJOR_VERSION}.tgz  
  
# Install Python.  
RUN \  
apt-get update && \  
apt-get install -y python3 python3-dev python3-pip python3-virtualenv && \  
apt-get install -y python3-numpy python3-wheel && \  
rm -rf /var/lib/apt/lists/*  
  
# Install system tools  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
apt-get install -y byobu curl git htop man unzip nano vim wget && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Java  
RUN \  
echo oracle-java${JAVA_MAJOR_VERSION}-installer shared/accepted-oracle-
license-v1-1 select true | debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java${JAVA_MAJOR_VERSION}-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk${JAVA_MAJOR_VERSION}-installer  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-${JAVA_MAJOR_VERSION}-oracle  
  
# Install R  
RUN echo "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/" | tee -a
/etc/apt/sources.list && \  
gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9 && \  
gpg -a --export E084DAB9 | apt-key add - && \  
apt-get update && \  
apt-get install -y r-base r-base-dev  
  
# Update pip and install Tensorflow  
RUN pip3 install --upgrade pip  
RUN pip3 install tensorflow  
  
# Download/Install Spark  
RUN mkdir ${SPARK_WORKDIR}  
WORKDIR ${SPARK_WORKDIR}  
RUN \  
wget ${SPARK_ARCHIVE} && \  
tar -xvzf spark-${SPARK_VERSION}-bin-hadoop${HADOOP_MAJOR_VERSION}.tgz && \  
rm spark-${SPARK_VERSION}-bin-hadoop${HADOOP_MAJOR_VERSION}.tgz && \  
chown -R root:root spark-${SPARK_VERSION}-bin-hadoop${HADOOP_MAJOR_VERSION} &&
\  
ln -s spark-${SPARK_VERSION}-bin-hadoop${HADOOP_MAJOR_VERSION}
${SPARK_WORKDIR}/current && \  
mkdir current/logs && \  
touch current/logs/spark-service.log  
  
# Define SPARK_HOME variable  
ENV SPARK_HOME ${SPARK_WORKDIR}/current  
  
# Set SPARK_HOME to PATH  
ENV PATH $PATH:$SPARK_HOME/bin  
  
# Config Spark-worker as a Service  
RUN mkdir /etc/service/spark-worker  
ADD files/run.spark-worker /tmp/run.spark-worker  
# DOS-fix: Make sure files have unix line endings and execute permission  
RUN \  
tr -d '\015' < /tmp/run.spark-worker > /tmp/run.spark-worker-unix && \  
mv /tmp/run.spark-worker-unix /etc/service/spark-worker/run && \  
chmod +x /etc/service/spark-worker/run  
  
# Config Spark-worker tu run as script during container startup  
#RUN mkdir -p /etc/my_init.d  
#ADD files/spark-worker.sh /tmp/spark-worker.sh  
# DOS-fix: Make sure files have unix line endings and execute permission  
#RUN \  
# tr -d '\015' < /tmp/spark-worker.sh > /tmp/spark-worker-unix.sh && \  
# mv /tmp/spark-worker-unix.sh /etc/my_init.d/spark-worker.sh && \  
# chmod +x /etc/my_init.d/spark-worker.sh  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 8081

