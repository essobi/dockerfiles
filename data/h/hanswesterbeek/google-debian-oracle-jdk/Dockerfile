FROM google/debian:wheezy  
  
RUN \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu precise main" | tee
-a /etc/apt/sources.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu precise main" |
tee -a /etc/apt/sources.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 &&
\  
apt-get update  
  
RUN \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
apt-get install -y oracle-java8-installer &&\  
apt-get clean  
  
RUN echo "JAVA_HOME=/usr/lib/jvm/java-8-oracle" >> /etc/environment

