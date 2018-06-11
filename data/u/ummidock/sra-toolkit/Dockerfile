#DOCKERFILE FOR FASQ-DUMP  
FROM ubuntu:16.04  
MAINTAINER Tiago Jesus, tiagojesus@medicina.ulisboa.pt  
  
#SET WORKDIR  
WORKDIR /NGStools/  
  
#INSTALL APT DEPENDENCIES  
RUN apt-get update  
RUN apt-get install -y wget  
  
#DOWNLOAD FASTQ-DUMP  
RUN wget https://ftp-
trace.ncbi.nlm.nih.gov/sra/sdk/2.8.2-1/sratoolkit.2.8.2-1-ubuntu64.tar.gz  
  
#EXTRACT THE FOLDER  
RUN tar -zxvf sratoolkit.2.8.2-1-ubuntu64.tar.gz  
  
ENV PATH="/NGStools/sratoolkit.2.8.2-1-ubuntu64/bin:${PATH}"  

