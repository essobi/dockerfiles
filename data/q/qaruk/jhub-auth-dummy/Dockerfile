FROM jupyterhub/jupyterhub  
  
RUN apt-get update && apt-get install -y curl  
  
RUN pip install jupyterhub-dummyauthenticator \  
jupyterhub-kubespawner  
  
RUN /opt/conda/bin/conda install --yes -c conda-forge pycurl  
  
USER root  
COPY startup.sh /startup.sh  
RUN chmod +x /startup.sh  
  
CMD ["/startup.sh"]  

