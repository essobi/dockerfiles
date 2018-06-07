FROM jupyter/r-notebook  
  
RUN conda config --add channels r  
RUN conda install --yes \  
'r-coda' \  
'r-digest' \  
'r-lubridate' && conda clean -yt  
  
RUN conda config --add channels jps2  
RUN conda install --yes \  
'r-ggplot2=2.0*' \  
'r-stanheaders' \  
'r-inline' \  
'r-viridis' && conda clean -yt  
  
RUN conda config --add channels rgrout  
RUN conda install --yes \  
'r-mvtnorm' && conda clean -yt  
  
RUN conda config --add channels asmeurer  
RUN conda install --yes \  
'r-rcpp' \  
'r-rcppeigen' \  
'r-matrix' \  
'r-bh' && conda clean -yt  
  
RUN conda config --add channels bioconda  
RUN conda install --yes \  
'r-matrixstats' && conda clean -yt  
  
RUN conda config --add channels mittner  
RUN conda install --yes \  
'r-loo' \  
'r-rstan' && conda clean -yt  
  
# Install R packages  
USER root  
COPY scripts/rpackages.R /home/jovyan/work/rpackages.R  
RUN chmod +x /home/jovyan/work/rpackages.R  
RUN Rscript /home/jovyan/work/rpackages.R \  
&& rm /home/jovyan/work/rpackages.R  
USER jovyan  

