# Base image  
FROM debian:9  
# Metadata  
LABEL maintainer="Naoto Imamachi <naoto.imamachi@gmail.com>"  
LABEL base.image="debian9"  
LABEL version="1"  
LABEL software="debian9+Miniconda2+Bioconda base Image"  
LABEL software.version="01112018"  
LABEL tags="NGS,Genomics,Transcriptomics,Bioconda,debian9"  
  
# Install Miniconda2 & Bioconda  
RUN apt-get -qq update && apt-get -qq -y install curl bzip2 \  
&& curl -sSL https://repo.continuum.io/miniconda/Miniconda2-latest-
Linux-x86_64.sh -o /tmp/miniconda.sh \  
&& bash /tmp/miniconda.sh -bfp /usr/local \  
&& rm -rf /tmp/miniconda.sh \  
&& conda install -y python=2 \  
&& conda update conda \  
&& conda config --add channels r \  
&& conda config --add channels defaults \  
&& conda config --add channels conda-forge \  
&& conda config --add channels bioconda \  
&& apt-get -qq -y remove curl bzip2 \  
&& apt-get -qq -y autoremove \  
&& apt-get autoclean \  
&& rm -rf /var/lib/apt/lists/* /var/log/dpkg.log \  
&& conda clean --all --yes  
  
ENV PATH /opt/conda/bin:$PATH  

