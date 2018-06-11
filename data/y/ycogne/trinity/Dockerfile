FROM debian:wheezy  
MAINTAINER Yannick Cogne  
# make sure the package repository is up to date  
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y wget  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y bzip2  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y procps  
RUN wget --no-check-certificate
https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh  
RUN chmod +x Miniconda2-latest-Linux-x86_64.sh  
RUN bash Miniconda2-latest-Linux-x86_64.sh -b -p /usr/miniconda2  
ENV PATH /usr/miniconda2/bin:$PATH  
RUN conda config --add channels r  
RUN conda config --add channels conda-forge  
RUN conda config --add channels bioconda  
RUN conda install Trinity  
RUN chmod a+xw -R /usr/miniconda2/  
RUN mkdir /home/results  
RUN chmod a+xwr -R /home/results  
RUN apt-get clean  

