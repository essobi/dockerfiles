FROM jupyterhub/jupyterhub-onbuild:0.7.0  
MAINTAINER Matt Edwards <matted@mit.edu>  
  
RUN pip install --upgrade pip && \  
pip install --upgrade git+git://github.com/jupyter/dockerspawner.git@0.5.0 &&
\  
pip install --upgrade git+git://github.com/matted/mit-oidc-authenticator.git  
  
# Copy to another location in the image, since we optionally mount  
# /srv/jupyterhub as persistent storage between hub restarts.  
RUN cp /srv/jupyterhub/jupyterhub_config.py /root/jupyterhub_config.py  

