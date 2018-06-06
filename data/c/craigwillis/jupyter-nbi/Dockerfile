FROM jupyter/scipy-notebook  
  
USER root  
  
RUN echo "deb http://ftp.uk.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list && \  
apt-get update -y && \  
apt-get install -y python-matplotlib && \  
apt-get clean && \  
pip install pymongo pandas folium && \  
rm -rf /var/lib/apt/lists/*  
  
USER $NB_USER  
ENV USER $NB_USER  
COPY start-notebook.sh /usr/local/bin/  
  
ENV HOME /home/jovyan  
WORKDIR /home/jovyan/work  
CMD ["start-notebook.sh", "--NotebookApp.token=''"]  

