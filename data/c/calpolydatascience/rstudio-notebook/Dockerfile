FROM calpolydatascience/rstudio:0.3  
LABEL maintainer="CSM Computing Support <csm-servicedesk@calpoly.edu>"  
  
USER root  
  
# Install all OS dependencies for notebook server that starts but lacks all  
# features (e.g., download as all possible file formats)  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get -yq dist-upgrade \  
&& apt-get install -yq --no-install-recommends \  
wget \  
bzip2 \  
ca-certificates \  
sudo \  
locales \  
fonts-liberation \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \  
locale-gen  
  
# Install Tini  
RUN wget --quiet
https://github.com/krallin/tini/releases/download/v0.10.0/tini && \  
echo "1361527f39190a7338a0b434bd8c88ff7233ce7b9a4876f3315c22fce7eca1b0 *tini"
| sha256sum -c - && \  
mv tini /usr/local/bin/tini && \  
chmod +x /usr/local/bin/tini  
  
# Configure environment  
ENV CONDA_DIR=/srv/venv \  
SHELL=/bin/bash \  
NB_USER=jovyan \  
NB_UID=1000 \  
NB_GID=100 \  
LC_ALL=en_US.UTF-8 \  
LANG=en_US.UTF-8 \  
LANGUAGE=en_US.UTF-8 \  
R_LIBS_USER=~/R/packages \  
R_LIBS_SITE=/usr/local/lib/R/site-library:/usr/lib/R/site-
library:/usr/lib/R/library:/srv/rlibs  
ENV PATH=$CONDA_DIR/bin:$PATH \  
PATH=$PATH:/srv/venv/bin/ \  
HOME=/home/$NB_USER  
  
ADD fix-permissions /usr/local/bin/fix-permissions  
  
# Create jovyan user with UID=1000 and in the 'users' group  
# and make sure these dirs are writable by the `users` group.  
# RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER && \  
# mkdir -p $CONDA_DIR && \  
# chown $NB_USER:$NB_GID $CONDA_DIR && \  
RUN chmod g+w /etc/passwd /etc/group && \  
chmod +x /usr/local/bin/fix-permissions  
  
# && \  
# fix-permissions $CONDA_DIR  
# Setup work directory for backward-compatibility  
RUN mkdir /home/$NB_USER/work && \  
fix-permissions $HOME && \  
fix-permissions /home/$NB_USER  
  
EXPOSE 8888  
WORKDIR $HOME  
  
# Configure container startup  
ENTRYPOINT ["tini", "--"]  
CMD ["start-notebook.sh"]  
  
# Add local files as late as possible to avoid cache busting  
COPY start.sh /usr/local/bin/  
COPY start-notebook.sh /usr/local/bin/  
COPY start-singleuser.sh /usr/local/bin/  
COPY jupyter_notebook_config.py /etc/jupyter/  
COPY rsession.conf /etc/rstudio/rsession.conf  
COPY Renviron /etc/R/Renviron  
RUN fix-permissions /etc/jupyter/  
  
# Switch back to jovyan to avoid accidental container runs as root  
USER $NB_UID  

