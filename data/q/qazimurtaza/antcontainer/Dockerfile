FROM ubuntu:14.04  
MAINTAINER Qazi Murtaza <qazi.murtaza@faircg.com>  
  
RUN apt-get update && \  
apt-get install -y --force-yes software-properties-common && \  
add-apt-repository ppa:webupd8team/java -y && \  
apt-get update && \  
echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java8-installer && \  
apt-get clean  
  
ENV ANT_VERSION 1.10.3  
RUN cd && \  
wget -q http://www.us.apache.org/dist/ant/binaries/apache-
ant-${ANT_VERSION}-bin.tar.gz && \  
tar -xzf apache-ant-${ANT_VERSION}-bin.tar.gz && \  
mv apache-ant-${ANT_VERSION} /opt/ant && \  
rm apache-ant-${ANT_VERSION}-bin.tar.gz  
  
ENV ANT_HOME /opt/ant  
ENV PATH ${PATH}:/opt/ant/bin  
  
RUN mkdir /src  
RUN mkdir /src/bin  
RUN mkdir /src/bin/platform  
  
WORKDIR /src/bin/platform  
  
ENTRYPOINT ["ant"]

