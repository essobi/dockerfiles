FROM continuumio/miniconda:4.4.10  
  
ENV CONDA_DIR=/opt/conda  
ENV PATH=${CONDA_DIR}/bin:${PATH}  
  
########################################  
# Add mount points  
########################################  
  
RUN mkdir /scratch /work /home1 /gpfs /corral-repl /corral-tacc /data  
  
########################################  
# Install ipyrad  
########################################  
  
RUN conda install -c ipyrad ipyrad  

