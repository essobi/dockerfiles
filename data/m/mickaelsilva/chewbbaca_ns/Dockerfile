#USE BLAST BINARIES FROM UMMIDOCK REPO  
FROM ummidock/blast_binaries:2.6.0-binaries  
WORKDIR /NGStools/  
RUN apt-get update  
RUN apt-get install psmisc  
#RUN apt-get install -y git make python-dev gcc wget libxml2-dev libxslt1-dev
zlib1g-dev g++ build-essential  
RUN apt-get install -y git make python3 python3-pip libatlas-base-dev wget g++
build-essential python3-numpy python3-scipy  
# python3-numpy python3-scipy  
RUN python3 -m pip install --upgrade pip  
  
#GET training files and Prodigal  
RUN git clone https://github.com/hyattpd/Prodigal.git  
  
#INSTALL chewBBACA requirements  
RUN pip3 install biopython plotly SPARQLWrapper chewbbaca_ns  
  
WORKDIR /NGStools/Prodigal  
RUN make install  
WORKDIR /NGStools/  
RUN git clone https://github.com/mickaelsilva/prodigal_training_files  
  
ENV PATH="/NGStools/prodigal_training_files/:${PATH}"  
RUN chewie_ns --version  

