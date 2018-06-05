#  
# JupyterHub docker image with ldap authentication and kubespawner.  
# Configuration file is jupyterhub-config.py  
#  
# docker run qaruk/k8s-jupyterhub -v ./jupyterhub-
config.py:/srv/jupyterhub/jupyterhub-config.py  
#  
FROM jupyterhub/jupyterhub  
  
RUN apt-get update && apt-get install -y curl  
  
RUN pip install jupyterhub-ldapauthenticator jupyterhub-kubespawner  
RUN conda install -y pycurl  

