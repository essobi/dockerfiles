FROM jupyter/datascience-notebook  
  
# Update and install system packages  
USER root  
RUN apt-get update -y && \  
apt-get install --no-install-recommends -y -q \  
libpq-dev \  
libreadline-dev && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Allow sudo to jovyan user  
ENV GRANT_SUDO yes  
  
# Enable Matplotlib inline by default  
COPY config/ipython.py /home/jovyan/.ipython/profile_default/ipython_config.py  
  
# Install requirements packages  
COPY requirements.yml /tmp/requirements.yml  
RUN conda env update -f=/tmp/requirements.yml && \  
conda clean -tipsy && \  
rm -rf /root/.cache/pip/*  
  
# Install buffer package  
COPY buffer /tmp/buffer  
RUN cd /tmp/buffer && \  
python setup.py -q develop  
  
# Enable Jupyter Notebook extensions  
RUN jupyter contrib nbextension install --system  
  
RUN jupyter nbextension enable collapsible_headings/main --system && \  
jupyter nbextension enable spellchecker/main --system && \  
jupyter nbextension enable datestamper/main --system && \  
jupyter nbextension enable execute_time/ExecuteTime --system && \  
jupyter nbextension enable runtools/main --system && \  
jupyter nbextension install
https://github.com/jfbercher/yapf_ext/archive/master.zip --user --system && \  
jupyter nbextension enable yapf_ext-master/yapf_ext --system && \  
jupyter nbextensions_configurator enable  

