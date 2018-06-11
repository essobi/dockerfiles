FROM microsoft/vsts-agent:ubuntu-16.04-docker-17.12.0-ce-standard  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
0x219BD9C9 && \  
echo "deb http://repos.azulsystems.com/ubuntu stable main" >>
/etc/apt/sources.list.d/zulu.list && \  
apt-get update && \  
apt-get -y install zulu-7 && \  
apt-get -y install zulu-9 && \  
apt-get -y install zulu-10 && \  
apt-get -y install zulu-8 && \  
update-alternatives --set java /usr/lib/jvm/zulu-8-amd64/bin/java && \  
rm -rf /var/lib/apt/lists/*  
  
ENV JAVA_HOME_7_X64=/usr/lib/jvm/zulu-7-amd64 \  
JAVA_HOME_8_X64=/usr/lib/jvm/zulu-8-amd64 \  
JAVA_HOME_9_X64=/usr/lib/jvm/zulu-9-amd64 \  
JAVA_HOME_10_X64=/usr/lib/jvm/zulu-10-amd64 \  
JAVA_HOME=/usr/lib/jvm/zulu-8-amd64  

