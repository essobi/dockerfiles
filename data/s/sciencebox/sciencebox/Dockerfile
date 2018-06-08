FROM sciencebox/sciencebox:latest  
MAINTAINER Fabiano Menegidio <fabiano.menegidio@biology.bio.br>  
  
USER root  
  
ENV CONDA_DIR /opt/conda  
ENV PATH $CONDA_DIR/bin:$PATH  
  
# Configure Miniconda  
ENV MINICONDA_VER latest  
ENV MINICONDA Miniconda2-$MINICONDA_VER-Linux-x86_64.sh  
ENV MINICONDA_URL https://repo.continuum.io/miniconda/$MINICONDA  
  
RUN mkdir -p /opt/conda && \  
chown sciencebox /opt/conda  
  
USER sciencebox  
  
# Install conda as sciencebox  
RUN cd /tmp && \  
mkdir -p $CONDA_DIR && \  
curl -L $MINICONDA_URL -o miniconda.sh && \  
/bin/bash miniconda.sh -f -b -p $CONDA_DIR && \  
rm miniconda.sh && \  
$CONDA_DIR/bin/conda config --add channels r && \  
$CONDA_DIR/bin/conda config --add channels bioconda && \  
$CONDA_DIR/bin/conda clean -tipsy  

