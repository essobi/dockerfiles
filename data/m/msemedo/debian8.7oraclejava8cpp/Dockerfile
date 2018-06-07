FROM msemedo/debian8.7upgraded:latest  
LABEL maintainer "Marcello DB Semedo"  
  
RUN apt-get -y update && \  
apt-get install -y software-properties-common \  
build-essential \  
gdb &&\  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee
/etc/apt/sources.list.d/webupd8team-java.list &&\  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list &&\  
apt-key adv \--keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886
&&\  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
apt-get -y update && \  
apt-get install -y oracle-java8-installer && \  
apt-get clean  
CMD /bin/bash  

