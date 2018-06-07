#################################################################  
# Dockerfile  
#  
# Version: 2  
# Software: Variant Effect Predictor  
# Software Version: 88  
# Description: variant annotation tool  
# Website: http://www.ensembl.org/info/docs/tools/vep/index.html  
# Tags: NGS  
# Provides: VEP 88  
# Base Image: willmclaren/ensembl-vep  
# Build Cmd: docker build .  
# Pull Cmd: docker pull personalizedoncology/vep_plugins_containerized  
# Run Cmd: docker run --rm -it personalizedoncology/vep_plugins_containerized
vep <options>  
# Extra: Includes plugins for LoF prediction and ExAC allele frequencies  
# Extra: as well as Ensembl and RefSeq caches  
# Extra Based on cschaerfe/vep86_plugins  
#################################################################  
  
# Base image  
FROM willmclaren/ensembl-vep:latest  
  
MAINTAINER Julian Heinrich  
  
# Install cache, fasta, and all plugins  
WORKDIR $HOME/src/ensembl-vep  
RUN ./INSTALL.pl -a cfp -s homo_sapiens -y GRCh37 -g all  
  
# Install other dependencies  
USER root  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y --no-install-recommends \  
samtools  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /home/vep  
USER vep  
RUN wget https://github.com/konradjk/loftee/archive/master.zip && \  
wget https://s3.amazonaws.com/bcbio_nextgen/human_ancestor.fa.gz && \  
wget https://s3.amazonaws.com/bcbio_nextgen/human_ancestor.fa.gz.fai && \  
wget https://s3.amazonaws.com/bcbio_nextgen/human_ancestor.fa.gz.gzi && \  
wget
https://raw.githubusercontent.com/Ensembl/VEP_plugins/release/88/LoFtool_scores.txt
&& \  
unzip master.zip && \  
rm master.zip  
  
USER root  
ENV PERL5LIB /home/vep/loftee-master/:$PERL5LIB  
  
# Clean up APT when done.  
RUN apt-get clean  
  
USER vep  

