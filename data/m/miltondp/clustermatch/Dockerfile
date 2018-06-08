FROM continuumio/miniconda3:4.4.10  
MAINTAINER Milton Pividori <mpividori@sinc.unl.edu.ar>  
  
COPY environment.yml /  
COPY matplotlibrc_agg /  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
fortran-compiler \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN conda config --append channels conda-forge  
#RUN conda install -y --file /requirements.txt \  
RUN conda env update -n root --file /environment.yml \  
&& rm /environment.yml  
  
#RUN MPLFILE=$(python -c "import matplotlib;
exit(matplotlib.matplotlib_fname())" 2>&1) cp /matplotlibrc_agg $MPLFILE \  
#RUN mkdir $HOME/.matplotlib && cp /matplotlibrc_agg
$HOME/.matplotlib/matplotlibrc \  
RUN cp /matplotlibrc_agg /opt/conda/lib/python3.6/site-
packages/matplotlib/mpl-data/matplotlibrc \  
&& rm /matplotlibrc_agg  
  
RUN ln -s /opt/conda/bin/python /usr/local/bin/python  
  

