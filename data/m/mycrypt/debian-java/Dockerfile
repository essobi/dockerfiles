FROM mycrypt/debian  
  
MAINTAINER Bai Xiaoyong "lostitle@gmail.com"  
# Install Java.  
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
apt-get install -y oracle-java7-installer &&\  
apt-get clean  
  
RUN echo "JAVA_HOME=/usr/lib/jvm/java-7-oracle" >> /etc/environment  
#ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  

