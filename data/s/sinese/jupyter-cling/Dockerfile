FROM jupyterhub/singleuser:0.8  
USER root  
  
RUN cd .. && \  
wget https://root.cern.ch/download/cling/cling_2018-02-26_ubuntu16.tar.bz2 &&
\  
tar -xvjf cling_2018-02-26_ubuntu16.tar.bz2 && \  
rm cling_*.tar.bz2 && \  
mv cling_* /opt/cling && \  
chown jovyan:users -R /opt/cling  
  
RUN apt-get -y update && \  
apt-get -y install build-essential minizip zlib1g-dev subversion texinfo git  
  
USER jovyan  
  
ENV PATH=/opt/conda/bin:/opt/cling/bin:$PATH  
  
RUN cd /opt/cling/share/cling/Jupyter/kernel && \  
pip install -e . && \  
jupyter-kernelspec install cling-cpp17 --user && \  
jupyter-kernelspec install cling-cpp14 --user && \  
jupyter-kernelspec install cling-cpp11 --user  
  
USER root  
  
RUN chown jovyan:users -R /home/jovyan  
  
USER jovyan  
  

