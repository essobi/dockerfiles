# Base docker image  
FROM debian:stretch  
MAINTAINER François Billant <fbillant@gmail.com>  
  
RUN useradd -ms /bin/bash jd  
  
COPY JDownloader.jar /home/jd/JDownloader.jar  
RUN chown jd:jd /home/jd/JDownloader.jar  
  
RUN sed -i.bak 's/stretch main/stretch main contrib non-free/g'
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y \  
wget \  
libxext6 \  
libxrender1 \  
libxtst6  
  
# Install Oracle JRE  
RUN cd /opt && \  
mkdir /opt/jre && \  
cd /opt/jre && \  
wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/8u161-b12/2f38c3b165be4555a1fa6e98c45e0808/jre-8u161-linux-x64.tar.gz
&& \  
tar -xvzf jre-*  
  
RUN update-alternatives --install /usr/bin/java java
/opt/jre/jre1.8.0_161/bin/java 100 && \  
java -version  
  
WORKDIR /home/jd  
  
# Autorun jdowloader  
CMD ["/usr/bin/java","-jar","/home/jd/JDownloader.jar"]  

