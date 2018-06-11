# docker pull eason02/alpine-ant:1.9.9  
FROM java:7-alpine  
  
MAINTAINER Eason Lau <eason.lau02@hotmail.com>  
  
ENV ANT_VERSION=1.9.9  
ENV ANT_HOME=/opt/ant  
ENV PATH=$PATH:$ANT_HOME/bin  
  
RUN mkdir -p /opt/ && \  
wget http://apache.website-solution.net//ant/binaries/apache-
ant-${ANT_VERSION}-bin.tar.gz && \  
tar -xzvf apache-ant-${ANT_VERSION}-bin.tar.gz -C /opt/ && \  
ln -s /opt/apache-ant-${ANT_VERSION}/ /opt/ant && \  
rm -f /apache-ant-${ANT_VERSION}-bin.tar.gz  
  
RUN export && \  
ant -version  

