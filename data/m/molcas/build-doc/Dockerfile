FROM phusion/baseimage  
  
# Update system and install  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y --no-install-recommends gcc gfortran make cmake latexmk
latex2html && \  
apt-get install -y --no-install-recommends python-pip python-sphinx && \  
apt-get install -y --no-install-recommends git && \  
apt-get clean && \  
pip install --upgrade pip setuptools && \  
pip install --upgrade sphinxcontrib-bibtex  

