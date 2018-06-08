FROM python:2.7  
LABEL maintainer "Fábio Tramasoli <tramasoli@mprs.mp.br>"  
LABEL env "DEV"  
LABEL purpose "SNAKEFOOD"  
LABEL version "0.0.1"  
ENV USER=snakefood  
ENV WORKDIR=/opt/workdir  
# COPIES CUSTOM SCRIPTS AND APPS  
COPY bin/*sh /usr/local/bin  
COPY files/snakefood /tmp/snakefood  
# https://docs.docker.com/engine/userguide/storagedriver/overlayfs-
driver/#limitations-on-overlayfs-compatibility  
RUN cd /tmp/snakefood && \  
pip install six && \  
python setup.py install && \  
useradd -ms /bin/bash ${USER} && \  
mkdir -p ${WORKDIR}  
USER ${USER}  
WORKDIR /home/${USER}  
VOLUME ${WORKDIR}  
CMD sfood  

