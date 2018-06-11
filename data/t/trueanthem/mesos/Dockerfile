FROM trueanthem/spark  
  
RUN echo "deb http://repos.mesosphere.io/debian wheezy main" | tee
/etc/apt/sources.list.d/mesosphere.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv E56151BF && \  
apt-get -y update && \  
apt-get -y install mesos=0.22.1-1.0.debian78  

