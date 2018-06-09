FROM openjdk:jre-slim  
LABEL maintainer="Christian Diener <mail (at) cdiener.com>"  
  
ENV HADOOP_VERSION="2.8.2"  
ENV HADOOP_CONF_DIR="/etc/hadoop"  
COPY start_server /bin  
COPY make_data.py /bin  
RUN apt-get update && \  
apt-get install -y --no-install-recommends wget bash python3 python3-pip  
RUN cd /root && \  
wget -q http://www-
eu.apache.org/dist/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz
&& \  
tar -xzf hadoop-${HADOOP_VERSION}.tar.gz && cp -rf hadoop-${HADOOP_VERSION}/*
.. && \  
rm -rf hadoop-${HADOOP_VERSION} && rm hadoop-${HADOOP_VERSION}.tar.gz && \  
chmod +x /bin/start_server /bin/make_data.py && python3 -m pip install faker  
  
ENTRYPOINT [ "/bin/bash", "/bin/start_server" ]  

