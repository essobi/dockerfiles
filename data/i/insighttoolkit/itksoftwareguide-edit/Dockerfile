FROM jupyter/base-notebook:latest as jupyter  
  
FROM insighttoolkit/itksoftwareguide-bin:latest as itksoftwareguide  
MAINTAINER Matt McCormick <matt.mccormick@kitware.com>  
  
RUN apt-get update && apt-get install -y \  
bash-completion \  
liquidprompt \  
sudo  
  
# Import Jupyter configuration and binaries  
# Configure environment  
ENV CONDA_DIR=/opt/conda \  
SHELL=/bin/bash \  
NB_USER=jovyan \  
NB_UID=1000 \  
NB_GID=100 \  
LC_ALL=en_US.UTF-8 \  
LANG=en_US.UTF-8 \  
LANGUAGE=en_US.UTF-8  
ENV PATH=$CONDA_DIR/bin:$PATH \  
HOME=/home/$NB_USER  
COPY \--from=jupyter /usr/local/bin/fix-permissions /usr/local/bin/  
# Create jovyan user with UID=1000 and in the 'users' group  
# and make sure these dirs are writable by the `users` group.  
RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER && \  
mkdir -p $CONDA_DIR && \  
chown $NB_USER:$NB_GID $CONDA_DIR && \  
fix-permissions $HOME && \  
fix-permissions $CONDA_DIR  
  
COPY \--from=jupyter /usr/local/bin/tini /usr/local/bin/  
COPY \--from=jupyter /opt/conda /opt/conda  
COPY \--from=jupyter /usr/local/bin/start.sh /usr/local/bin/  
COPY \--from=jupyter /usr/local/bin/start-notebook.sh /usr/local/bin/  
COPY \--from=jupyter /usr/local/bin/start-singleuser.sh /usr/local/bin/  
COPY \--from=jupyter /etc/jupyter/jupyter_notebook_config.py /etc/jupyter/  
RUN fix-permissions /etc/jupyter/  
RUN fix-permissions /ITKSoftwareGuide  
RUN fix-permissions /ITKSoftwareGuide-build && \  
chown -R $NB_USER:$NB_GID /ITKSoftwareGuide-build  
  
RUN /usr/bin/liquidprompt_activate  
  
EXPOSE 8888  
WORKDIR /  
  
# Configure container startup  
ENTRYPOINT ["tini", "--"]  
CMD ["start.sh", "jupyter", "lab"]  
  
USER $NB_USER  

