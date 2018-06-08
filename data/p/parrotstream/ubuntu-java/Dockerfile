FROM ubuntu:zesty  
  
MAINTAINER Matteo Capitanio <matteo.capitanio@gmail.com>  
  
ENV ORACLE_JDK_VER 8  
ENV JAVA_HOME /usr/lib/jvm/java-${ORACLE_JDK_VER}-oracle  
  
USER root  
  
RUN apt-get update -y; \  
apt-get install -y software-properties-common  
RUN add-apt-repository ppa:webupd8team/java; \  
apt-get update -y  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-
set-selections; \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections  
RUn apt-get install -y oracle-java${ORACLE_JDK_VER}-installer  
  
ENV PATH $JAVA_HOME/bin:$PATH  
RUN update-alternatives --install /usr/bin/java java $JAVA_HOME/bin/java 2  
RUN update-alternatives --set java $JAVA_HOME/bin/java  
  
CMD ["/bin/bash"]  

