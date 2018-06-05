FROM ubuntu:16.04  
MAINTAINER Bruno Gonçalves, bfgoncalves@medicina.ulisboa.pt  
  
#DEFINE WORKDIR  
WORKDIR /NGStools/  
  
#INSTALL DEPENDENCIES  
RUN apt-get update  
RUN apt-get install -y make wget bzip2 gcc libz-dev  
  
#DOWNLOAD AND EXTRACT BWA  
RUN wget https://downloads.sourceforge.net/project/bio-bwa/bwa-0.7.15.tar.bz2  
RUN tar -jxvf bwa-0.7.15.tar.bz2  
  
#CHANGE TO BOWTIE DIR  
WORKDIR ./bwa-0.7.15  
  
#RUN MAKE AND ADD TO PATH  
RUN make  
ENV PATH="/NGStools/bwa-0.7.15:${PATH}"  

