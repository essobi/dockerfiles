FROM jupyter/minimal-notebook:latest  
  
LABEL maintainer="Rafal Skolasinski <r.j.Skolasinski@gmail.com>"  
  
USER root  
  
# Add environment file  
RUN mkdir /environments  
COPY environment.yml /environments/  
  
RUN conda install --yes -c defaults conda=4.5 nb_conda=2.2.1  
RUN conda env create --file /environments/environment.yml  
  
# Fix permissions (required when following the base image)  
RUN fix-permissions /opt/conda  
  
# Cleanup all downloaded conda files  
RUN conda clean --yes --all  
  
# Switch back to jovyan to avoid accidental container runs as root  
USER $NB_UID  

