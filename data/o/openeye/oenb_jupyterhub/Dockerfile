FROM ubuntu:14.04  
MAINTAINER OpenEye <mattg@eyesopen.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get upgrade -y && \  
apt-get install -y wget libcairo2-dev npm nodejs nodejs-legacy && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Need to rebuild pam to deal with kernel issue  
# rebuild and install libpam with --disable-audit option  
# see https://github.com/sequenceiq/docker-pam  
RUN apt-get update && apt-get -y build-dep pam && export
CONFIGURE_OPTS=--disable-audit && cd /root && apt-get -b source pam && \  
dpkg -i libpam-doc*.deb libpam-modules*.deb libpam-runtime*.deb libpam0g*.deb
&& \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Configure environment  
ENV CONDA_DIR /opt/conda  
ENV PATH $CONDA_DIR/bin:$PATH  
ENV SHELL /bin/bash  
  
# Install Conda with Python3 for JupyterHub  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-
Linux-x86_64.sh && \  
bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda && \  
rm Miniconda3-latest-Linux-x86_64.sh && \  
/opt/conda/bin/conda update --quiet --yes conda && \  
/opt/conda/bin/conda install --yes sqlalchemy tornado jinja2 traitlets
requests pip && \  
/opt/conda/bin/pip install --upgrade pip  
  
# install js dependencies and jupyterhub  
RUN npm install -g configurable-http-proxy && rm -rf ~/.npm  
RUN pip --no-cache-dir install jupyterhub  
  
# Install Python/IPython/Jupyter Stack  
RUN conda install --quiet --yes \  
'numpy' \  
'scipy' \  
'pandas' \  
'matplotlib' \  
'seaborn' \  
'scikit-learn' \  
'sympy' \  
'patsy' \  
'statsmodels' \  
'jupyter' \  
'ipywidgets' \  
'bokeh' \  
&& conda clean -yt  
  
# Create python2 env  
RUN conda create -p $CONDA_DIR/envs/py2 python=2.7 \  
'numpy' \  
'scipy' \  
'pandas' \  
'matplotlib' \  
'seaborn' \  
'scikit-learn' \  
'sympy' \  
'patsy' \  
'statsmodels' \  
'jupyter' \  
'ipywidgets' \  
'bokeh' \  
&& conda clean -yt  
  
# Install Python 2 kernel spec globally  
RUN $CONDA_DIR/envs/py2/bin/python \  
$CONDA_DIR/envs/py2/bin/jupyter \  
kernelspec install-self  
  
# Install OE TKs  
COPY requirements.txt /tmp/requirements.txt  
RUN pip --no-cache-dir install -r /tmp/requirements.txt && \  
pip --no-cache-dir install --pre --extra-index-url
https://pypi.anaconda.org/OpenEye/channel/beta/simple OpenEye-oenotebook && \  
pip --no-cache-dir install -U --pre -i
https://pypi.anaconda.org/OpenEye/channel/rc/simple OpenEye-toolkits  
  
RUN $CONDA_DIR/envs/py2/bin/pip --no-cache-dir install -r
/tmp/requirements.txt && \  
$CONDA_DIR/envs/py2/bin/pip --no-cache-dir install --pre --extra-index-url
https://pypi.anaconda.org/OpenEye/channel/beta/simple OpenEye-oenotebook  
  
# Make python2 kernel the default in notebooks.  
RUN /bin/bash -c "source activate py2 && ipython kernel install && source
deactivate"  
EXPOSE 8888  
# Set Up External Volumes for Notebooks  
VOLUME /opt/hub_data  
ENV OE_LICENSE /opt/hub_data/oe_license.txt  
  
RUN mkdir /srv/oauthenticator  
WORKDIR /srv/oauthenticator  
ENV OAUTHENTICATOR_DIR /srv/oauthenticator  
  
# Set up ssl if present  
ADD ssl /srv/oauthenticator/ssl  
  
ADD local_jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py  
  
ADD cull_idle_servers.py /tmp/cull_idle_servers.py  
RUN chmod 700 /srv/oauthenticator  
  
ADD add_user.sh /tmp/add_user.sh  
  
CMD ["jupyterhub", "-f", "/srv/jupyterhub/jupyterhub_config.py","--
port","80","--no-ssl"]  

