# Copyright (c) Jupyter Development Team.  
# Derived from Jupyter notebook stack.  
# Distributed under the terms of the Modified BSD License.  
FROM marcsaric/minimal-notebook  
  
LABEL maintainer="Marc Saric <marc.saric@gmx.de>"  
  
USER root  
  
# FIXME: Setup git-annex  
# Install all OS dependencies for fully functional notebook server  
RUN apt-get update && apt-get install -yq --no-install-recommends \  
ftp-ssl \  
rng-tools \  
&& apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Testinstall the bash-kernel from https://github.com/takluyver/bash_kernel  
RUN pip install bash_kernel \  
&& python -m bash_kernel.install  
  
# Switch back to jovyan to avoid accidental container runs as root  
USER $NB_USER  
  
# This somehow did not work really  
RUN git config --global user.email "marc.saric@gmx.de"  
RUN git config --global user.name "Marc Saric"  
  

