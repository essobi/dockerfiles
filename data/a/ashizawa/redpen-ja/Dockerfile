FROM ubuntu:latest  
  
WORKDIR /tmp  
  
RUN locale-gen ja_JP.UTF-8  
  
ENV LANG=ja_JP.UTF-8 LANGUAGE=ja_JP:ja LC_ALL=ja_JP.UTF-8 VERSION="1.8.0"  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-
set-selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
apt-get update && \  
apt-get -y install software-properties-common && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get -y install oracle-java8-installer oracle-java8-set-default && \  
echo "export JAVA_HOME=/usr/lib/jvm/java-8-oracle" >> /etc/environment && \  
wget -q https://github.com/redpen-
cc/redpen/releases/download/redpen-${VERSION}/redpen-${VERSION}.tar.gz -O - |
tar xz && \  
cp -av redpen-distribution-${VERSION}/* /usr/local/ && \  
rm -rf redpen-distribution-${VERSION} && \  
export PATH=$PATH:/usr/local/bin  
  
WORKDIR /data  
  
CMD ["/usr/local/bin/redpen"]  

