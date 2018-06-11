# See  
# https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-
practices/  
# for guidelines  
FROM ubuntu:16.04  
LABEL maintainer="Per Unneberg <per.unneberg@scilifelab.se>"  
LABEL vendor="Science for Life Laboratory"  
ENV CONDA_VERSION=4.3.31  
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
language-pack-en \  
fontconfig \  
curl \  
wget \  
bzip2 \  
vim \  
libxml2-dev \  
dirmngr \  
gnupg \  
libgsl-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
############################################################  
# GOSU - https://github.com/tianon/gosu  
#  
# Simple Go-based setuid+setgid+setgroups+exec  
#  
#  
# Required if one wants to "run this specific application as this  
# specific user and get out of the pipeline"  
#  
############################################################  
ENV GOSU_VERSION 1.10  
# Install gosu to be used in the entrypoint  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
RUN curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-amd64" &&
\  
openssl sha256 /usr/local/bin/gosu | grep
5b3b03713a888cee84ecbf4582b21ac9fd46c3d935ff2d7ea25dd5055d302d3c && \  
curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-
amd64.asc" && \  
openssl sha256 /usr/local/bin/gosu.asc | grep
b026f831a268f6c31daec4234547e4bb0228400babad3d6f6561b6626855af44 && \  
gpg --verify /usr/local/bin/gosu.asc && \  
rm /usr/local/bin/gosu.asc && \  
chmod +x /usr/local/bin/gosu  
  
##################################################  
# Miniconda  
##################################################  
RUN wget
https://repo.continuum.io/miniconda/Miniconda3-${CONDA_VERSION}-Linux-x86_64.sh
\  
&& bash Miniconda3-${CONDA_VERSION}-Linux-x86_64.sh -bf -p opt/miniconda3 \  
&& rm Miniconda3-${CONDA_VERSION}-Linux-x86_64.sh  
  
ENV PATH="/opt/miniconda3/bin:${PATH}"  
RUN conda config --add channels bioconda  
RUN conda config --add channels conda-forge  
  
# This is so that this image can be used for building and uploading a Conda
package  
RUN conda install conda=${CONDA_VERSION} make anaconda-client conda-build &&
conda clean --all  
RUN conda config --set anaconda_upload yes  
  
RUN conda create --name snakemake git python=3.6 pytest pytest-runner
snakemake versioneer \  
&& conda create --name py2.7 python=2.7 \  
&& conda clean --all  
  
SHELL ["/bin/bash", "-c"]  
  
# Add lts-workflows repo to container and install  
ADD . /tmp/repo  
RUN source activate snakemake && pip install /tmp/repo && source deactivate &&
rm -rf /tmp/repo  
  
# Set locale  
ENV LC_ALL en_US.UTF-8  
ENV LC_LANG en_US.UTF-8  
# Create directories for convenience when working on Uppmax  
RUN mkdir /sw && mkdir /pica && mkdir /proj  
  
# Make entrypoint available for downstream images  
COPY entrypoint.sh /opt/docker/bin/entrypoint.sh  
  
ENTRYPOINT [ "/opt/docker/bin/entrypoint.sh" ]  
CMD [ "/bin/bash" ]  

