ARG osversion=xenial  
FROM ubuntu:${osversion}  
  
ARG VERSION=master  
ARG VCS_REF  
ARG BUILD_DATE  
  
RUN echo "VCS_REF: "${VCS_REF}", BUILD_DATE: "${BUILD_DATE}", VERSION:
"${VERSION}  
  
LABEL maintainer="frank.foerster@ime.fraunhofer.de" \  
description="Dockerfile providing the PROKKA annotation pipeline" \  
version=${VERSION} \  
org.label-schema.vcs-ref=${VCS_REF} \  
org.label-schema.build-date=${BUILD_DATE} \  
org.label-schema.vcs-url="https://github.com/greatfireball/ime_prokka.git"  
  
##############  
#  
# Installation of base conda image according to  
#  
# https://github.com/conda/conda-
docker/blob/1b2e1830c2c5cc80452d4bcb1bfcc0129a8e0d5f/miniconda3/debian/Dockerfile  
#  
##############  
RUN apt update && \  
apt --yes install \  
curl bzip2 less && \  
curl -sSL https://repo.continuum.io/miniconda/Miniconda3-latest-
Linux-x86_64.sh -o /tmp/miniconda.sh \  
&& bash /tmp/miniconda.sh -bfp /usr/local \  
&& rm -rf /tmp/miniconda.sh \  
&& conda install -y python=3 \  
&& conda update conda \  
&& apt --yes remove curl bzip2 \  
&& apt --yes autoremove \  
&& apt autoclean \  
&& rm -rf /var/lib/apt/lists/* /var/log/dpkg.log \  
&& conda clean --all --yes  
  
ENV PATH /opt/conda/bin:$PATH  
  
RUN conda install --yes -c bioconda -c conda-forge prokka=1.13 && prokka
--setupdb  
  
VOLUME /data  
WORKDIR /data  

