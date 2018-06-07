FROM ubuntu:14.04  
RUN apt-get -y update  
RUN apt-get -y install software-properties-common  
RUN add-apt-repository -y ppa:ethereum/ethereum-qt  
RUN add-apt-repository -y ppa:ethereum/ethereum  
RUN apt-get -y update  
RUN apt-get -y install ethminer  
ADD run.sh .  
CMD sh run.sh  

