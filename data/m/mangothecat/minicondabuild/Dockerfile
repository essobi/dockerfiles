FROM continuumio/miniconda3:latest  
  
RUN conda update -y conda \  
&& conda install nomkl \  
&& conda install conda-build \  
&& conda clean \--all  

