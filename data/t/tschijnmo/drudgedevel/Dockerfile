FROM tschijnmo/gccpython:latest  
  
#  
# Spark runtime  
#  
# Java stack dependencies  
RUN apt-get update && apt-get install -y --no-install-recommends \  
openjdk-8-jre \  
openjdk-8-jdk \  
&& rm -rf /var/lib/apt/lists/*  
  
# Actually download the Spark binary.  
RUN set -ex \  
&& wget -O spark.tar.gz
"http://ftp.wayne.edu/apache/spark/spark-2.2.1/spark-2.2.1-bin-hadoop2.7.tgz"
\  
&& mkdir -p /usr/local/spark \  
&& tar -xzC /usr/local/spark --strip-components=1 -f spark.tar.gz \  
&& rm spark.tar.gz  
  
# Set the environment variables up.  
ENV SPARK_HOME /usr/local/spark  
ENV PYSPARK_PYTHON /usr/local/bin/python3  
ENV PYSPARK_DRIVER_PYTHON ${PYSPARK_PYTHON}  
ENV PYTHONPATH
${PYTHONPATH}:${SPARK_HOME}/python:${SPARK_HOME}/python/lib/py4j-0.10.4-src.zip  
ENV SPARK_LOCAL_IP 127.0.0.1  
#  
# Additional miscellaneous drudge stack dependencies  
#  
RUN set -ex \  
&& pip3 install Jinja2 sympy numpy networkx ipython pytest  
  
RUN set -ex \  
&& git clone https://github.com/tschijnmo/DummyRDD.git \  
&& cd DummyRDD \  
&& python3 setup.py install \  
&& cd .. && rm -rf DummyRDD  
  
WORKDIR /home/drudge  
  

