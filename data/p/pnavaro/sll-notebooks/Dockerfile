FROM jupyter/scipy-notebook  
  
MAINTAINER Pierre Navaro <pierre.navaro@univ-rennes1.fr>  
  
USER root  
COPY . ${HOME}  
RUN chown -R ${NB_USER} ${HOME}  
  
RUN apt-get update && apt-get -yq dist-upgrade \  
&& apt-get install -yq --no-install-recommends \  
cmake gfortran libfftw3-dev libopenblas-dev \  
libopenmpi-dev openmpi-bin libhdf5-openmpi-dev \  
&& apt-get clean && apt-get purge \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN conda install --quiet --yes -c conda-forge pandas seaborn yt && \  
conda install --quiet --yes -c rlehe openpmd_viewer tqdm && \  
conda install --quiet --yes -c spectraldns h5py-parallel && \  
conda clean -tipsy && \  
fix-permissions $CONDA_DIR  
  
RUN wget --no-check-certificate http://selalib.gforge.inria.fr/binary.tgz \  
&& tar -zxf binary.tgz && rm binary.tgz && fix-permissions $HOME/selalib  
  
USER ${NB_USER}  
  
# Configure environment  
ENV PATH=$HOME/selalib/bin:$PATH  

