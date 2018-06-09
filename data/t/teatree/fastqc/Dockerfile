# Docker container to temproarily unzip fastq.gz files to then perform fastqc
on these fastq files.  
#Pull baseimage  
FROM ubuntu:14.04.4  
#FROM openjdk:7  
#download fastqc software  
ENV VERSION v0.11.5  
MAINTAINER Annemarie Eckes, Annemarie.Eckes@earlham.ac.uk  
#This Docker file is based on
https://hub.docker.com/r/conradstoerker/fastqc/~/dockerfile/  
# download and install FastQC  
RUN apt update  
RUN apt install -y wget  
RUN apt install unzip  
RUN sudo apt-get install --yes openjdk-7-jre-headless  
RUN wget
"http://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_${VERSION}.zip"  
RUN unzip fastqc_${VERSION}.zip  
  
RUN chmod 777 FastQC/fastqc  
RUN ln -s FastQC/fastqc /usr/local/bin/fastqc  
  
# Creating directories to use  
RUN mkdir /fastqc  
RUN mkdir /fastqc/data  
  
COPY fastqc.sh /tmp/fastqc.sh  
RUN chmod 777 /tmp/fastqc.sh  
  
WORKDIR /tmp/  
ENTRYPOINT ["/tmp/fastqc.sh"]  

