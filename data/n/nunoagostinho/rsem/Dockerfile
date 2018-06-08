FROM ubuntu:16.10  
MAINTAINER Nuno Agostinho <nunodanielagostinho@gmail.com>  
  
RUN apt-get update  
  
# RSEM  
RUN apt-get install -y rsem  
  
# STAR  
RUN apt-get install -y make  
ENV SW=/root/software/  
RUN mkdir -p ${SW}  
WORKDIR ${SW}  
ENV STAR="STAR"  
COPY ${STAR} ${STAR}  
WORKDIR "${SW}/${STAR}/source"  
RUN make STAR  
ENV PATH="${PATH}:${SW}/${STAR}/bin/Linux_x86_64/"  
WORKDIR ${SW}  
  
# BOWTIE and BOWTIE2  
RUN apt-get install -y bowtie  
RUN apt-get install -y bowtie2  
  
# samtools  
RUN apt-get install -y samtools  
  
# boost C++  
RUN apt-get install -y libboost-all-dev

