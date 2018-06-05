FROM skippa/base  
MAINTAINER mike.aizatsky@gmail.com  
  
# Add Tini  
ENV TINI_VERSION v0.13.2  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/usr/bin/tini  
RUN chmod +x /usr/bin/tini  
ENTRYPOINT ["/usr/bin/tini", "--"]  
  
# Add Anaconda  
ENV ANACONDA_VERSION "4.2.0"  
ENV CONDA_PATH "/opt/conda"  
ENV PATH "$CONDA_PATH/bin:$PATH"  
RUN apt-get update && apt-get upgrade -y && apt-get install -y wget bzip2  
  
RUN wget --quiet
https://repo.continuum.io/archive/Anaconda3-$ANACONDA_VERSION-Linux-x86_64.sh
-O anaconda.sh && \  
/bin/bash anaconda.sh -b -p $CONDA_PATH && \  
rm anaconda.sh  
  
RUN conda update anaconda -y  
ENV JUPYTER "/opt/conda/bin/jupyter"  
CMD ["jupyter", "notebook", "--no-browser", "--ip='*'", "--port=8888", "--
notebook-dir=/workspace"]  

