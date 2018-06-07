# DOCKERFILE for patho_typing https://github.com/B-UMMI/patho_typing  
FROM ummidock/rematch:3.3.0-1  
MAINTAINER Diogo N. Silva, diogosilva@medicina.ulisboa.pt  
  
RUN apt-get update && apt-get -y install \  
python3-pip  
  
WORKDIR /NGStools  
  
RUN git clone https://github.com/B-UMMI/patho_typing.git  
RUN pip3 install future  
ENV PATH="/NGStools/patho_typing:$PATH"  
RUN chmod -R o+wr /NGStools/  
  
WORKDIR /data/  
  

