# Copyright (c) Jupyter Development Team.  
# Distributed under the terms of the Modified BSD License.  
FROM jupyter/datascience-notebook  
#DISCLAIMER: ~6.07GB starting (ubuntu 16.04 + jupyter stacks)  
# eventually will be better to trim down with smaller base  
# though, right now (storagecost << human time)  
  
#last checked: 9.14GB  
#forked to version cytometry workflows under "cytometry" branch  
LABEL maintainer="jfx319 <jfx319@virginia.edu>"  
  
USER root  
  
#switch to bash  
#https://docs.docker.com/engine/reference/builder/#shell  
SHELL ["/bin/bash", "-c"]  
  
# pre-reqs for below, many for R (swig for cytoflow)  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
fonts-dejavu \  
tzdata \  
gfortran \  
gcc \  
&& apt-get install -y swig \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
USER $NB_UID  
  
# install Seurat (on R 3.4.1 and install java)  
RUN Rscript <(echo "install.packages('Seurat',
repos='http://cran.us.r-project.org', clean=TRUE)") \  
&& rm -rf /tmp/* \  
&& fix-permissions $CONDA_DIR \  
&& fix-permissions /home/$NB_USER  
  
#install python flowcytometrytools from github  
#but why is it not copying the gui template files?  
#temporary workaround to just download those two directly  
#also downgrade tornado for compatibility  
RUN pip install --quiet --no-cache-dir
git+git://github.com/eyurtsev/FlowCytometryTools \  
&& wget -O /opt/conda/lib/python3.6/site-
packages/FlowCytometryTools/gui/webagg_backend/app_template.html \  
https://raw.githubusercontent.com/eyurtsev/FlowCytometryTools/master/FlowCytometryTools/gui/webagg_backend/app_template.html
\  
&& wget -O /opt/conda/lib/python3.6/site-
packages/FlowCytometryTools/gui/wx_backend/wx-glade-wireframe-template.wxg \  
https://raw.githubusercontent.com/eyurtsev/FlowCytometryTools/master/FlowCytometryTools/gui/wx_backend/wx-
glade-wireframe-template.wxg \  
&& conda install -y tornado=4.5.3 \  
&& rm -rf /tmp/* \  
&& fix-permissions $CONDA_DIR \  
&& fix-permissions /home/$NB_USER  
  
# Install R flowCore, flowsom and companion plotting  
# https://bioconductor.org/help/course-materials/2010/BioC2010/seqGating.pdf  
RUN conda install --quiet --yes -c bioconda \  
bioconductor-flowcore \  
bioconductor-flowviz \  
bioconductor-ggcyto \  
bioconductor-flowsom && \  
conda clean -tipsy && \  
fix-permissions $CONDA_DIR && \  
fix-permissions /home/$NB_USER  
  
#install cytoflow  
# this layer is under development and may be buggy  
# http://cytoflow.readthedocs.io/en/stable/INSTALL.html  
RUN pip install --quiet --no-cache-dir Sphinx \  
&& pip install --quiet --no-cache-dir cytoflow \  
&& rm -rf /tmp/* \  
&& fix-permissions $CONDA_DIR \  
&& fix-permissions /home/$NB_USER  
  
### EXPANDING SECTION  
# these developments make many of the previous cytometry-specific interactive
tools somewhat obsolete  
###  
# evolving tools in the jupyter ecosystem:  
# jupyterlab, dashboards, ipywidgets, holoviews/bokeh vs dash/plotly  
# https://www.youtube.com/watch?v=6Pzg-UY1VDg  
# beta extensions for a beta platform... obviously may break  
# https://blog.jupyter.org/jupyterlab-is-ready-for-users-5a6f039b8906  
# https://github.com/twosigma/beakerx/tree/master/doc/python  
# https://github.com/quantopian/qgrid  
# https://github.com/bloomberg/bqplot  
# https://jupyter-dashboards-layout.readthedocs.io/en/latest/  
# http://jupyter.org/widgets  
# https://github.com/maartenbreddels/ipyvolume  
# https://github.com/vispy/vispy  
# https://github.com/RaRe-Technologies/gensim  
# -c conda-forge -c ioam geoviews  
# ipyleaflet  
# nglview -c bioconda  
# toyplot  
# vispy -c conda-forge (gpu, opengl)  
# pythreejs  
# mpld3 -c conda-forge  
# pyd3 -c conda-forge  
# ipyvolume -c conda-forge  
# gensim -c conda-forge  
# jupyterthemes -c conda-forge  
# altair -c creditx vega3 \  
# iris-agent (too early right now, but look forward to future)  
# dask extensions: https://anaconda.org/search?q=dask  
# turning off jupyterlabextension for now until compatibilities are fixed:  
# && jupyter labextension install @jupyter-widgets/jupyterlab-manager \  
RUN conda install -y -c bokeh \  
bokeh \  
datashader \  
&& conda install -y -c conda-forge \  
pandas \  
matplotlib \  
notebook \  
ipywidgets jupyter_dashboards \  
jupyterlab \  
pyinstaller \  
beakerx \  
bqplot \  
qgrid \  
holoviews \  
dask \  
numpy h5py Pillow scipy toolz pytables snakeviz distributed \  
&& rm -rf /tmp/* \  
&& fix-permissions $CONDA_DIR \  
&& fix-permissions /home/$NB_USER  
  
  
### Some ML developments & python based scRNAseq  
# note to self: kaggle kernels and google colab has jupyter-esque free compute
notebooks (incl. gpu)  
RUN conda install -y -c conda-forge hdbscan \  
&& conda install -y seaborn scikit-learn statsmodels numba \  
&& pip install --quiet --no-cache-dir umap-learn anndata scanpy \  
&& conda install -y -c conda-forge python-igraph \  
&& conda install -y -c vtraag louvain \  
&& rm -rf /tmp/* \  
&& fix-permissions $CONDA_DIR \  
&& fix-permissions /home/$NB_USER  
  
###  
# Free online environments may even make versioning my own container obsolete
one day...  
###  
#https://annefou.github.io/jupyter_dashboards/index.html  
# mybinder.org  
# https://medium.com/@mbostock/a-better-way-to-code-2b1d2876a3a0  

