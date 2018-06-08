########################################################################  
# Dockerfile for a minimal Git server over SSH  
#  
# ## .  
# ## ## ## ==  
# ## ## ## ## ===  
# /""""""""""""""""\\___/ ===  
# ~~~ {~~ ~~~~ ~~~ ~~~~ ~~ ~ / ===- ~~~  
# \\______ o __/  
# \ \ __/  
# \\____\\______/  
#  
# Component: Minimal Git server over SSH  
# Author: pjan vandaele <pjan@pjan.io>  
# Scm url: https://github.com/docxs/docker-git-server  
# License: MIT  
########################################################################  
  
# pull base image  
FROM docxs/base:latest  
  
# maintainer details  
MAINTAINER pjan vandaele "pjan@pjan.io"  
  
# Install the SSH server and Git  
RUN \  
apt-prepare && \  
apt-get install -q -y \  
openssh-server \  
git && \  
apt-cleanup &&\  
mkdir /var/run/sshd  
  
# Configure ssh  
COPY ./config/etc_ssh_ssh_config /etc/ssh/ssh_config  
  
# Copy the run script  
COPY ./bin /bin  
  
# expose ssh  
EXPOSE \  
22  
  
ENTRYPOINT \  
["/bin/gitserver-run"]  
  
# docker build [--rm] -t <user>/gitserver .  
# docker run -v /data --name gitserver-data busybox  
# docker run -d -v /etc/localtime:/etc/localtime:ro --volumes-from gitserver-
data -p 2222:22 \--name git <user>/gitserver  

