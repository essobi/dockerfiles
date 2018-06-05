FROM ubuntu:16.04  
MAINTAINER felix11h.dev@gmail.com  
  
USER root  
  
# decided against fixed versions for these basic  
# basic packages as previous versions are often  
# not available making the build fail  
RUN apt-get -qy update  
RUN apt-get install -qy python python-dev python-pip git screen  
  
# some dependencis are needed for building  
# matplotlib in the next step  
RUN apt-get -qy build-dep python-matplotlib  
  
# fixed python package versions, this might help  
# in reproducing the computational environment  
# from scratch without Docker  
RUN pip install --upgrade pip==9.0.1  
RUN pip install numpy==1.14.1 scipy==1.0.0 matplotlib==1.5.0 sumatra==0.7.3 \  
gitpython==1.0.1 nose==1.3.7 ipython==5.5.0  
  
  
# current the method of installing graph_tool as  
# documented on website https://graph-tool.skewed.de/  
# installs graph_tool version 2.26  
RUN echo "deb http://downloads.skewed.de/apt/xenial xenial universe" | tee -a
/etc/apt/sources.list  
RUN echo "deb-src http://downloads.skewed.de/apt/xenial xenial universe" | tee
-a /etc/apt/sources.list  
  
RUN apt-key adv --keyserver pgp.skewed.de --recv-key 612DEFB798507F25  
RUN apt-get -qy update  
RUN apt-get install -qy python-graph-tool  
  
# latex is used for text in figures but the full install  
# is prohibitively large. I will only recommend the full  
# image for byte-identical reproduction  
RUN apt-get install -qy texlive-full  
  
RUN useradd -ms /bin/bash docker  
USER docker  

