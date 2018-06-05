# Copyright (c) Jupyter Development Team.  
# Distributed under the terms of the Modified BSD License.  
#  
# heavily modified by Charless Fowlkes <fowlkes@ics.uci.edu> (c) 2017  
#  
# Pin to version of notebook image that includes start-singleuser.sh script  
FROM fowlkes/bigdipa_notebook_base:latest  
  
RUN apt-get update  
  
# openslide  
RUN apt-get install -y --no-install-recommends openslide-tools  
  
# ASAP library  
RUN apt-get install -y --no-install-recommends libjasper1 libpugixml1v5
libboost-thread1.58.0 libboost-regex1.58.0 libdcmtk2-dev  
  
# pyopencl  
RUN apt-get install -y --no-install-recommends python3-pyopencl  
  
# remove tex live to save 1GB  
# RUN apt-get remove --autoremove -y texlive-base inkscape  
# cleanup apt cruft  
RUN rm -rf /var/lib/apt/lists/*  
  
# script used to make sure conda permissions are good  
ADD fix-permissions /usr/local/bin/fix-permissions  
RUN chmod a+x /usr/local/bin/fix-permissions  
  
########################################################################################  
# install anaconda/python components as jovyan  
#  
USER jovyan  
  
# TODO: set version requirements here  
# ML and graph labs  
RUN conda update --yes conda && \  
conda install --yes tensorflow-gpu keras networkx pandas python-graphviz && \  
conda clean -tipsy  
  
# calcium imaging lab  
RUN conda install --yes future ipyparallel h5py spyder nose bokeh && \  
conda install --yes -c menpo opencv3 && \  
conda clean -tipsy  
  
RUN fix-permissions $CONDA_DIR  
  
# avoid conda version of pyopencl  
# peakutils & tqdm are for graph lab  
RUN pip install pyopencl allensdk openslide-python peakutils tqdm  
  
# don't run conda clean after this, it removes cuda80  
RUN conda install -c soumith --yes pytorch torchvision cuda80  
  
########################################################################################  
# finally install custom startup script and notebook_image  
#  
USER root  
  
COPY ./start-authless-notebook.sh /usr/local/bin/start-authless-notebook.sh  
RUN chmod a+rx /usr/local/bin/start-authless-notebook.sh  
  
COPY ./start-passwd-notebook.sh /usr/local/bin/start-passwd-notebook.sh  
RUN chmod a+rx /usr/local/bin/start-passwd-notebook.sh  
  
COPY docker-entrypoint.sh /srv/docker-entrypoint.sh  
RUN chmod a+rx /srv/docker-entrypoint.sh  
RUN mkdir -p /home/bigdipa/  
ADD notebook_image.tar.gz /home/bigdipa/  
RUN chown -R jovyan /home/bigdipa  
  
########################################################################################  
ENTRYPOINT ["tini", "--", "/srv/docker-entrypoint.sh"]  
CMD ["start-singleuser.sh"]  
USER jovyan  

