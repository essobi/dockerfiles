FROM phusion/baseimage:0.9.19  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
MAINTAINER Kyle Wilcox <kyle@axiomdatascience.com>  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANG C.UTF-8  
RUN apt-get update && apt-get install -y \  
binutils \  
build-essential \  
bzip2 \  
ca-certificates \  
git \  
libglib2.0-0 \  
libsm6 \  
libxext6 \  
libxrender1 \  
pwgen \  
wget \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Setup CONDA (https://hub.docker.com/r/continuumio/miniconda3/~/dockerfile/)  
ENV MINICONDA_VERSION 4.1.11  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
curl -k -o /miniconda.sh
https://repo.continuum.io/miniconda/Miniconda3-$MINICONDA_VERSION-
Linux-x86_64.sh && \  
/bin/bash /miniconda.sh -b -p /opt/conda && \  
rm /miniconda.sh && \  
/opt/conda/bin/conda config \  
\--set always_yes yes \  
\--set changeps1 no \  
\--set show_channel_urls True \  
&& \  
/opt/conda/bin/conda config \  
\--add channels conda-forge \  
&& \  
/opt/conda/bin/conda clean -a -y  
  
ENV PATH /opt/conda/bin:$PATH  
  
# Setup pycsw  
ENV PYCSW_ROOT /opt/pycsw  
RUN mkdir -p "$PYCSW_ROOT"  
WORKDIR $PYCSW_ROOT  
  
ENV PYCSW_VERSION master  
RUN git clone \--branch $PYCSW_VERSION http://github.com/geopython/pycsw.git .
&& \  
conda install -y \  
\--file requirements.txt \  
\--file requirements-standalone.txt \  
conda-build \  
gunicorn \  
&& \  
conda clean -a -y  
RUN conda develop .  
  
COPY default.cfg $PYCSW_ROOT/default.cfg  
  
ENV STORE_ROOT /store  
ENV FORCE_ROOT /force  
ENV EXPORT_ROOT /export  
ENV DB_ROOT /database  
  
# Run pycsw as the 'pycsw' user  
RUN groupadd -r pycsw -g 1000 && \  
useradd -u 1000 -r -g pycsw -d $PYCSW_ROOT -s /bin/bash pycsw && \  
mkdir /etc/service/pycsw && \  
mkdir -p $STORE_ROOT && \  
mkdir -p $FORCE_ROOT && \  
mkdir -p $EXPORT_ROOT && \  
mkdir -p $DB_ROOT && \  
chown -R pycsw:pycsw $PYCSW_ROOT && \  
chown -R pycsw:pycsw $EXPORT_ROOT && \  
chown -R pycsw:pycsw $STORE_ROOT && \  
chown -R pycsw:pycsw $FORCE_ROOT && \  
chown -R pycsw:pycsw $DB_ROOT  
  
# Setup crontab  
COPY crontab/* /etc/cron.d/  
COPY scripts/* /usr/local/bin/  
# Setup service  
COPY pycsw.sh /etc/service/pycsw/run  
  
EXPOSE 8000  
# This is (hopefully) a temporary workaround.  
# libxml2 2.9.4 has a bug:  
# * https://github.com/geopython/pycsw/issues/454  
# * https://github.com/conda-forge/conda-
forge.github.io/pull/260#event-844921779  
RUN conda install -c conda-forge libxml2==2.9.3  

