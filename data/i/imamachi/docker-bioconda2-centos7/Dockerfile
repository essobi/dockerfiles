# Base image  
FROM centos:centos7  
  
# Metadata  
LABEL maintainer="Naoto Imamachi <naoto.imamachi@gmail.com>"  
LABEL base.image="Centos7"  
LABEL version="1"  
LABEL software="Centos7+Miniconda2+Bioconda base Image"  
LABEL software.version="01102018"  
LABEL tags="NGS,Genomics,Transcriptomics,Bioconda,Centos7"  
  
# Install Miniconda2 & Bioconda  
RUN yum -y update \  
&& yum -y install curl bzip2 \  
&& curl -sSL https://repo.continuum.io/miniconda/Miniconda2-latest-
Linux-x86_64.sh -o /tmp/miniconda.sh \  
&& bash /tmp/miniconda.sh -bfp /usr/local/ \  
&& rm -rf /tmp/miniconda.sh \  
&& conda install -y python=2 \  
&& conda update conda \  
&& conda config --add channels r \  
&& conda config --add channels defaults \  
&& conda config --add channels conda-forge \  
&& conda config --add channels bioconda \  
&& conda clean --all --yes \  
&& rpm -e --nodeps bzip2 \  
&& yum -y autoremove \  
&& yum clean all  

