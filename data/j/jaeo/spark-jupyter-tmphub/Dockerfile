  
##################################################  
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
## Spark-Jupyterhub with temporal authentication  
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
##################################################  
  
FROM jaeo/spark-jupyter  
USER root  
  
RUN pip install \  
dockerspawner \  
jupyterhub-tmpauthenticator  
  
USER $NB_UID

