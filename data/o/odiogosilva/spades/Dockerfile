# DOCKERFILE for spades  
FROM ummidock/assemblerflow_base:1.0.0  
MAINTAINER Diogo N. Silva, diogosilva@medicina.ulisboa.pt  
  
RUN apt-get update && apt-get -y install \  
bash \  
python \  
wget  
  
WORKDIR /NGStools  
  
RUN wget
https://github.com/ablab/spades/releases/download/v3.11.0/SPAdes-3.11.0-Linux.tar.gz
&& tar -xf SPAdes-3.11.0-Linux.tar.gz  
  
ENV PATH="/NGStools/SPAdes-3.11.0-Linux/bin:$PATH"  

