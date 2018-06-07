# DOCKERFILE for seq_typing https://github.com/B-UMMI/seq_typing  
FROM odiogosilva/rematch:latest  
MAINTAINER Diogo N. Silva, diogosilva@medicina.ulisboa.pt  
  
RUN apt-get update && apt-get -y install \  
python3-pip  
  
WORKDIR /NGStools  
  
RUN git clone https://github.com/B-UMMI/seq_typing.git  
RUN pip3 install future  
ENV PATH="/NGStools/seq_typing:$PATH"  
RUN chmod -R o+wr /NGStools/  
  
WORKDIR /data/  
  

