FROM ubuntu:14.04  
  
MAINTAINER devops <nitanka.gogoi@razorthink.com>  
ARG SPARK_URL="http://d3kbcqa49mib13.cloudfront.net/spark-2.1.0-bin-
hadoop2.7.tgz"  
ARG PYTHON35_URL="https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz"  
  
RUN apt-get update && \  
apt-get install -y software-properties-common python-software-properties curl
build-essential checkinstall && \  
apt-get install -y libreadline-gplv2-dev libncursesw5-dev libssl-dev tk-dev
libgdbm-dev libc6-dev libbz2-dev && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
cd /tmp && \  
curl -O ${SPARK_URL} && \  
tar -xzf spark-2.1.0-bin-hadoop2.7.tgz && \  
mv spark-2.1.0-bin-hadoop2.7 /opt/spark && \  
echo "#!/bin/bash" > /root/start-master.sh && \  
echo "/opt/spark/bin/spark-class org.apache.spark.deploy.master.Master --host
0.0.0.0" >> /root/start-master.sh && \  
chmod +x /root/start-master.sh && \  
cd /tmp && curl -O ${PYTHON35_URL} && \  
tar -xzf `basename ${PYTHON35_URL}` && \  
rm `basename ${PYTHON35_URL}` && \  
mv `basename -s .tgz ${PYTHON35_URL}` /usr/src/ && \  
cd /usr/src/`basename -s .tgz ${PYTHON35_URL}` && ./configure && make
altinstall && \  
python3.5 -m pip install --upgrade pip boto pyhdfs smart_open matplotlib
sphinx_rtd_theme jsonpickle jinja2 flask flask-httpauth \  
pandas boto3 scipy sklearn gitchangelog pythonbenchmark pyhdfs typeguard
sphinx-autodoc-typehints pyyaml cython nose coloredlogs \  
check-manifest flake8 bunch coverage  
  
  
ENV JAVA_HOME=/usr/lib/jvm/java-8-oracle  
ENV SPARK_HOME=/opt/spark  
ENV PATH=${PATH}:${SPARK_HOME}/bin  
ENV PATH=${PATH}:${SPARK_HOME}/sbin  
  
CMD ["/root/start-master.sh"]  
EXPOSE 4000-40000  

