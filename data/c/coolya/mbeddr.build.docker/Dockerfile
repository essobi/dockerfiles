FROM debian:jessie  
MAINTAINER Kolja Dummann <kolja.dummann@logv.ws>  
ADD ./backports.list /etc/apt/sources.list.d/backports.list  
RUN apt-get update  
RUN apt-get install -y openjdk-8-jdk \  
ant \  
build-essential \  
bison \  
ca-certificates \  
curl \  
flex \  
g++ \  
gcc \  
gdb \  
git \  
libz-dev \  
libwww-perl \  
make \  
patch \  
subversion \  
unzip \  
wget \  
zip  
  
RUN apt-get autoremove  
RUN cd /tmp && \  
wget https://github.com/aktau/github-release/releases/download/v0.6.2/linux-
amd64-github-release.tar.bz2 && \  
tar -xjvf linux-amd64-github-release.tar.bz2 && \  
mv bin/linux/amd64/github-release /usr/bin/ && \  
rm -rf bin/  
RUN mkdir /buildAgent && cd /buildAgent && \  
wget https://build.mbeddr.com/update/buildAgent.zip && \  
unzip buildAgent.zip && \  
chmod +x /buildAgent/bin/agent.sh  
ADD ./buildAgent.properties /buildAgent/conf/buildAgent.properties  
ADD ./start.sh /start  
RUN mkdir -p /root/.ssh  
ADD ./sshconfig /root/.ssh/config  
RUN chmod +x /start  
VOLUME ["/build"]  
ENTRYPOINT ["/start"]  
COPY ./bin/* /usr/bin/  
RUN chmod +x /usr/bin/*  

