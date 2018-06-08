# ninjaben/jupyter-hub-oauth  
#  
# JupyterHub with user and OAuth config mounted at container start.  
#  
# This image is inspired by the jupyterhub official oauthenticator example:  
# https://github.com/jupyterhub/oauthenticator/tree/master/example  
#  
# Instead of baking user configuration into the Docker image at build time,  
# config is mounted in at container start time.  
#  
# This expects you to supply some local configuration:  
# - CONF is a host folder with your configuration:  
# - CONF/userlist defines trusted users and admins  
# - CONF/ssl/ssl.cert optional, for ssh  
# - CONF/ssl/ssl.key optional, for ssh  
# - ENV_FILE is your environment file with oauth info and secrets  
#  
# userlist file should have one user per line, followed by "admin" if it's an
admin user:  
# jane admin  
# jon  
# arnie  
#  
# Your environment file should have GitHub and Google OAuth secrets:  
# OAUTH_CALLBACK_URL=  
# OAUTH_CLIENT_ID=  
# OAUTH_CLIENT_SECRET=  
# GITHUB_CLIENT_ID=  
# GITHUB_CLIENT_SECRET=  
#  
# Then you can run:  
# sudo docker run -p 443:443 -v $CONF:/var/jupyter --env-file=$ENV_FILE -t -i
ninjaben/jupyter-hub-oauth  
#  
FROM jupyterhub/jupyterhub  
  
MAINTAINER Ben Heasly <benjamin.heasly@gmail.com>  
  
# Python libs  
RUN pip install jupyter \  
&& pip install jupyter_client  
  
# Install oauthenticator  
RUN python3 -m pip install oauthenticator  
  
# Create shared notebook folder and checkpoint folder  
RUN mkdir -p /srv/ipython/examples/.ipynb_checkpoints/ \  
&& chmod -R 777 /srv/ipython/examples  
ADD Hello.ipynb /srv/ipython/examples/Hello.ipynb  
  
# Create oauthenticator directory  
WORKDIR /srv/oauthenticator  
ENV OAUTHENTICATOR_DIR /srv/oauthenticator  
  
# Get config for jupyterhub and oauth  
ADD jupyterhub_config.py /srv/oauthenticator/jupyterhub_config.py  
ADD addusers.sh /srv/oauthenticator/addusers.sh  
ADD oauth-setup-and-run-jupyterhub /srv/oauthenticator/oauth-setup-and-run-
jupyterhub  
  
# Set up users and launch jupyterhub.  
RUN groupadd jupyter  
ENTRYPOINT ["/bin/bash", "/srv/oauthenticator/oauth-setup-and-run-jupyterhub"]  
  

