# DOCKERFILE for spades  
FROM ubuntu:16.04  
MAINTAINER Inês Mendes, cimendes@medicina.ulisboa.pt  
  
RUN apt-get update && apt-get -y install \  
bash \  
python \  
python3 \  
wget  
  
WORKDIR /NGStools  
  
RUN wget http://cab.spbu.ru/files/release3.12.0/SPAdes-3.12.0-Linux.tar.gz &&
tar -xf SPAdes-3.12.0-Linux.tar.gz  
  
ENV PATH="/NGStools/SPAdes-3.12.0-Linux/bin:$PATH"

