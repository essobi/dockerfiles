# Testing integration with Docker hub  
FROM jupyter/scipy-notebook  
  
USER $NB_USER  
RUN conda install --quiet --yes anaconda-client anaconda mkl-rt boto3 pymongo
biopython sqlalchemy rdflib psycopg2 nltk pytables lxml autopep8 yapf nodejs
pandas openjdk maven pytest mysql-connector-python elasticsearch ipyparallel
pyld  
RUN conda install --quiet --yes --channel conda-forge widgetsnbextension
jupyterlab ipywidgets beakerx  
RUN conda install --quiet --yes --channel https://conda.anaconda.org/openbabel
openbabel  
RUN conda install --quiet --yes --channel https://conda.anaconda.org/bioconda
rdflib-jsonld  
#RUN pip install matplotlib_venn  
#RUN pip install xmljson  
RUN conda update --all --quiet --yes  
#RUN pip install -U beakerx # Needed while we wait for conda to update the
package  
RUN beakerx install  
ENV TINI_VERSION v0.6.0  
USER root  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/usr/bin/tini  
RUN chmod +x /usr/bin/tini  
RUN ipcluster nbextension enable  
USER $NB_USER  
RUN pip install jupyter_contrib_nbextensions  
RUN jupyter contrib nbextension install --user  
RUN jupyter nbextensions_configurator enable \--user  
RUN bash -c "jupyter-nbextension enable codefolding/main ; jupyter-nbextension
enable code_prettify/code_pretiffy ; jupyter-nbextension enable
execute_time/ExecuteTime ; jupyter-nbextension enable gist_it/main ; jupyter-
nbextension enable snippets/main ; jupyter-nbextension enable
snippets_menu/main ; jupyter-nbextension enable autopep8 ; jupyter-nbextension
enable codefolding/edit ; jupyter-nbextension enable collapsible_headings/main
; jupyter-nbextension enable splitcell/splitcell ; jupyter-nbextension enable
toc2/main"  
RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager  
ENTRYPOINT ["/usr/bin/tini", "--"]  
#CMD bash -c "jupyter lab --no-browser --port=8888 --NotebookApp.token="  
CMD bash -c "jupyter lab --no-browser --port=8888"  

