FROM ubuntu:latest  
MAINTAINER Mark Derbyshire <mark.derbyshire@curtin.edu.au>  
RUN apt-get update && apt-get install -y build-essential && apt-get install -y
python2.7 python-pip python-setuptools python-dev  
RUN mkdir /opt/bwa  
WORKDIR /opt/bwa  
ADD http://downloads.sourceforge.net/project/bio-
bwa/bwakit/bwakit-0.7.12_x64-linux.tar.bz2?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fbio-
bwa%2F&ts=1477377649&use_mirror=internode /opt/bwa  
RUN tar xvjf bwakit-0.7.12_x64-linux.tar.bz2 && rm *.bz2 && mv bwa.kit bwa  
ENV PATH /opt/bwa/bwa:$PATH  
WORKDIR /opt/  
RUN mkdir /opt/stampy  
WORKDIR /opt/stampy  
ADD http://www.well.ox.ac.uk/bioinformatics/Software/Stampy-latest.tgz
/opt/stampy  
RUN tar xvzf Stampy-latest.tgz && rm *.tgz && mv * stampy  
WORKDIR stampy  
RUN make  
ENV PATH /opt/stampy/stampy/:$PATH  

