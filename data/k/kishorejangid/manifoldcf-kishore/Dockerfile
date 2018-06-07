FROM openjdk:8-jdk  
  
LABEL maintainer "kishorejangid@live.com"  
  
#Install git  
RUN apt-get update && apt-get install -y \  
git  
  
# Installs Ant  
ENV ANT_VERSION 1.9.9  
RUN cd && \  
wget -q http://archive.apache.org/dist/ant/binaries/apache-
ant-${ANT_VERSION}-bin.tar.gz && \  
tar -xzf apache-ant-${ANT_VERSION}-bin.tar.gz && \  
mv apache-ant-${ANT_VERSION} /opt/ant && \  
rm apache-ant-${ANT_VERSION}-bin.tar.gz  
ENV ANT_HOME /opt/ant  
ENV PATH ${PATH}:${ANT_HOME}/bin  
  
#Clone Apache ManifoldCF  
RUN git clone \--depth 1 https://github.com/apache/manifoldcf.git  
  
WORKDIR ./manifoldcf  
  
# Build ManifoldCF  
RUN ant -d make-core-deps build  
  
WORKDIR /manifoldcf/dist/example  
  
EXPOSE 8345  
RUN /manifoldcf/dist/example/start.sh  

