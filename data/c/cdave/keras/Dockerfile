from tensorflow/tensorflow:1.4.1-gpu-py3  
  
# The main point  
RUN pip install keras  
  
# Nice to haves  
RUN pip --no-cache-dir install \  
tqdm \  
keras-tqdm \  
seaborn \  
statsmodels \  
keras-tqdm\  
scikit-image  
  
## Configure Jupiter notebook extensions  
# Enable JS widgets  
RUN jupyter nbextension enable \--py --sys-prefix widgetsnbextension  
# Install contributed notebook extensions  
RUN pip install https://github.com/ipython-
contrib/jupyter_contrib_nbextensions/tarball/master && \  
jupyter contrib nbextension install --system && \  
jupyter nbextension enable collapsible_headings/main && \  
jupyter nbextension enable spellchecker/main  
# Install vim bindings  
RUN jupyter nbextension install https://github.com/lambdalisue/jupyter-vim-
binding/archive/master.tar.gz --system && \  
jupyter nbextension enable jupyter-vim-binding-master/vim_binding  
  

