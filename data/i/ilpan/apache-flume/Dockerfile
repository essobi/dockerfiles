# Apache Flume  
FROM ilpan/base-java  
MAINTAINER ilpan<pna.dev@outlook.com>  
  
ENV JENV_HOME /usr/local/.jenv  
ENV FLUME_HOME $JENV_HOME/candidates/flume  
  
# install zookeeper  
RUN mkdir -p ${FLUME_HOME} && cd $JENV_HOME/archives/ && \  
wget -c https://mirrors.tuna.tsinghua.edu.cn/apache/flume/1.8.0/apache-
flume-1.8.0-bin.tar.gz && \  
tar -xzf apache-flume-1.8.0-bin.tar.gz && mv apache-flume-1.8.0-bin
$FLUME_HOME/1.8.0 && \  
bash -c "source ~/.jenv/bin/jenv-init.sh && jenv default flume 1.8.0" && \  
rm -rf $JENV_HOME/archives/*  
  

