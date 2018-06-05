### https://hub.docker.com/r/continuumio/anaconda3/~/dockerfile/  
# FROM debian:8.5  
  
# MAINTAINER Kamil Kwiek <kamil.kwiek@continuum.io>  
  
# ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
  
# RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-
certificates \  
# libglib2.0-0 libxext6 libsm6 libxrender1 \  
# git mercurial subversion  
  
# RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
# wget --quiet
https://repo.continuum.io/archive/Anaconda3-4.1.1-Linux-x86_64.sh -O
~/anaconda.sh && \  
# /bin/bash ~/anaconda.sh -b -p /opt/conda && \  
# rm ~/anaconda.sh  
  
# RUN apt-get install -y curl grep sed dpkg && \  
# TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o
"/v.*\"" | sed 's:^..\\(.*\\).$:\1:'` && \  
# curl -L
"https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb"
> tini.deb && \  
# dpkg -i tini.deb && \  
# rm tini.deb && \  
# apt-get clean  
  
# ENV PATH /opt/conda/bin:$PATH  
  
# ENTRYPOINT [ "/usr/bin/tini", "--" ]  
# CMD [ "/bin/bash" ]  
### My Added Code  
FROM continuumio/anaconda3  
MAINTAINER Damiano Lombardo  
  
ENV JUPYTER_CONFIG_DIR="/opt/jupyterprofile"  
  
RUN /opt/conda/bin/conda install jupyter -y --quiet  
RUN /opt/conda/bin/jupyter notebook --generate-config  
  
ENTRYPOINT [ "/usr/bin/tini", "--" ]  
  
CMD ["/opt/conda/bin/jupyter", "notebook", "--ip='*'", "--no-browser", "--
notebook-dir=/opt/notebooks", "--port=9999"]  
  

