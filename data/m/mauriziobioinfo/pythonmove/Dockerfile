#Reorder reference file for GATk  
#base image ubuntu  
FROM ubuntu:14.04  
# Maintainer  
MAINTAINER Maurizio Polano "mauriziopolano@blu.it"  
# update system  
RUN apt-get update && apt-get upgrade -y && apt-get dist-upgrade -y  
RUN apt-get install -y zip  
RUN apt-get install -y python-software-properties python-dev python-pip  
RUN apt-get install -y libfreetype6-dev libpng-dev libncurses5-dev vim git-
core build-essential curl unzip wget  
RUN apt-get install -y python python-pip wget  
#RUN wget
http://pypi.python.org/packages/source/b/biopython/biopython-1.65.tar.gz &&
tar xvf biopython-1.65.tar.gz && cd biopython-1.65/ && python setup.py install
-y  
RUN pip install biopython  
RUN apt-get install -y ipython  
CMD ["/bin/bash"]  
WORKDIR /home  
  

