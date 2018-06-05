FROM continuumio/miniconda  
  
LABEL maintainer "Luca Novara <luca.novara@ircc.it>"  
  
ENV BWA_VERSION "0.7.17"  
ENV EAUTILS_VERSION "1.04.807"  
ENV HTSEQ_VERSION "0.9.1"  
ENV MAPSPLICE_VERSION "2.2.0"  
ENV NUMPY_VERSION "1.14.3"  
ENV PICARD_VERSION "2.17.11"  
ENV RSEM_VERSION "1.3.0"  
ENV SAMTOOLS_VERSION "1.3"  
ENV UBU_VERSION "1.2b"  
RUN conda config --add channels defaults && \  
conda config --add channels conda-forge && \  
conda config --add channels bioconda && \  
conda update conda && \  
conda install mapsplice=${MAPSPLICE_VERSION} && \  
# Otherwise samtools gets overwritten with 0.1.19 version  
conda install bats \  
bedtools \  
bwa=${BWA_VERSION} \  
htseq=${HTSEQ_VERSION} \  
make \  
numpy=${NUMPY_VERSION} \  
picard=${PICARD_VERSION} \  
rsem=${RSEM_VERSION} \  
samtools=${SAMTOOLS_VERSION} && \  
git clone https://github.com/zstephens/neat-genreads.git /tmp/neat-genreads &&
\  
chmod 755 /tmp/neat-genreads/genReads.py && \  
ln -s /tmp/neat-genreads/genReads.py /usr/local/bin && \  
rm -rf /opt/conda/pkgs/* /tmp/neat-genreads/.git  
  
ADD https://github.com/ExpressionAnalysis/ea-
utils/archive/${EAUTILS_VERSION}.tar.gz /tmp/  
  
RUN tar xzf /tmp/${EAUTILS_VERSION}.tar.gz -C /tmp/ && \  
cp -a /tmp/ea-utils-${EAUTILS_VERSION}/clipper/gtf2bed /usr/local/bin && \  
rm -rf /tmp/*  
  
ADD
https://github.com/mozack/ubu/releases/download/v1.2b/ubu-${UBU_VERSION}-SNAPSHOT-
jar-with-dependencies.jar /tools/ubu-${UBU_VERSION}/  
  
COPY ./utils/build_rsem_gtf.py /usr/local/bin  

