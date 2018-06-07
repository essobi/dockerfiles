############################################################  
# Dockerfile to build DiscoSNP++ tool container image  
# Based on debian wheezy  
############################################################  
  
# Set the base image to debian wheezy  
FROM debian:wheezy  
  
# Set noninterative mode  
ENV DEBIAN_FRONTEND noninteractive  
ENV PACKAGES wget make cmake gcc g++ zlib1g-dev bwa python git  
  
ENV TAR
https://github.com/GATB/DiscoSnp/releases/download/v2.2.9/DiscoSNP.-v2.2.9-Source.tar.gz  
ENV SOURCE DiscoSNP++-v2.2.9-Source  
ENV DIR /opt  
  
################## DEPENDENCIES INSTALLATION ######################  
  
RUN apt-get update -y  
RUN apt-get install -y ${PACKAGES}  
  
################## DISCOSNP INSTALLATION ######################  
  
WORKDIR ${DIR}  
RUN wget ${TAR} -O - | tar xvzf -  
  
WORKDIR ${DIR}/${SOURCE}  
RUN sh INSTALL  
  
ENTRYPOINT ["./run_discoSnp++.sh"]  
CMD ["-help"]  
  
##################### Maintainer #####################  
  
MAINTAINER Monjeaud Cyril <Cyril.Monjeaud@irisa.fr>  
  
#################### Example ########################  
# docker run -it --rm cmonjeau/discosnppp  
# docker run -it --rm -v /home/user/discoSNP_data:/data cmonjeau/discosnppp -r
"/data/reads_sequence1.fasta.gz /data/reads_sequence2.fasta.gz" -G
/data/reference_genome.fa -p /data/results/discoRes  
  

