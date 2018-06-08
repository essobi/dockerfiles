FROM vaiski/miniconda:latest  
  
MAINTAINER Eemil Väisänen <eemil.vaisanen@iki.fi>  
  
ENV USER=scientist GROUP=scientist HOME=/home/scientist  
RUN adduser -s /bin/bash -D -s /bin/bash $USER \  
&& mkdir $HOME/workspace \  
&& chown -R $USER:$GROUP $HOME  
  
RUN conda install -y jupyter  
  
RUN conda install -y \  
numpy \  
scipy \  
matplotlib \  
pandas \  
sympy \  
numexpr \  
bokeh \  
seaborn \  
statsmodels \  
patsy \  
scikit-learn \  
scikit-image \  
nltk \  
lxml \  
beautifulsoup4  
  
RUN conda install -y -c conda-forge \  
hdf5 \  
h5py \  
folium \  
tensorflow \  
Theano \  
altair \  
keras  
  
# RUN mkdir -p $HOME/.jupyter/custom \  
# && curl https://raw.githubusercontent.com/dunovank/jupyter-
themes/master/jupyterthemes/styles/compiled/grade3.css >
$HOME/.jupyter/custom/custom.css  
VOLUME ["$HOME/workspace"]  
EXPOSE 8888  
USER $USER  
WORKDIR $HOME/workspace  
  
RUN mkdir $HOME/.jupyter \  
&& echo "c.NotebookApp.ip = '*'" > $HOME/.jupyter/jupyter_notebook_config.py \  
&& echo "c.NotebookApp.open_browser = False" >>
$HOME/.jupyter/jupyter_notebook_config.py  
  
ENTRYPOINT ["/sbin/tini", "--"]  
CMD ["jupyter", "notebook"]  

