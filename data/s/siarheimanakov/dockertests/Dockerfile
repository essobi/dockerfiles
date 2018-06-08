#################################################################  
# Dockerfile  
#  
# Version: 1  
# Software: bowtie  
# Software Version: 1.1.2  
# Description: An ultrafast memory-efficient short read aligner  
# Website: http://bowtie-
bio.sourceforge.net/index.shtml|https://github.com/BenLangmead/bowtie  
# Tags: Genomics  
# Provides: bowtie 1.1.2  
# Base Image: biodckr/biodocker  
# Build Cmd: docker build --rm -t biodckrdev/bowtie 1.1.2/.  
# Pull Cmd: docker pull biodckrdev/bowtie  
# Run Cmd: docker run --rm -it biodckrdev/bowtie <options> <files>  
#################################################################  
  
# Set the base image to Ubuntu  
FROM biodckr/biodocker  
  
################## BEGIN INSTALLATION ######################  
  
ENV ZIP=bowtie-1.1.2-linux-x86_64.zip  
ENV URL=https://github.com/BioDocker/software-archive/releases/download/bowtie  
ENV FOLDER=bowtie-1.1.2  
ENV DST=/home/biodocker/bin  
  
RUN wget $URL/$ZIP -O $DST/$ZIP && \  
unzip $DST/$ZIP -d $DST && \  
rm $DST/$ZIP && \  
mv $DST/$FOLDER/* $DST && \  
rmdir $DST/$FOLDER  
  
# CHANGE WORKDIR TO /DATA  
WORKDIR /data  
  
COPY BowtieInd/ /usr/local/BowtieInd/  
COPY FASTQ/ /usr/local/FASTQ/  
  
# DEFINE DEFAULT COMMAND  
CMD ["bowtie"]  
  
##################### INSTALLATION END #####################  
  
# File Author / Maintainer  
MAINTAINER Saulo Alves Aflitos <sauloal@gmail.com>  

