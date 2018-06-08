# python3-notebook Dockerfile  
FROM oldschoolweaver/python3-base:latest  
LABEL Miguel Soares <miguel.bayan.soares@gmail.com>  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
ENV SHELL /bin/bash  
ENV NB_USER notebook  
ENV NB_UID 1000  
ENV HOME /home/$NB_USER  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
# Create notebook user with UID=1000 and in the 'users' group  
RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER  
  
#USER $NB_USER  
USER root  
  
# Setup work directory for backward-compatibility  
RUN mkdir /home/$NB_USER/work  
RUN chmod -R 777 /home/$NB_USER/  
  
#USER root  
WORKDIR /home/$NB_USER/work  
  
# Safety step to remove any old iPython packages that may have crept in. If we
do not remove, then an import error will occur in Jupyter due to the conflict
caused by Jupyter installing the newest version of iPython.  
RUN apt-get purge -y ipython* && \  
apt-get update && apt-get install sudo && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN sudo -H pip3 install jupyter && sudo -H pip3 install jupyterlab  
RUN echo "Finished Install of Jupyter Notebook"  
RUN jupyter serverextension enable \--py jupyterlab --sys-prefix  
  
RUN echo "root:password" | chpasswd  
RUN echo "notebook:password" | chpasswd  
  
RUN sudo adduser notebook sudo  
  
EXPOSE 8888  
WORKDIR $HOME  
  
# Configure container startup  
#ENTRYPOINT ["tini", "--"]  
CMD ["start.sh"]  
  
COPY jupyter_notebook_config.py /etc/jupyter/  
RUN chown -R $NB_USER:users /home/$NB_USER/  
RUN chown -R $NB_USER:users /etc/jupyter/  
  
# Switch back to jovyan to avoid accidental container runs as root  
USER $NB_USER  
  
# Add local files as late as possible to avoid cache busting  
COPY start.sh /usr/local/bin/  

