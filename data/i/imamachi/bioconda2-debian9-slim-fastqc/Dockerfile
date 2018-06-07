# Base image  
FROM imamachi/docker-bioconda2-debian9-slim:latest  
  
# Metadata  
LABEL maintainer="Naoto Imamachi <naoto.imamachi@gmail.com>"  
LABEL base.image="debian9-slim"  
LABEL version="0.11.6"  
LABEL software="fastqc_0.11.6"  
LABEL software.version="20180131"  
LABEL tags="NGS,Genomics,Transcriptomics,Bioconda,debian9-slim,fastqc"  
  
# Install a software  
# Dejavu fonts are not included with default::openjdk(fastqc recipe).  
# They are already included with conda-forge::openjdk.  
# https://github.com/conda-forge/staged-recipes/issues/3164  
RUN conda install boto3 awscli \  
&& conda install fastqc=0.11.6 \  
&& conda install -c conda-forge openjdk \  
&& conda clean --all --yes  

