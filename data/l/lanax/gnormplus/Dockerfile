#  
# Gnormplus Docker file  
#  
FROM ubuntu:latest  
MAINTAINER Elangovan  
  
RUN apt-get update  
  
#install oracle jdk 8  
RUN apt-get -y install software-properties-common python-software-properties  
RUN add-apt-repository ppa:webupd8team/java  
RUN apt-get -y update  
RUN echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true" | debconf-set-selections  
RUN echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 seen
true" | debconf-set-selections  
RUN apt-get -y install oracle-java8-installer  
  
#GNormPlus set up  
RUN wget -nv
https://www.ncbi.nlm.nih.gov/CBBresearch/Lu/Demo/tmTools/download/GNormPlus/GNormPlusJava.zip  
RUN apt-get -y install unzip  
RUN unzip GNormPlusJava.zip -d .  
RUN rm GNormPlusJava.zip  
  
####CRF set up for GNormPlus  
########Install C++ compilers for CRF  
RUN apt-get -y install build-essential  
RUN apt-get -y install gawk  
COPY CRFLib/CRFplusplus_v0.58.zip .  
RUN unzip CRFplusplus_v0.58.zip -d CRF58  
RUN rm CRFplusplus_v0.58.zip  
####update CRFv.058 files in GNormPlus  
RUN cp -r /CRF58/* /GNormPlusJava/CRF  
WORKDIR /GNormPlusJava/CRF  
RUN pwd  
RUN ls  
RUN chmod +x configure  
RUN ./configure  
RUN make  
RUN make install  
  
#some execute permissions that are missing  
WORKDIR /GNormPlusJava  
RUN chmod +x Ab3P  
  
WORKDIR /GNormPlusJava

