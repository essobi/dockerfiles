FROM jupyter/scipy-notebook  
  
MAINTAINER Shogun Team <shogun-team@shogun-toolbox.org>  
  
USER root  
  
RUN conda install --quiet --yes -c conda-forge shogun  
  
USER jovyan  
ENV SHOGUN_DATA_DIR /home/jovyan/work/data  
  
EXPOSE 8888  
CMD ["start-singleuser.sh"]  

