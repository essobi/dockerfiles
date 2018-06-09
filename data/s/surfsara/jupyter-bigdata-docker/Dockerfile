FROM jupyter/all-spark-notebook  
  
USER root  
  
RUN apt-get -y update && \  
apt-get install -yq \  
krb5-user \  
python-krbv \  
libkrb5-dev \  
libsasl2-dev \  
libsasl2-modules-gssapi-heimdal  
  
RUN cd /opt && \  
git clone https://github.com/sara-nl/hathi-client && \  
cd hathi-client && \  
git checkout spark-2.0 && \  
cp /opt/hathi-client/conf/krb5.conf /etc/krb5.conf && \  
/opt/hathi-client/bin/get.sh hadoop && \  
/opt/hathi-client/bin/get.sh spark && \  
ln -s /opt/conda/envs/python2/bin/python2 /usr/local/bin/python2.7  
  
COPY spark-defaults.conf /usr/local/spark/conf/  
COPY spark-env.sh /usr/local/spark/conf/  
  
RUN chmod -R 755 /usr/local/spark  
  
ENV CLIENT_DIR=/opt/hathi-client  
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/  
ENV KRB5_CONFIG=/opt/hathi-client/conf/krb5.conf  
ENV HADOOP_HOME=/opt/hathi-client/hadoop  
ENV HADOOP_CONF=/opt/hathi-client/hadoop/etc/hadoop  
ENV HADOOP_CONF_DIR=/opt/hathi-client/hadoop/etc/hadoop  
ENV
PATH=/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/hathi-
client/hadoop/bin:/opt/hathi-client:/usr/local/spark/bin  
ENV PYSPARK_PYTHON=/usr/local/bin/python2.7  
  
USER jovyan  
  
USER root  

