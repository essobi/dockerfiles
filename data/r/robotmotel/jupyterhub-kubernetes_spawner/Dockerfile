FROM jupyterhub/jupyterhub:latest  
  
RUN apt-get update && apt-get install -y curl  
RUN pip install jupyterhub-ldapauthenticator  
RUN pip install git+git://github.com/cyberroadie/jupyterhub-
kubernetes_spawner.git@master  
  
USER root  
COPY startup.sh /startup.sh  
RUN chmod +x /startup.sh  
  
CMD ["/startup.sh"]  

