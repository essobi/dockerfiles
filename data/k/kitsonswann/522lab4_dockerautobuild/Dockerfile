# Docker file for ubuntu-522lab4  
# Kitson Swann, Oct 23, 2016  
# use rocker/hadleyverse as base image  
FROM rocker/hadleyverse:latest  
  
# get OS updates and install build tools  
RUN apt-get update  
RUN apt-get install -y build-essential  
  
# install graphviz  
RUN apt-get install -y graphviz  
  
# install git  
RUN apt-get install -y wget  
RUN apt-get install -y make git  
  
# clone, build makefile2graph,  
# then copy key makefile2graph files to usr/bin so they will be in $PATH  
RUN git clone https://github.com/lindenb/makefile2graph.git  
  
RUN make -C makefile2graph/.  
  
RUN cp makefile2graph/makefile2graph usr/bin  
RUN cp makefile2graph/make2graph usr/bin  
  
# install Lab 4 dependancies  
# install ezknitr  
RUN Rscript -e 'install.packages("ezknitr")'  

