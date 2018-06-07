FROM ubuntu:16.04  
MAINTAINER Miguel Machado <mpmachado@medicina.ulisboa.pt>  
  
WORKDIR /NGStools/  
  
RUN apt-get update  
  
# Dependencies  
RUN apt-get install -y git python-dev python-pip wget && pip install -U numpy
biopython pysam pandas  
  
# HMMER  
RUN wget http://eddylab.org/software/hmmer3/3.1b2/hmmer-3.1b2-linux-
intel-x86_64.tar.gz && tar xf hmmer-3.1b2-linux-intel-x86_64.tar.gz && rm
hmmer-3.1b2-linux-intel-x86_64.tar.gz  
  
# vsearch  
RUN wget
https://github.com/torognes/vsearch/releases/download/v2.4.3/vsearch-2.4.3-linux-x86_64.tar.gz
&& tar xf vsearch-2.4.3-linux-x86_64.tar.gz && rm
vsearch-2.4.3-linux-x86_64.tar.gz  
  
# MIDAS  
RUN git clone https://github.com/snayfach/MIDAS  
  
ENV PYTHONPATH="/NGStools/MIDAS:${PYTHONPATH}"
PATH="/NGStools/MIDAS/scripts:/NGStools/hmmer-3.1b2-linux-
intel-x86_64/binaries:/NGStools/vsearch-2.4.3-linux-x86_64/bin:${PATH}"  
# Clean  
RUN apt-get remove -y git python-pip wget && apt-get autoclean -y  
  
WORKDIR /data/  

