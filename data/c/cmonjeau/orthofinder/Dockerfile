################################################  
# Dockerfile to build OrthoFinder software  
# Based on debian blast  
################################################  
  
# Set the base image to debian blast  
FROM simonalpha/ncbi-blast-docker  
  
LABEL version="1.1.8"  
  
# Set noninterative mode  
ENV DEBIAN_FRONTEND noninteractive  
  
################## Update & upgrade ######################  
ENV PACKAGES wget make gcc g++ mafft unzip python-pip python-dev libatlas-
base-dev gfortran  
  
RUN apt-get update -y  
RUN apt-get install -y ${PACKAGES}  
  
################# Numpy / Scipy install ########################  
RUN pip install numpy  
RUN pip install scipy  
  
################# Fastree install ########################  
ENV FASTTREE_URL http://www.microbesonline.org/fasttree/FastTree  
  
RUN wget -P /usr/local/bin ${FASTTREE_URL} && \  
chmod a+x /usr/local/bin/FastTree  
  
################# MCL install ########################  
ENV MCL_URL http://micans.org/mcl/src/mcl-14-137.tar.gz  
ENV MCL_PATH /opt/mcl-14-137  
  
WORKDIR /opt  
RUN wget ${MCL_URL} -O - | tar xvzf -  
WORKDIR ${MCL_PATH}  
  
RUN ./configure --prefix=/usr/local && make install  
  
################# DLCpar install ########################  
ENV DLCPAR_URL
https://www.cs.hmc.edu/~yjw/software/dlcpar/pub/sw/dlcpar-1.0.tar.gz  
ENV DLCPAR_PATH /opt/dlcpar-1.0  
  
WORKDIR /opt  
RUN wget ${DLCPAR_URL} --no-check-certificate -O - | tar zxvf -  
WORKDIR ${DLCPAR_PATH}  
  
RUN python setup.py install  
  
################ FastME install ##########################  
ENV FASTME_URL http://www.atgc-
montpellier.fr/download/sources/fastme/fastme-2.1.5.tar.gz  
ENV FASTME_PATH fastme-2.1.5  
  
WORKDIR /opt  
RUN wget ${FASTME_URL} --no-check-certificate -O - | tar zxvf -  
WORKDIR ${FASTME_PATH}  
  
RUN ./configure --prefix=/usr/local && make install  
  
################# DIAMOND install ########################  
ENV DIAMOND_URL
https://github.com/bbuchfink/diamond/releases/download/v0.9.9/diamond-
linux64.tar.gz  
  
WORKDIR /opt  
RUN wget ${DIAMOND_URL} --no-check-certificate -O - | tar xvzf - && mv diamond
/usr/local/bin/diamond-sse2  
  
########################### orthoFinder install & run tests
#############################  
ENV ORTHOFINDER_URL https://github.com/davidemms/OrthoFinder/archive/1.1.8.zip  
ENV ORTHOFINDER_FILE_NAME 1.1.8.zip  
ENV ORTHOFINDER_PATH /opt/OrthoFinder-1.1.8/orthofinder  
  
WORKDIR /opt  
RUN wget ${ORTHOFINDER_URL} --no-check-certificate && unzip
${ORTHOFINDER_FILE_NAME}  
ENV PATH "$PATH:${ORTHOFINDER_PATH}"  
  
WORKDIR /root  
RUN pwd && ls -1  
RUN orthofinder.py -f ${ORTHOFINDER_PATH}/ExampleDataset/  
  
########################## clean source file #################################  
  
RUN rm -r /opt/1.1.8.zip  
  
###############################################################  
  
MAINTAINER Monjeaud Cyril <Cyril.Monjeaud@irisa.fr>  

