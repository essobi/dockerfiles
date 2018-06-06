FROM mcfonsecalab/python36_bio  
  
MAINTAINER Pedro Barbosa <pedro.barbosa@medicina.ulisboa.pt>  
  
RUN apt-get update  
RUN conda update -n base conda  
  
LABEL mosdepth="v0.2.2"  
LABEL goleft="v0.1.18"  
LABEL deeptools="v3.0.1"  
RUN conda install -c bioconda mosdepth goleft deeptools  
  
RUN apt-get autoclean -y  

