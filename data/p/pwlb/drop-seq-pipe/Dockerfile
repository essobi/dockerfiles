FROM pwlb/rna-seq-pipeline-base:v0.1.0  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet
https://repo.continuum.io/miniconda/Miniconda3-4.3.27-Linux-x86_64.sh -O
~/miniconda.sh && \  
/bin/bash ~/miniconda.sh -b -p /opt/conda && \  
rm ~/miniconda.sh  
ENV PATH /opt/conda/bin:$PATH  
  
# this step takes unberably long due to a bug in conda  
RUN git clone https://github.com/Hoohm/dropSeqPipe.git && \  
cd dropSeqPipe && \  
git reset origin 161572831c748f45504c4e21c117d6aca554a5b6 && \  
cp drop-seq-tools-wrapper.sh $DROPSEQPATH && \  
conda env create -v --name dropSeqPipe --file environment.yaml  
  
COPY ./binaries/gtfToGenePred /usr/bin/gtfToGenePred  
  
ENV NUMCELLS 500  
ENV NCORES 1  
ENV TARGETS all  
COPY config/config.yaml /config/  
COPY scripts /scripts  
  
ENTRYPOINT ["bash", "/scripts/run-all.sh"]  
CMD [""]  

