FROM v4tech/dev-python-pandas:latest  
MAINTAINER Stewart V. Wright <stewart@vifortech.com>  
  
# Massive overkill - installing a full Anaconda (python 3) and R  
# Useful for offline dev when you don't know what you want to work on...  
# Install full Anaconda  
# Hash is from https://docs.continuum.io/anaconda/hashes/all  
# Hash is from https://mran.revolutionanalytics.com/download/  
ENV ANACONDA_URL="https://repo.continuum.io/archive" \  
ANACONDA_INSTALLER="Anaconda3-5.0.0-Linux-x86_64.sh" \  
ANACONDA_SHA265="67f5c20232a3e493ea3f19a8e273e0618ab678fa14b03b59b1783613062143e9"  
  
  
RUN rm -rf /opt/conda \  
&& wget --quiet ${ANACONDA_URL}/${ANACONDA_INSTALLER} \  
&& sha256sum /${ANACONDA_INSTALLER} | grep -q "${ANACONDA_SHA256}" \  
&& /bin/bash /${ANACONDA_INSTALLER} -b -p /opt/conda \  
&& rm ${ANACONDA_INSTALLER} \  
&& /opt/conda/bin/conda config --append channels r \  
&& /opt/conda/bin/conda upgrade --yes \--all \  
&& /opt/conda/bin/conda install --yes -c r \  
anaconda-client \  
boost \  
boto3 \  
botocore \  
conda-build \  
coverage \  
cvxopt \  
feedparser \  
flake8 \  
future \  
ipykernel \  
ipython \  
ipywidgets \  
matplotlib \  
notebook \  
numpy \  
pandas \  
pep8 \  
pyflakes \  
pymc \  
quandl \  
rpy2 \  
scipy \  
spacy \  
r \  
r-essentials \  
r-xts \  
r-shiny \  
r-readxl \  
r-rsqlite \  
&& /opt/conda/bin/conda clean --yes \--tarballs --packages --source-cache  

