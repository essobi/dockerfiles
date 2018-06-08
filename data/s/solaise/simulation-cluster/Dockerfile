FROM solaise/miniconda:latest  
  
# Copy the package manifests  
COPY ["packages.conda", "/packages.pip", "./"]  
  
# Install packages  
RUN set -ex; \  
conda install --yes --quiet \  
\--file packages.conda; \  
conda clean --yes --all; \  
apt-get update; \  
apt-get install -y \  
gcc; \  
pip install --no-cache-dir \  
\--requirement packages.pip; \  
apt-get remove -y --purge \  
gcc; \  
apt-get autoremove -y --purge  
  
# The entry point  
ENTRYPOINT ["/bin/bash"]

