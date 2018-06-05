# DOCKERFILE for skesa  
FROM ubuntu:16.04  
MAINTAINER Diogo N. Silva, diogosilva@medicina.ulisboa.pt  
  
RUN apt-get update && apt-get -y install \  
bash \  
python3 \  
wget  
  
WORKDIR /NGStools/skesa  
  
RUN wget ftp://ftp.ncbi.nlm.nih.gov/pub/agarwala/skesa/skesa.static && mv
skesa.static skesa && chmod +x skesa  
  
ENV PATH="/NGStools/skesa/:$PATH"  

