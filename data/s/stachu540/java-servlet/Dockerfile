FROM ubuntu:artful  
  
ADD script.sh ./  
  
RUN apt-get -y update && apt-get -y upgrade && apt-get install -y software-
properties-common curl wget zip unzip git mercurial  
RUN add-apt-repository ppa:webupd8team/java -y && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections  
RUN apt-get -y update && apt-get install -y oracle-java8-installer  
  
RUN chmod +x script.sh && /bin/bash script.sh  

