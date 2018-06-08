FROM tsutomu7/scientific-python  
  
ENV DEBIAN_FRONTEND=noninteractive  
RUN conda install -y --channel https://conda.anaconda.org/cachemeorg
funcdesigner openopt && \  
pip install --no-cache openopt mypulp myopenopt && \  
find /opt -name __pycache__ | xargs rm -r && \  
sudo rm -rf /opt/conda/pkgs/*  
CMD ["/bin/bash"]  

