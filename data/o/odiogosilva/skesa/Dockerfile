# DOCKERFILE for skesa  
FROM ummidock/assemblerflow_base:1.0.0  
MAINTAINER Diogo N. Silva, diogosilva@medicina.ulisboa.pt  
  
RUN apt-get update && apt-get -y install \  
bash \  
wget  
  
WORKDIR /NGStools/skesa  
  
RUN wget ftp://ftp.ncbi.nlm.nih.gov/pub/agarwala/skesa/skesa.static && mv
skesa.static skesa && chmod +x skesa  
  
ENV PATH="/NGStools/skesa/:$PATH"  

