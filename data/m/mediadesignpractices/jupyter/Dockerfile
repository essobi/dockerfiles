FROM mediadesignpractices/python:python3-latest  
LABEL organization "Media Design Practices"  
LABEL maintainer "mediadesignpractices"  
LABEL contributor "unsalted"  
  
USER root  
ENV NOTEBOOK_DIR $HOME/notebooks  
  
RUN apt-get update && apt-get install -yq --no-install-recommends \  
libsm6 \  
pandoc \  
libxrender1 \  
inkscape \  
libav-tools \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# install IPython kernel
http://ipython.readthedocs.io/en/stable/install/kernel_install.html  
RUN python2 -m pip install ipykernel \  
&& python2 -m ipykernel install --user  
  
# useful basics  
RUN pip3 --no-cache-dir install \  
jupyter \  
sklearn \  
ipywidgets \  
&& \  
python -m ipykernel.kernelspec  
  
# Set up our notebook config.  
COPY jupyter_notebook_config.py $HOME/.jupyter/  
  
# IPython  
EXPOSE 8888  
RUN mkdir -p $NOTEBOOK_DIR \  
&& chown $NB_USER $NOTEBOOK_DIR \  
&& ln -s $NOTEBOOK_DIR $DATA_DIR/notebooks  
  
COPY example.ipynb $NOTEBOOK_DIR  
  
USER $NB_USER  
WORKDIR $NOTEBOOK_DIR  
  
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0"]

