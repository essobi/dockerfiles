############################################################  
# Dockerfile to build Kissplice tool container image  
# Based on debian wheezy  
############################################################  
  
# Set the base image to debian wheezy  
FROM debian:wheezy  
  
# Set noninterative mode  
ENV DEBIAN_FRONTEND noninteractive  
ENV PACKAGES wget make cmake gcc g++ zlib1g-dev python  
  
ENV TAR ftp://pbil.univ-
lyon1.fr/pub/logiciel/kissplice/download/kissplice-2.2.1.tar.gz  
ENV SOURCE kissplice-2.2.1  
ENV DIR /opt  
  
################## DEPENDENCIES INSTALLATION ######################  
  
RUN apt-get update -y  
RUN apt-get install -y ${PACKAGES}  
  
################## KISSPLICE INSTALLATION ######################  
  
WORKDIR ${DIR}  
RUN wget ${TAR} -O - | tar xvzf -  
RUN mkdir ${DIR}/${SOURCE}/build  
WORKDIR ${DIR}/${SOURCE}/build  
  
RUN cmake ..  
RUN make  
RUN make install  
  
ENTRYPOINT ["kissplice"]  
CMD ["--help"]  
  
##################### Maintainer #####################  
  
MAINTAINER Monjeaud Cyril <Cyril.Monjeaud@irisa.fr>  
  
#################### Example ########################  
# docker run -it --rm cmonjeau/kissplice  
# docker run -it --rm -v /home/user/Kissplice:/data cmonjeau/kissplice -r
/data/reads1.fa -r /data/reads2.fa -o /data  
  

