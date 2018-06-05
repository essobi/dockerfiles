FROM jupyterhub/jupyterhub  
  
RUN apt-get update && apt-get install -y curl  
  
# Authentification  
RUN pip install jupyterhub-kubespawner \  
jupyterhub-dummyauthenticator  
  
CMD ["jupyterhub"]  

