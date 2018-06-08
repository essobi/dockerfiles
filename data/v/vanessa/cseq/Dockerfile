#########################################  
# SciF Base  
#  
# docker build -f Dockerfile.scif -t vanessa/cseq .  
# docker run vanessa/cseq  
#  
#########################################  
  
FROM continuumio/miniconda3  
  
#########################################  
# SciF Install  
  
ADD . /  
RUN apt-get update && apt-get install -y git wget build-essential \  
gcc-multilib apt-utils \  
zlib1g-dev samtools  
  
RUN /opt/conda/bin/conda install -y numpy scipy && \  
/opt/conda/bin/pip install biopython  
  
RUN git clone https://github.com/lh3/seqtk.git build && \  
cd build && git checkout v1.2 && make && mv seqtk /usr/local/bin  
  
RUN /opt/conda/bin/pip install scif  
RUN chmod u+x /entrypoint.sh  
  
# Install the filesystem from the recipe  
RUN scif install /carrierseq.scif  
  
# Labels  
LABEL bioRxiv-doi https://doi.org/10.1101/175281  
  
# SciF Entrypoint  
  
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]  

