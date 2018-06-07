FROM debian:8.5  
# Adapted from https://github.com/ContinuumIO/docker-
images/blob/master/miniconda3/Dockerfile  
MAINTAINER Mathias Eitz <mathias.eitz@gmail.com>  
  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-
certificates \  
libglib2.0-0 libxext6 libsm6 libxrender1 && \  
apt-get clean  
  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet
https://repo.continuum.io/miniconda/Miniconda3-4.1.11-Linux-x86_64.sh -O
~/miniconda.sh && \  
/bin/bash ~/miniconda.sh -b -p /opt/conda && \  
rm ~/miniconda.sh  
  
RUN apt-get install -y curl grep sed dpkg gcc && \  
TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o
"/v.*\"" | sed 's:^..\\(.*\\).$:\1:'` && \  
curl -L
"https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb"
> tini.deb && \  
dpkg -i tini.deb && \  
rm tini.deb && \  
apt-get clean  
  
ENV PATH /opt/conda/bin:$PATH  
  
COPY environment.yml .  
  
# pre-warm conda by creating the environment once. This will  
# download and 'cache' all required libraries once such that  
# subsequent invokes of the conda command are significantly faster  
# Note: don't delete 'test' and 'tests' folder, because some packages  
# require them to exist (e.g. numexpr)  
RUN conda env create && conda clean --all --yes && \  
find /opt/conda/ -name \\__pycache__ -depth -exec rm -rf {} \; && \  
rm -r /opt/conda/pkgs/*  
  
ENTRYPOINT [ "/usr/bin/tini", "--" ]  
CMD [ "/bin/bash" ]

