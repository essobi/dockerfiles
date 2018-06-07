FROM continuumio/miniconda3  
  
LABEL maintainer="Nick Ma <www.github.com/nma>"  
  
COPY dl_env_linux.yml /  
  
RUN conda env create --name dl -f dl_env_linux.yml  
  
# Default to run the DL environment if running as /bin/bash  
RUN echo "source activate dl" >> /root/.bashrc  
# Ignore ctrl+d from exitting our docker container  
RUN echo "set -o ignoreeof" >> /root/.bashrc  
  
COPY requirements.txt /  
COPY install_requirements.sh /  
RUN /install_requirements.sh  
  
COPY jupyter_notebook_config.py /root/.jupyter/  
COPY run_jupyter.sh /  
  
# Jupyter Notebook port  
EXPOSE 8888  
# Tensorboard port  
EXPOSE 6006  
# Execute the notebook by default  
CMD ["/run_jupyter.sh"]  

