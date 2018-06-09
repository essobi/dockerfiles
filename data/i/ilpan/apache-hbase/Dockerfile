# apache hbase  
  
FROM ilpan/apache-hadoop  
MAINTAINER ilpan<ilpan.dev@outlook.com>  
  
ENV CANDIDATES /usr/local/.jenv/candidates  
ENV HBASE_HOME ${CANDIDATES}/hbase/current/  
ENV HBASE_VERSION 1.4.1  
  
# install hbase  
# zookeeper 3.4.x and hadoop 2.7.1+ for hbase 2.x or 1.x  
RUN mkdir ${CANDIDATES}/hbase && cd /usr/local/.jenv/archives/ && \  
wget -c
http://mirrors.hust.edu.cn/apache/hbase/${HBASE_VERSION}/hbase-${HBASE_VERSION}-bin.tar.gz
&& \  
tar -xzf hbase-${HBASE_VERSION}-bin.tar.gz -C ${CANDIDATES}/hbase/ && \  
cd ${CANDIDATES}/hbase && mv hbase-${HBASE_VERSION} ${HBASE_VERSION} && \  
bash -c "source ~/.jenv/bin/jenv-init.sh && jenv default hbase
${HBASE_VERSION}" && \  
rm -rf /usr/local/.jenv/archives/*  

