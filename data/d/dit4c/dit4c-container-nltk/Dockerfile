FROM dit4c/dit4c-container-base:debian  
MAINTAINER Tim Dettrick <t.dettrick@uq.edu.au>  
  
# install  
# - Python 3, PIP and dependencies  
# - Xvfb for background X11 rendering  
# - matplotlib  
# - nltk.draw dependencies  
RUN apt-get update && \  
apt-get install -y \  
python3-pip python3-all-dev \  
xvfb \  
python3-matplotlib \  
python3-tk && \  
apt-get clean  
  
RUN pip3 install ipython jupyter nltk  
  
COPY etc /etc  
COPY var /var  
  
RUN su - researcher -c "mkdir -p ~/.jupyter && echo -e
\"c.NotebookApp.base_url = '/jupyter'\nc.NotebookApp.token = ''\" >
~/.jupyter/jupyter_notebook_config.py"  

