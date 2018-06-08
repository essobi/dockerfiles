# Use the official miniconda linux distro  
FROM continuumio/miniconda:latest  
  
# Install base packages  
RUN set -ex; \  
apt-get update; \  
apt-get install \  
bash \  
curl; \  
pip install --upgrade pip  
  
# Set console environment  
RUN echo 'PS1='"'"'\\[\e[01;33m\\][\h
\u:\\[\e[01;34m\\]\w\\[\e[01;33m\\]]\\[\e[00m\\]\$ '"'" >> /root/.bashrc; \  
echo -e 'eval `dircolors -b`\nalias ls="ls --color=auto"\nalias l="ls
-lah"\nalias ll="ls -lh"' >> /root/.bashrc  
  
# Install Dockerize  
ENV DOCKERIZE_VERSION v0.3.0  
RUN set -ex; \  
curl -sOL
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz; \  
tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz; \  
rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
# Entrypoint  
ENTRYPOINT ["/bin/bash"]

