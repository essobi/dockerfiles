# Docker demo image, as used on try.jupyter.org and tmpnb.org  
FROM jupyter/minimal-notebook:2d878db5cbff  
MAINTAINER Oscar Esteban <oesteban@stanford.edu>  
  
# Install system libraries first as root  
USER root  
  
# Use bash  
RUN ln -snf /bin/bash /bin/sh  
ARG DEBIAN_FRONTEND=noninteractive  
  
# Update packages and install the minimal set of tools  
RUN apt-get update && \  
apt-get install -y --no-install-recommends wget curl git xvfb bzip2 apt-utils
\  
gfortran \  
graphviz \  
liblapack-dev \  
libblas-dev \  
libatlas-dev \  
libatlas-base-dev \  
libblas3 \  
libblas-common \  
libopenblas-dev \  
libxml2-dev \  
libxslt1-dev \  
libfreetype6-dev \  
libpng12-dev \  
libqhull-dev \  
libxft-dev \  
libjpeg-dev \  
libyaml-dev && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install FSL  
RUN mkdir -p /opt && \  
mkdir downloads && \  
wget -q -O downloads/FSL.tar.gz
http://googledrive.com/host/0BxI12kyv2olZZEVsMkc2WE1LZVk && \  
tar xzf downloads/FSL.tar.gz -C /opt  
RUN rm -rf downloads  
  
# Now switch to jovyan for all conda and other package manager installs  
USER jovyan  
WORKDIR /home/jovyan/  
  
# Python packages  
RUN conda install --yes numpy pandas scikit-learn scikit-image matplotlib
scipy seaborn sympy cython patsy statsmodels cloudpickle dill numba bokeh
beautifulsoup4 && \  
conda clean -yt && \  
pip install --user \--no-cache-dir pydotplus && \  
pip install --user \--no-cache-dir -e
git+https://github.com/nipy/nipype#egg=nipype  
# Now for a python2 environment  
RUN conda create -p $CONDA_DIR/envs/python2 python=2.7 ipykernel numpy pandas
scikit-learn scikit-image matplotlib scipy seaborn sympy cython patsy
statsmodels cloudpickle dill numba bokeh && \  
conda clean -yt && \  
source activate python2 && \  
python -m ipykernel install --user && \  
pip install --user --no-cache-dir pydotplus && \  
pip install --user --no-cache-dir -e
git+https://github.com/nipy/nipype#egg=nipype  
  
# Extra Kernels  
RUN pip install --user --no-cache-dir bash_kernel && \  
python -m bash_kernel.install  
  
WORKDIR /home/jovyan/work  
ADD notebooks/ /home/jovyan/work/  
  
# Add local content, starting with notebooks and datasets which are the
largest  
# so that later, smaller file changes do not cause a complete recopy during  
# build  
# COPY notebooks/ /home/jovyan/work/  
# COPY datasets/ /home/jovyan/work/datasets/  
# Switch back to root for permission fixes, conversions, and trust. Make sure  
# trust is done as jovyan so that the signing secret winds up in the jovyan  
# profile, not root's  
USER root  
  
# Set-up environment  
# Make sure that appropriate files are sourced in login and non-login shells  
RUN echo '#!/bin/bash' > /etc/profile.d/crn_neuro.sh && \  
echo 'export FSLDIR=/opt/fsl' >> /etc/profile.d/crn_neuro.sh && \  
echo 'export PATH=$FSLDIR/bin:$PATH' >> /etc/profile.d/crn_neuro.sh && \  
echo 'source $FSLDIR/etc/fslconf/fsl.sh' >> /etc/profile.d/crn_neuro.sh && \  
echo 'source /etc/profile.d/crn_neuro.sh' >> /etc/bash.bashrc  
  
# Convert notebooks to the current format and trust them  
RUN find /home/jovyan/work -name '*.ipynb' -exec jupyter nbconvert --to
notebook {} --output {} \; && \  
chown -R jovyan:users /home/jovyan && \  
sudo -u jovyan env "PATH=$PATH" find /home/jovyan/work -name '*.ipynb' -exec
jupyter trust {} \;  
  
EXPOSE 8888  
ADD start-notebook.sh /usr/local/bin/start-notebook.sh  
RUN chmod +x /usr/local/bin/start-notebook.sh  
  
# Finally, add the site specific tmpnb.org / try.jupyter.org configuration.  
# These should probably be split off into a separate docker image so that
others  
# can reuse the very expensive build of all the above with their own site  
# customization.  
# Expose our custom setup to the installed ipython (for mounting by nginx)  
# COPY resources/custom.js /opt/conda/lib/python3.4/site-
packages/notebook/static/custom/  
# Add the templates  
# COPY resources/templates/ /srv/templates/  
# RUN chmod a+rX /srv/templates  
# Append tmpnb specific options to the base config  
# COPY resources/jupyter_notebook_config.partial.py /tmp/  
# RUN cat /tmp/jupyter_notebook_config.partial.py >>
/home/jovyan/.jupyter/jupyter_notebook_config.py && \  
# rm /tmp/jupyter_notebook_config.partial.py  

