############################################################  
# Dockerfile to build Lordec tool container image  
# Based on debian wheezy  
############################################################  
  
# Set the base image to debian wheezy  
FROM debian:wheezy  
  
# Set noninterative mode  
ENV DEBIAN_FRONTEND noninteractive  
ENV PACKAGES wget make cmake gcc g++ zlib1g-dev libboost-dev  
  
ENV TAR http://www.atgc-
montpellier.fr/download/sources/lordec/LoRDEC-0.6.tar.gz  
ENV SOURCE LoRDEC-0.6  
ENV DIR /opt  
  
################## DEPENDENCIES INSTALLATION ######################  
  
RUN apt-get update -y  
RUN apt-get install -y ${PACKAGES}  
  
################## LORDEC INSTALLATION ######################  
  
WORKDIR ${DIR}  
RUN wget ${TAR} -O - | tar xvzf -  
  
WORKDIR ${DIR}/${SOURCE}  
RUN make install_dep  
RUN make  
  
RUN ln -s ${DIR}/${SOURCE}/lordec-stat /usr/local/bin  
RUN ln -s ${DIR}/${SOURCE}/lordec-correct /usr/local/bin  
RUN ln -s ${DIR}/${SOURCE}/lordec-trim /usr/local/bin  
RUN ln -s ${DIR}/${SOURCE}/lordec-trim-split /usr/local/bin  
RUN ln -s ${DIR}/${SOURCE}/lordec-build-SR-graph /usr/local/bin  
  
##################### Maintainer #####################  
  
MAINTAINER Monjeaud Cyril <Cyril.Monjeaud@irisa.fr>  
  
#################### Example ########################  
# docker run -it --rm cmonjeau/lordec  
# docker run -it --rm -v /home/user/Lordec:/data cmonjeau/lordec lordec-stat
-i /data/pac-10Kl.fa -2 /data/rcc745-10K.fq -k 31 -s 1 -S
/data/results/stat_file  
# docker run -it --rm -v /home/user/Lordec:/data cmonjeau/lordec lordec-
correct -i /data/pac-10Kl.fa -2 /data/rcc745-10K.fq -k 31 -s 1 -o
/data/results/output_reads.fq  
# docker run -it --rm -v /home/user/Lordec:/data cmonjeau/lordec lordec-trim
-i /data/pac-10Kl.fa -o /data/results/output_trim.fa  
# docker run -it --rm -v /home/user/Lordec:/data cmonjeau/lordec lordec-trim-
split -i /data/pac-10Kl.fa -o /data/results/output_trim.fa  
# docker run -it --rm -v /home/user/Lordec:/data cmonjeau/lordec lordec-build-
SR-graph -2 /data/rcc745-10K.fq -k 31 -s 1 -g /data/results/output_graph  
  

