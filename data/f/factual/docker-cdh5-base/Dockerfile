FROM factual/docker-base-java  
  
ENV CDH_VERSION 5.13  
COPY cloudera.pref /etc/apt/preferences.d/cloudera.pref  
RUN echo "deb [arch=amd64]
http://archive.cloudera.com/cdh5/ubuntu/trusty/amd64/cdh trusty-
cdh${CDH_VERSION} contrib" >> /etc/apt/sources.list.d/cloudera.list && \  
echo "deb-src http://archive.cloudera.com/cdh5/ubuntu/trusty/amd64/cdh trusty-
cdh${CDH_VERSION} contrib" >> /etc/apt/sources.list.d/cloudera.list && \  
echo "deb [arch=amd64]
http://archive.cloudera.com/gplextras5/ubuntu/trusty/amd64/gplextras trusty-
gplextras${CDH_VERSION} contrib" >> /etc/apt/sources.list.d/gplextras.list &&
\  
echo "deb-src
http://archive.cloudera.com/gplextras5/ubuntu/trusty/amd64/gplextras trusty-
gplextras${CDH_VERSION} contrib" >> /etc/apt/sources.list.d/gplextras.list &&
\  
curl -sf https://archive.cloudera.com/cdh5/ubuntu/trusty/amd64/cdh/archive.key
> archive.key && \  
apt-key add archive.key && \  
apt-get update && \  
apt-get install -y \  
hadoop-client \  
hadoop-lzo \  
krb5-user \  
lsof  
  
  
  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

