FROM vdsg/python3-ml  
  
MAINTAINER VDSG <contact@vdsg.at>  
  
RUN \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
libfreetype6 libpng3 && \  
pip3 install --upgrade --no-cache-dir \  
matplotlib seaborn notebook && \  
rm -rf /var/lib/apt/lists/* && \  
mkdir /root/.jupyter && \  
mkdir /JupyterNotebooks \  
  
COPY ./jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py  
  
EXPOSE 8888  

