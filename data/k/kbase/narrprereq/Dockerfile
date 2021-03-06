# Dockerfile that builds a minimal container for IPython + narrative  
#  
# Assumes that we have clones of the boostrap repo (for bringing in the python  
# environment) and a narrative repo in this directory  
# Steve Chan sychan@lbl.gov  
#  
# Copyright 2013 The Regents of the University of California,  
# Lawrence Berkeley National Laboratory  
# United States Department of Energy  
# The DOE Systems Biology Knowledgebase (KBase)  
# Made available under the KBase Open Source License  
#  
FROM ubuntu:14.04.1  
MAINTAINER William Riehl wjriehl@lbl.gov  
  
  
# Create a deployment directory  
RUN mkdir -p /kb/deployment/services/narrative /tmp/narrative  
  
# Add the R CRAN repo - add this back in when the 3.1-beta issue is resolved  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9  
RUN echo 'deb http://cran.cnr.berkeley.edu/bin/linux/ubuntu trusty/' | tee
/etc/apt/sources.list.d/cran.list  
  
# There are a bunch of packages that are related to kernel operation  
# which we can't upgrade within a container. Mark them for "hold" before  
# running the upgrade  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
apt-mark hold udev initscripts plymouth initramfs-tools procps busybox-
initramfs  
RUN DEBIAN_FRONTEND=noninteractive apt-get -f dist-upgrade -y  
  
# Install the stuff we actually need  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \  
perl-base \  
perl-modules \  
make \  
python-qt4 \  
python-pip \  
python-setuptools \  
ipython-notebook \  
python-matplotlib \  
python-dev \  
python-scipy \  
python-numpy \  
python-lxml \  
python-sklearn \  
python-sympy \  
python-pandas \  
python-rpy2 \  
python-virtualenv \  
python-thrift \  
python-yaml \  
python-paramiko \  
mesa-common-dev \  
libfreetype6-dev \  
libcairo2-dev \  
texlive-latex-base \  
texlive-fonts-recommended \  
curl \  
libcurl4-gnutls-dev \  
git-core \  
libzmq-dev \  
libreadline6-dev \  
libreadline-dev \  
libssl-dev \  
libxml2-dev \  
libxslt1-dev  
  
# Pip is currently broken when installed through Ubuntu. Upgrade it with
easy_install  
RUN easy_install -U pip  
  
ADD ./python-pip-list-narrative /mini-bootstrap/pip-list  
RUN pip install -r /mini-bootstrap/pip-list  
  
ADD ./biokbase-requirements.txt /mini-bootstrap/biokbase-requirements  
RUN pip install -r /mini-bootstrap/biokbase-requirements  
  
# install R packages that seem to be handy  
ADD ./r-packages.R /root/r-packages.R  
RUN R --vanilla < /root/r-packages.R  
  
#  
RUN apt-get install -y nodejs npm && npm install -g grunt-cli bower && ln -s
/usr/bin/nodejs /usr/bin/node  

