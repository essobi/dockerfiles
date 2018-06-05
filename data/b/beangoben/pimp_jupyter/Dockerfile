FROM jupyter/scipy-notebook  
  
# make bash default shell  
USER root  
RUN ln -snf /bin/bash /bin/sh  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends jq imagemagick \  
librsvg2-bin libcairo2-dev libgd-dev libffi-dev && \  
apt-get clean && \  
apt-get autoclean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN conda install -y -q -c conda-forge conda-build xlrd xlwt nb_conda_kernels
&&\  
conda update -y -q pip notebook numpy scipy matplotlib seaborn ipython && \  
conda clean --all  
RUN pip install --no-cache autopep8  
#jupyter theme selector  
RUN mkdir /opt/conda/share/jupyter/nbextensions/jupyter_themes &&\  
wget
https://raw.githubusercontent.com/merqurio/jupyter_themes/master/theme_selector.js
&&\  
mv theme_selector.js /opt/conda/share/jupyter/nbextensions/jupyter_themes &&\  
jupyter nbextension enable jupyter_themes/theme_selector  
  
# live reveal  
RUN conda install -y -q -c damianavila82 rise && conda clean --all  
  
# jupyter notebook extensions  
RUN pip install --upgrade --no-cache --ignore-installed
https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tarball/master
&&\  
jupyter nbextensions_configurator enable \--system && \  
jupyter contrib nbextension install --system  
# update conda  
RUN chown -R $NB_USER /home/$NB_USER  
USER $NB_USER  
# load default extension options  
COPY nbextensions_default.json /home/$NB_USER/.jupyter/nbconfig  
RUN cd /home/$NB_USER/.jupyter/nbconfig && jq -s add notebook.json
nbextensions_default.json > new.json && mv new.json notebook.json  
#jupyter css  
RUN mkdir -p /home/$NB_USER/.jupyter/custom  
COPY custom /home/$NB_USER/.jupyter/custom  
# remove token  
RUN echo "c.NotebookApp.token=''" >> ~/.jupyter/jupyter_notebook_config.py  

