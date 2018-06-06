#USE BLAST BINARIES FROM UMMIDOCK REPO  
FROM ummidock/blast_binaries:2.6.0-binaries  
MAINTAINER Diogo N Silva, diogosilva@medicina.ulisboa.pt  
  
WORKDIR /NGStools/  
  
RUN apt-get update && apt-get install -y \  
git \  
make \  
python3-dev \  
python3-numpy \  
python3-pip \  
gcc \  
wget \  
libxml2-dev \  
libxslt1-dev \  
libblas-dev \  
liblapack-dev \  
zlib1g-dev \  
g++ \  
build-essential  
  
#GET chewBBACA and Prodigal  
RUN git clone https://github.com/hyattpd/Prodigal.git  
RUN git clone -b chewbbaca_py3 https://github.com/B-UMMI/chewBBACA.git  
  
#INSTALL chewBBACA requirements  
WORKDIR /NGStools/chewBBACA  
RUN pip3 install -r requirements.txt  
RUN pip3 install --upgrade numpy  
  
#INSTALL PRODIGAL  
WORKDIR /NGStools/Prodigal  
RUN make install  
  
WORKDIR /NGStools/  
  
#ADD chewBBACA TO PATH  
ENV PATH="/NGStools/chewBBACA:${PATH}"  
ENV PATH="/NGStools/chewBBACA/utils:${PATH}"  
ENV PATH="/NGStools/chewBBACA/allelecall:${PATH}"  
ENV PATH="/NGStools/chewBBACA/createschema:${PATH}"  
ENV PATH="/NGStools/chewBBACA/SchemaEvaluator:${PATH}"  

