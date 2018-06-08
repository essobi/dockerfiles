#
*****************************************************************************  
# Installs https://github.com/nilqed/fricas_jupyter  
# Build ..: docker build -t nilqed/fricas_jupyter .  
# Test ...: docker run -t -i nilqed/fricas_jupyter /bin/bash  
# Run ....: docker run -p 443:8888 -t -i nilqed/fricas_jupyter \  
# jupyter notebook --ip=*  
#
*****************************************************************************  
# $Id: Dockerfile 1 2015-10-23 02:52:02Z pagani $  
#
*****************************************************************************  
  
FROM nilqed/fricas  
  
MAINTAINER Kurt Pagani <nilqed@gmail.com>  
  
  
# =====  
# iSPAD  
# =====  
  
RUN cd /root && \  
git clone https://github.com/nilqed/fricas_jupyter.git && \  
cd ./fricas_jupyter && \  
./install.sh  
  
  
  
# =======  
# MathJax  
# =======  
  
RUN cd /usr/local/lib/python3.4/dist-packages/notebook/static/components && \  
rm -r MathJax && \  
git clone git://github.com/mathjax/MathJax.git MathJax  
# =====================  
# CodeMirror mode/lexer  
# =====================  
  
RUN cd /root/tmp  
  

