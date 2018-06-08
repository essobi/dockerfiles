# Docker file for building the base system user image  
FROM ritjupyter/base-systemuser  
MAINTAINER Joshua Milas <jgm6496@rit.edu>  
  
USER root  
  
# Install the spell check plugin  
RUN cd /tmp && \  
git clone https://github.com/Calysto/notebook-extensions.git && \  
cd notebook-extensions && \  
jupyter nbextension install calysto --system && \  
jupyter nbextension enable calysto/spell-check/main --system && \  
rm -rf /home/jovyan && \  
rm -rf /tmp/*  
  
# Add the KGCOE report template and files  
# This must be changed if there is an update to python  
# `ls -d /opt/conda/lib/python*` will get you the correct location  
COPY kgcoe_jupyter_template.tplx /opt/conda/lib/python3.5/site-
packages/nbconvert/templates/latex/article.tplx  
COPY KGCOEReport.cls /usr/local/share/texmf/tex/latex/KGCOEReport.cls  
RUN texhash /usr/local/share/texmf  

