FROM ubuntu:14.04  
MAINTAINER Peter Bryzgalov  
  
# Install Python  
RUN apt-get update && apt-get install -y --no-install-recommends \  
wget build-essential checkinstall software-properties-common \  
bzip2 \  
ca-certificates \  
sudo \  
locales \  
libreadline-gplv2-dev libncursesw5-dev libssl-dev \  
libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev \  
python-dev python-pip python-numpy python-scipy python-pandas gfortran \  
python-tk \  
python-setuptools && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN /usr/bin/python --version  
  
RUN sudo pip install nose "ipython[notebook]"  
  
# Install Java.  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
# Install Spark  
ENV SPARK_HOME=/usr/local/spark  
RUN mkdir -p $SPARK_HOME  
RUN mkdir /spark-distr  
WORKDIR /spark-distr  
RUN wget http://d3kbcqa49mib13.cloudfront.net/spark-1.6.2-bin-hadoop2.6.tgz &&
\  
tar -xzvf spark-1.6.2-bin-hadoop2.6.tgz -C $SPARK_HOME \--strip-components 1
&& \  
rm spark-1.6.2-bin-hadoop2.6.tgz  
  
RUN echo "export SPARK_HOME=/usr/local/spark" >> $HOME/.bashrc  
RUN echo "export PATH=$PATH:$SPARK_HOME/bin" >> $HOME/.bashrc  
ENV
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$SPARK_HOME/bin  
  
ENV PYSPARK_DRIVER_PYTHON=jupyter  
ENV PYSPARK_DRIVER_PYTHON_OPTS="notebook --no-browser --port=8888
--ip=0.0.0.0"  
WORKDIR /root  
  
EXPOSE 6066 7077 8020 8080 8081 8888 19888 50010 50020 50070 50075 50090  
CMD pyspark --master local[2]  
  

