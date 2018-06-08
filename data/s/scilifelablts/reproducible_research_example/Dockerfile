FROM rocker/hadleyverse  
  
WORKDIR /home  
ENV LC_ALL C  
SHELL ["/bin/bash", "-c"]  
  
RUN apt-get update && apt-get install bzip2  
  
RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh  
RUN bash Miniconda3-latest-Linux-x86_64.sh -bf && rm Miniconda3-latest-
Linux-x86_64.sh  
ENV PATH="/root/miniconda3/bin:${PATH}"  
RUN git clone http://bitbucket.org/scilifelab-
lts/reproducible_research_example.git  
RUN conda config --add channels bioconda  
RUN conda create --name my_conda_env snakemake fastqc  
  
CMD source activate my_conda_env;cd reproducible_research_example;snakemake
results/SRR068303.pdf  

