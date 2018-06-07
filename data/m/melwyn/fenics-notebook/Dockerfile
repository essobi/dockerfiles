FROM jupyter/scipy-notebook:c88678a1c7c9  
  
LABEL maintainer="Lars Melwyn <melwyn (at) scico.io>"  
  
USER $NB_UID  
  
RUN conda install --quiet --yes 'fenics' && \  
fix-permissions $CONDA_DIR && \  
fix-permissions /home/$NB_USER  
  

