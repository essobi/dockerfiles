FROM continuumio/anaconda  
  
RUN conda install -y jupyter seaborn scikit-image pyqtgraph \  
&& conda install -y -c conda-forge tqdm \  
&& mkdir /opt/notebooks  
  
WORKDIR /opt/notebooks  
  
CMD ["/opt/conda/bin/jupyter", "notebook", "--notebook-dir=/opt/notebooks", "
--ip='*'", "--port=8888", "--no-browser"]  

