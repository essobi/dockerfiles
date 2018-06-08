# docker build --rm -t ipyrad .  
FROM ubuntu:16.04  
MAINTAINER Mario David <mariojmdavid@gmail.com>  
LABEL description="Run ipyrad"  
  
RUN apt-get update -y  
RUN apt-get install software-properties-common bzip2 tar wget -y  
  
RUN apt-get update -y  
RUN cd /home && wget https://repo.continuum.io/miniconda/Miniconda-latest-
Linux-x86_64.sh  
RUN bash /home/Miniconda-latest-Linux-x86_64.sh -b  
ENV PATH $PATH:/root/miniconda2/bin  
RUN conda update conda  
RUN conda install -c ipyrad ipyrad  
RUN apt-get clean  

