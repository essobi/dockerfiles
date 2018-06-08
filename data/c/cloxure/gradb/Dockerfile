FROM ubuntu  
  
MAINTAINER cloxure  
  
RUN apt-get update  
  
RUN apt-get install -y software-properties-common python-software-properties  
RUN add-apt-repository ppa:openjdk-r/ppa  
RUN apt-get update  
  
RUN apt-get install -y openjdk-8-jdk  
RUN apt-get install -y wget  
  
RUN wget
https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein  
RUN chmod a+x ./lein  
  
RUN apt-get install -y git  
  
RUN git clone https://github.com/cloxure/gradb.git  

