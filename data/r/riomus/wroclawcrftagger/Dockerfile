FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
  
  
RUN apt-get update -yq && \  
apt-get -yq install git cmake libicu-dev\  
realpath libantlr-dev libxml++2.6-dev bison \  
flex libloki-dev python-dev swig build-essential libboost-all-dev gcc p7zip-
full && \  
rm -rf /var/lib/apt/lists/*  
  
  
COPY assets/assets.7z /tmp/assets/  
  
RUN cd /tmp/assets/ && 7z x assets.7z && rm -rf /tmp/assets/assets.7z  
  
RUN sh /tmp/assets/crfpp/installCRFpp.sh &&\  
sh /tmp/assets/corpus2/installCorpus2.sh &&\  
sh /tmp/assets/morfeusz/installMorfeusz.sh &&\  
sh /tmp/assets/toki/installToki.sh &&\  
sh /tmp/assets/maca/installMaca.sh &&\  
sh /tmp/assets/wccl/installWccl.sh &&\  
sh /tmp/assets/wcrft2/installWcrft2.sh  

