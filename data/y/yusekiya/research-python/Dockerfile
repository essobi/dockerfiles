FROM continuumio/anaconda3:5.0.1  
RUN echo deb http://ftp.uk.debian.org/debian jessie-backports main >>
/etc/apt/sources.list &&\  
apt-get update && apt-get install -y fonts-freefont-ttf ffmpeg &&\  
apt-get clean  
RUN conda install -yq jupyter psycopg2  
RUN mkdir -p /project/notebook  
COPY jupyter_notebook_config.py /opt/conda/etc/jupyter/  
WORKDIR "/project"  
CMD ["/opt/conda/bin/jupyter", "notebook", "--allow-root"]  
EXPOSE 8888  

