FROM ubuntu:trusty  
  
RUN echo "deb http://repos.mesosphere.io/ubuntu/ trusty main" >
/etc/apt/sources.list.d/mesosphere.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv E56151BF && \  
apt-get update && \  
apt-get install -y maven \  
node \  
npm \  
default-jdk \  
mesos \  
scala \  
curl git  
  
RUN git clone https://github.com/mesos/chronos.git /chronos  
  
WORKDIR /chronos  
  
RUN mvn clean package  
  
EXPOSE 8081  
ENTRYPOINT ["bin/start-chronos.bash"]  

