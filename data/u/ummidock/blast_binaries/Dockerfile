FROM ubuntu:16.04  
MAINTAINER Miguel Machado <mpmachado@medicina.ulisboa.pt>  
  
WORKDIR /NGStools/  
  
RUN apt-get update  
  
RUN apt-get install -y wget  
RUN apt-get install -y tar  
  
# Blast+  
RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.6.0/ncbi-
blast-2.6.0+-x64-linux.tar.gz && tar xf ncbi-blast-2.6.0+-x64-linux.tar.gz &&
rm ncbi-blast-2.6.0+-x64-linux.tar.gz  
  
ENV PATH="/NGStools/ncbi-blast-2.6.0+/bin:${PATH}"  
RUN apt-get remove -y wget  
RUN apt-get autoclean -y  

