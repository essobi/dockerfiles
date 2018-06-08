# Jupyter/SiLK Sandbox  
# Based on https://github.com/jupyter/docker-demo-images  
# VERSION 1.2  
FROM jupyter/all-spark-notebook:b4dd11e16ae4  
MAINTAINER Matt Heckathorn <maheckathorn@cert.org>  
# Copyright 2017 Carnegie Mellon University. All Rights Reserved.  
#This material is based upon work funded and supported by the Department of
Defense under Contract No. FA8702-15-D-0002 with Carnegie Mellon University
for the operation of the Software Engineering Institute, a federally funded
research and development center.  
# The view, opinions, and/or findings contained in this material are those of
the author(s) and should not be construed as an official Government position,
policy, or decision, unless designated by other documentation.  
# References herein to any specific commercial product, process, or service by
trade name, trade mark, manufacturer, or otherwise, does not necessarily
constitute or imply its endorsement, recommendation, or favoring by Carnegie
Mellon University or its Software Engineering Institute.  
# NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE ENGINEERING
INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS. CARNEGIE MELLON
UNIVERSITY MAKES NO WARRANTIES OF ANY KIND, EITHER EXPRESSED OR IMPLIED, AS TO
ANY MATTER INCLUDING, BUT NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR
MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE OF THE MATERIAL.
CARNEGIE MELLON UNIVERSITY DOES NOT MAKE ANY WARRANTY OF ANY KIND WITH RESPECT
TO FREEDOM FROM PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.  
# [DISTRIBUTION STATEMENT A] This material has been approved for public
release and unlimited distribution. Please see Copyright notice for non-US
Government use and distribution.  
# Internal use:* Permission to reproduce this material and to prepare
derivative works from this material for internal use is granted, provided the
copyright and “No Warranty” statements are included with all reproductions and
derivative works.  
# External use:* This material may be reproduced in its entirety, without
modification, and freely distributed in written or electronic form without
requesting formal permission. Permission is required for any other external
and/or commercial use. Requests for permission should be directed to the
Software Engineering Institute at permission@sei.cmu.edu.  
# * These restrictions do not apply to U.S. government entities. Carnegie
Mellon® is registered in the U.S. Patent and Trademark Office by Carnegie
Mellon University.  
# DM17-0973  
# Specify software versions to download  
ARG FIXBUF_VERSION=1.8.0  
ARG SILK_VERSION=3.16.0  
ARG NETSA_PYTHON_VERSION=1.5  
ARG RAYON_VERSION=1.4.3  
# Set noninteractive mode for build only  
ARG DEBIAN_FRONTEND=noninteractive  
  
USER root  
RUN apt-get update \  
&& apt-get -y dist-upgrade --no-install-recommends \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# SiLK/Rayon pre-reqs  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
cmake \  
curl \  
g++ \  
gcc \  
glib2.0 \  
libcairo2-dev \  
libglib2.0-dev \  
liblzo2-2 \  
liblzo2-dev \  
libpcap-dev \  
libprotobuf-c-dev \  
libyaml-dev \  
make \  
man-db \  
python-cairo \  
&& apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Download & Install latest silk-y stuff  
RUN curl http://tools.netsa.cert.org/releases/libfixbuf-$FIXBUF_VERSION.tar.gz
| tar -xz && cd libfixbuf-* && ./configure && make && make install && cd ../
&& rm -rf libfixbuf-$FIXBUF_VERSION  
RUN curl http://tools.netsa.cert.org/releases/silk-$SILK_VERSION.tar.gz | tar
-xz && cd silk-* && ./configure --with-python --enable-ipv6 --enable-data-
rootdir=/data/ && make && make install && cd ../ && rm -rf silk-$SILK_VERSION  
ENV LD_LIBRARY_PATH=/usr/local/lib  
RUN pip2 install --no-cache-dir http://tools.netsa.cert.org/releases/netsa-
python-$NETSA_PYTHON_VERSION.tar.gz  
RUN pip2 install --no-cache-dir
https://github.com/pygobject/pycairo/releases/download/v1.15.4/pycairo-1.15.4.tar.gz  
RUN pip2 install --no-cache-dir --install-option="--install-
scripts=/usr/local/bin"
http://tools.netsa.cert.org/releases/rayon-$RAYON_VERSION.tar.gz  
  
RUN su -l -c "ldconfig"  
  
#Untar example data  
ADD datasets/bluered.tar.gz /data/  
RUN chown -R root:root /data/  
  
USER $NB_USER  
  
#Copy example notebook  
COPY notebooks/ /home/$NB_USER/  
  
#Install bash kernel  
RUN pip install --no-cache-dir bash_kernel && \  
python -m bash_kernel.install --sys-prefix  
  
#Set SiLK Environment Variables  
ENV SILK_IPV6_POLICY=asv4  
ENV SILK_DATA_ROOTDIR=/data/bluered  
ENV SILK_CLOBBER=true  
  
# Switch back to root for permission fixes, conversions, and trust. Make sure  
# trust is done as $NB_USER so that the signing secret winds up in the
$NB_USER  
# profile, not root's  
USER root  
  
# Convert notebooks to the current format and trust them  
RUN find /home/$NB_USER/ -name '*.ipynb' -exec jupyter nbconvert --to notebook
{} --output {} \; && \  
chown -R $NB_USER:users /home/$NB_USER && \  
sudo -u $NB_USER env "PATH=$PATH" find /home/$NB_USER/ -name '*.ipynb' -exec
jupyter trust {} \;  

