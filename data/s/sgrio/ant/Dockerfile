FROM sgrio/java-oracle:jdk_8  
MAINTAINER SgrAlpha <admin@mail.sgr.io>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV ANT_VERSION 1.10.1  
ENV ANT_HOME /opt/apache-ant  
ENV PATH ${ANT_HOME}/bin:$PATH  
  
RUN curl --silent --location --retry 3 \  
http://archive.apache.org/dist/ant/binaries/apache-
ant-${ANT_VERSION}-bin.tar.gz \  
| tar xz -C /tmp && \  
mv /tmp/apache-ant-${ANT_VERSION} /opt/apache-ant-${ANT_VERSION} && \  
ln -s /opt/apache-ant-${ANT_VERSION} ${ANT_HOME} && \  
rm -rf /tmp/*  
  
WORKDIR ${ANT_HOME}  

