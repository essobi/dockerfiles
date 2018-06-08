FROM v4tech/dev-python-pandas:latest  
MAINTAINER Stewart V. Wright <stewart@vifortech.com>  
  
# Massive overkill - installing a full Anaconda (python 2.7) and R  
# Useful for offline dev when you don't know what you want to work on...  
# Install full Anaconda  
# Hash is from https://docs.continuum.io/anaconda/hashes/all  
# Hash is from https://mran.revolutionanalytics.com/download/  
ENV ANACONDA_URL="https://repo.continuum.io/archive" \  
ANACONDA_INSTALLER="Anaconda2-4.2.0-Linux-x86_64.sh" \  
ANACONDA_SHA265="beee286d24fb37dd6555281bba39b3deb5804baec509a9dc5c69185098cf661a"  
  
  
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
cvxcanon \  
cvxopt \  
feedparser \  
flake8 \  
future \  
gdata \  
googlecl \  
icalendar \  
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

