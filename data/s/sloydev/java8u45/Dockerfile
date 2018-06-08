FROM ubuntu  
  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y wget && \  
rm -rf /var/lib/apt/lists/*  
  
  
RUN \  
mkdir /opt/jdk && cd /opt && \  
wget --header "Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-pub/java/jdk/8u45-b14/jdk-8u45-linux-x64.tar.gz
&& \  
tar -zxf jdk-8u45-linux-x64.tar.gz -C /opt/jdk && \  
update-alternatives --install /usr/bin/java java /opt/jdk/jdk1.8.0_45/bin/java
100

