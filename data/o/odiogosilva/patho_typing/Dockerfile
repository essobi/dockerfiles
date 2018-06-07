# DOCKERFILE for patho_typing https://github.com/B-UMMI/patho_typing  
FROM odiogosilva/rematch:latest  
MAINTAINER Diogo N. Silva, diogosilva@medicina.ulisboa.pt  
  
RUN apt-get update && apt-get -y install \  
python3-pip  
  
WORKDIR /NGStools  
  
RUN git clone -b jani https://github.com/B-UMMI/patho_typing.git  
RUN pip3 install future  
ENV PATH="/NGStools/patho_typing:$PATH"  
RUN chmod -R o+wr /NGStools/  
  
WORKDIR /data/  
  

