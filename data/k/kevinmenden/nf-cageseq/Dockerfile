FROM ubuntu  
  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
RUN apt-get update --fix-missing && \  
apt-get install -y wget bzip2 ca-certificates curl git && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet
https://repo.continuum.io/miniconda/Miniconda3-4.4.10-Linux-x86_64.sh -O
~/miniconda.sh && \  
/bin/bash ~/miniconda.sh -b -p /opt/conda && \  
rm ~/miniconda.sh && \  
/opt/conda/bin/conda clean -tipsy  
  
ENV TINI_VERSION v0.16.1  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/usr/bin/tini  
RUN chmod +x /usr/bin/tini  
  
ENV PATH $PATH:/opt/conda/bin  
ENTRYPOINT [ "/usr/bin/tini", "--" ]  
CMD [ "/bin/bash" ]  
  
COPY environment.yml /  
RUN conda env create -f /environment.yml  
ENV PATH $PATH:/opt/conda/envs/nf-cageseq/bin  
  
# Install container-wide requrements gcc, pip, zlib, libssl, make, libncurses,
fortran77, g++, R  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
g++ \  
gcc \  
gfortran \  
libbz2-dev \  
libcurl4-openssl-dev \  
libgsl-dev \  
libgsl2 \  
liblzma-dev \  
libncurses5-dev \  
libpcre3-dev \  
libreadline-dev \  
libssl-dev \  
make \  
python-dev \  
zlib1g-dev \  
liblzo2-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install R  
RUN curl -fsSL https://cran.r-project.org/src/base/R-3/R-3.4.2.tar.gz -o
/opt/R-3.4.2.tar.gz && \  
tar xvzf /opt/R-3.4.2.tar.gz -C /opt/ && \  
cd /opt/R-3.4.2 && \  
./configure --with-x=no && \  
make && \  
make install && \  
rm /opt/R-3.4.2.tar.gz  
  
# Install some necessary libraries (move to top at some point)  
RUN apt-get update && apt-get install -y libxml2 libmariadb-client-lgpl-dev  
  
# Install custom R packages  
RUN echo 'source("https://bioconductor.org/biocLite.R")' > /opt/packages.r &&
\  
echo 'biocLite()' >> /opt/packages.r && \  
echo 'biocLite(c("CAGEr", "BSgenome.Hsapiens.UCSC.hg38",
"BSgenome.Hsapiens.NCBI.GRCh38"))' >> /opt/packages.r && \  
Rscript /opt/packages.r && \  
mkdir -p /usr/local/lib/R/site-library

