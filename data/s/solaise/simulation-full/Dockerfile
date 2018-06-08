FROM solaise/simulation-base:latest  
  
# Copy the package manifests  
COPY manifests "/manifests/"  
RUN chmod 644 /manifests/*  
  
# Install conda packages from manifest  
RUN set -ex; \  
conda install --yes --quiet --file /manifests/packages.conda; \  
conda install --yes --quiet --channel conda-forge --file
/manifests/packages.conda-forge; \  
conda clean --yes --all  
  
# Install pip packages from manifest and dependencies from apt  
RUN set -ex; \  
apt-get update; \  
apt-get install -y \  
gcc \  
freetds-dev \  
texlive \  
texlive-latex-extra \  
pandoc; \  
pip install --no-cache-dir --requirement /manifests/packages.pip  
  
# Cleanup  
RUN set -ex; \  
apt-get remove -y --purge \  
gcc  
# apt-get autoremove -y --purge  
# The entry point  
ENTRYPOINT ["/bin/bash"]

