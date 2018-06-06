FROM ubuntu  
  
MAINTAINER Cillie Malan <cilliemalan@gmail.com>  
  
ADD prime.sh /prime.sh  
  
# some apt stuff  
RUN sudo apt-get -y update && \  
sudo apt-get -y install build-essential unzip wget curl git python-pip
libkrb5-dev  
  
# node from ppa  
RUN curl -sL https://deb.nodesource.com/setup_0.12 | sudo -E bash - && \  
sudo apt-get install -y nodejs  
  
# update npm  
RUN sudo npm install -g npm  
  
# some node stuff  
RUN sudo npm install yo grunt-cli bower gulp -g  
  
# aws stuff  
RUN sudo pip install awscli  
  
# nvm  
#RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.26.1/install.sh | bash  
# some npm stuff  
RUN ["/bin/bash", "/prime.sh"]  
  
#java  
RUN sudo apt-get -y update && \  
sudo apt-get install -y software-properties-common python-software-properties
&& \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
sudo /usr/bin/debconf-set-selections && \  
sudo add-apt-repository -y ppa:webupd8team/java && \  
sudo apt-get update && \  
sudo apt-get install -y oracle-java8-installer

