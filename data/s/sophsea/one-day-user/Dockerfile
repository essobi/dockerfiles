FROM jupyter/tensorflow-notebook  
  
LABEL maintainer="Sophie Searcy <s@soph.info>"  
  
RUN conda install --yes \  
'yapf' \  
'autopep8' \  
'ipywidgets' \  
'jupyter_contrib_nbextensions' && \  
conda clean -tipsy && \  
fix-permissions $CONDA_DIR  
  
RUN pip install git+https://github.com/data-8/gitautosync  
  
RUN jupyter contrib nbextension install --user  
RUN jupyter nbextension enable \--py widgetsnbextension  
RUN jupyter nbextension enable python-markdown/main  
RUN jupyter nbextension enable code_prettify/code_prettify  
RUN jupyter nbextension enable varInspector/main  
RUN jupyter nbextension enable execute_time/ExecuteTime  
RUN jupyter nbextension enable toggle_all_line_numbers/main  
  
# Make sure the contents of our repo are in ${HOME}  
USER root  
COPY . /srv/app/src  
RUN chown -R ${NB_UID} /srv/app/src  
USER ${NB_USER}  

