FROM centos  
  
RUN yum install -y java-1.8.0-openjdk-devel  
RUN yum install -y wget  
RUN yum install -y unzip  
RUN yum install -y net-tools  
RUN echo "export JAVA_HOME=/usr/lib/jvm/java" >> /root/.bashrc  
  
ARG
HBASE_URL=https://archive.apache.org/dist/hbase/1.2.5/hbase-1.2.5-bin.tar.gz  
ARG PHOENIX_URL=https://archive.apache.org/dist/phoenix/apache-
phoenix-4.10.0-HBase-1.2/bin/apache-phoenix-4.10.0-HBase-1.2-bin.tar.gz  
  
ARG HBASE_VER=hbase-1.2.5  
ARG PHOENIX_VER=4.10.0-HBase-1.2  
# Setup HBase binaries  
RUN wget -nv ${HBASE_URL} -O /hbase.tgz  
RUN tar -xzvf /hbase.tgz  
RUN mv /${HBASE_VER} /hbase  
  
# Setup Phoenix binaries  
RUN wget -nv ${PHOENIX_URL} -O /phoenix.tgz  
RUN tar -xzvf /phoenix.tgz  
RUN mv /apache-phoenix-${PHOENIX_VER}-bin /phoenix  
RUN cp /phoenix/phoenix-${PHOENIX_VER}-server.jar /hbase/lib  
  
ADD conf /hbase/conf  
CMD source /root/.bashrc; sh /hbase/bin/start-hbase.sh; sleep 10;
/phoenix/bin/queryserver.py  

