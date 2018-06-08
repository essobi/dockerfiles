FROM continuumio/miniconda3  
  
LABEL maintainer="Nick Ma <www.github.com/nma>"  
  
RUN conda create -n gensim gensim pandas numpy matplotlib scikit-learn mpld3
python=3.4 jupyter notebook  
  
# Default to run the DL environment if running as /bin/bash  
RUN echo "source activate gensim" >> /root/.bashrc  
# Ignore ctrl+d from exitting our docker container  
RUN echo "set -o ignoreeof" >> /root/.bashrc  
  
COPY jupyter_notebook_config.py /root/.jupyter/  
COPY run_jupyter.sh /  
  
# Jupyter Notebook port  
EXPOSE 8888  
# Execute the notebook by default  
CMD ["/run_jupyter.sh"]  

