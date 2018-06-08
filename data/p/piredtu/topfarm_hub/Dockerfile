# JupyterHub Docker image built from specific commit on master GitHub branch  
# docker build -t piredtu/topfarm_hub .  
FROM jupyter/jupyterhub  
  
MAINTAINER Pierre-Elouan Rethore <pire@dtu.dk>  
  
  
# We need to update pip, otherwise the version of requests that  
# is installed by dockerspawner breaks things.  
RUN pip3 install --upgrade pip  
  
# Install dockerspawner and oauthenticator  
RUN /usr/local/bin/pip3 install git+git://github.com/docker/docker-
py.git@1.2.0#egg=docker-py  
RUN /usr/local/bin/pip3 install git+git://github.com/jupyter/dockerspawner.git  
RUN /usr/local/bin/pip3 install
git+git://github.com/jupyter/oauthenticator.git  
RUN /usr/local/bin/pip3 install git+git://github.com/docker/docker-
py.git@1.2.0#egg=docker-py  
  
# Add variable to allow connecting to the docker host  
ENV DOCKER_HOST unix://docker.sock  
  
# Create oauthenticator directory -- this is where we'll put the userlist
later  
RUN mkdir /srv/oauthenticator  
ENV OAUTHENTICATOR_DIR /srv/oauthenticator  
RUN chmod 700 /srv/oauthenticator  
  
RUN mkdir /srv/jupyterhub_db  
  
# add the userlist, spawner, and authenticator  
ADD userlist /srv/oauthenticator/userlist  
  
# install docker_oauth  
ADD https://raw.githubusercontent.com/jhamrick/docker-
oauthenticator/master/docker_oauth.py /srv/oauthenticator/docker_oauth.py  
  
# set working directory to the jupyterhub directory  
WORKDIR /srv/jupyterhub  

