FROM continuumio/anaconda:latest  
  
# Copy the package manifests  
COPY manifests "/manifests/"  
RUN chmod 644 /manifests/*  
  
# Install base packages  
RUN set -ex; \  
apt-get update; \  
apt-get install -y \  
bash \  
curl \  
gcc  
  
# Install conda packages from manifest  
RUN set -ex; \  
conda update --yes --quiet conda; \  
conda install --yes --quiet --file /manifests/packages_base.conda; \  
conda install --yes --quiet --channel conda-forge --file
/manifests/packages_base.conda-forge; \  
conda clean --yes --all  
  
# Install pip packages from manifest  
RUN set -ex; \  
pip install --upgrade pip; \  
pip install --no-cache-dir --requirement /manifests/packages_base.pip  
  
# Hacks and cleanup  
RUN set -ex; \  
apt-get install -y \  
libgl1-mesa-glx; \  
apt-get remove -y --purge \  
gcc  
# apt-get autoremove -y --purge  
# Install Dockerize  
ENV DOCKERIZE_VERSION v0.4.0  
RUN set -ex; \  
curl -sOL
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz; \  
tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz; \  
rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
# Set console environment  
RUN echo 'PS1='"'"'\\[\e[01;33m\\][\h
\u:\\[\e[01;34m\\]\w\\[\e[01;33m\\]]\\[\e[00m\\]\$ '"'" >> /root/.bashrc; \  
echo 'eval `dircolors -b`\nalias ls="ls --color=auto"' >> /root/.bashrc  
  
# The entry point  
ENTRYPOINT ["/bin/bash"]

