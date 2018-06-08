#****************************************************************************  
# A Sherpa Dockerfile. From an example by Andrew Odewahn (@odewahn)  
#  
# - https://github.com/DougBurke/sherpa-standalone-notebooks  
# - https://github.com/sherpa/sherpa  
# - https://hub.docker.com/r/continuumio/miniconda/  
#  
#****************************************************************************  
FROM frolvlad/alpine-glibc  
  
MAINTAINER Omar Laurino <olaurino@cfa.harvard.edu>  
  
#****************************************************************************  
# Install Miniconda3 (inspired by kyoba/miniconda3-alpine)  
#****************************************************************************  
ENV PATH=/opt/conda/bin:$PATH \  
MINICONDA=Miniconda3-latest-Linux-x86_64.sh  
  
RUN apk add --no-cache --virtual=build-deps --update-cache wget \  
&& wget -q --no-check-certificate
https://repo.continuum.io/miniconda/$MINICONDA \  
&& apk del build-deps \  
&& apk add --no-cache --update-cache bash \  
&& /bin/bash $MINICONDA -b -p /opt/conda \  
&& rm -rf /root/.continuum /opt/conda/pkgs/* \  
&& rm $MINICONDA  
  
#****************************************************************************  
# Install required conda libraries  
#****************************************************************************  
RUN conda install -y -c sherpa \  
notebook=4.2.3 matplotlib astropy=1.3 scipy sherpa=4.9.1 nomkl && \  
conda remove -y --force qt pyqt qtconsole && \  
conda clean -tipsy && \  
rm -rf /opt/conda/pkgs/* && \  
pip install saba corner  
  
# Expose the notebook port  
EXPOSE 8888  
# Add notebooks to image  
ADD . /data  
  
# Set working dir  
WORKDIR /data  
  
# Mount conda environments folder as volume for persistence  
VOLUME /opt/conda/envs  
  
# Single CPU Configuration file  
ENV SHERPARC=/data/sherparc  
  
#****************************************************************************  
# Fire it up  
#****************************************************************************  
CMD ipython notebook --no-browser --port 8888 --ip=*  
  

