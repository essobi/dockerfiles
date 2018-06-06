FROM ubuntu:16.04  
MAINTAINER Channel IT Services, LLC  
ENV\  
DEBIAN_FRONTEND=noninteractive  
RUN\  
apt-get update &&\  
apt-get install -y vim curl sudo wget openssh-server openssh-client rsync &&\  
apt-get update && apt-get -y upgrade &&\  
apt-get install -y software-properties-common &&\  
add-apt-repository ppa:webupd8team/java &&\  
apt-get update &&\  
echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true"
| sudo debconf-set-selections &&\  
apt-get install -y oracle-java8-installer &&\  
apt-get update &&\  
apt-get clean  

