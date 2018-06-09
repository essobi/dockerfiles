FROM thinkiq/ubuntu-base  
MAINTAINER Bruce McCleave <bruce@thinkiq.com>  
  
ARG HBASE_VERSION=1.3.0  
  
ENV JAVA_HOME=/usr/lib/jvm/default-java HBASE_HOME=/usr/local/hbase
PATH=$PATH:$HBASE_HOME/bin  
  
LABEL Description="HBase Dev", \  
"HBase Version"="$HBASE_VERSION"  
  
USER root  
WORKDIR /  
  
  
RUN apt-get update && \  
apt-get -y install liblzo2-dev && \  
cd /usr/local && \  
wget -t 100 --retry-connrefused -O "hbase-$HBASE_VERSION-bin.tar.gz"
"http://www.apache.org/dyn/closer.lua?filename=hbase/$HBASE_VERSION/hbase-$HBASE_VERSION-
bin.tar.gz&action=download" && \  
mkdir hbase-$HBASE_VERSION && \  
tar zxf hbase-$HBASE_VERSION-bin.tar.gz -C hbase-$HBASE_VERSION \--strip 1 &&
\  
ln -sv hbase-$HBASE_VERSION hbase && \  
rm -fv hbase-$HBASE_VERSION-bin.tar.gz && \  
{ rm -rf hbase/{docs,src}; : ; } && \  
chown -R hduser:hadoop hbase-$HBASE_VERSION && chmod -R 775
hbase-$HBASE_VERSION && \  
mkdir /hbase-zoo && \  
chmod 777 /hbase-zoo && \  
mkdir -pv /usr/local/hbase/logs && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
USER hduser  
WORKDIR /home/hduser  
  
EXPOSE 60000 60010 60020 60030

