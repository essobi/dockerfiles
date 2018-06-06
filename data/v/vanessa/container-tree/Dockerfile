FROM continuumio/miniconda3  
  
RUN /opt/conda/bin/pip install containertree && \  
git clone https://www.github.com/singularityhub/container-tree && \  
cd container-tree/examples/summary_tree_slurm && \  
/opt/conda/bin/python generate.py /database.pkl  

