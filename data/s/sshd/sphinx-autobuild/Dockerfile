FROM python:3.6  
MAINTAINER shuns  
  
RUN set -x && \  
pip install 'Sphinx == 1.5.3' \  
'sphinx-autobuild == 0.6.0' \  
'sphinx_rtd_theme == 0.2.4' \  
'recommonmark == 0.4.0'  
  
ENV DOC_DIR=/document  
  
WORKDIR $DOC_DIR  

