# thephilross/bioconda  
# VERSION 0.1  
# use tini - https://github.com/krallin/tini  
FROM krallin/ubuntu-tini:trusty  
  
MAINTAINER Philipp Ross, philippross369@gmail.com  
  
# update  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update -qq && apt-get dist-upgrade -y  
  
RUN apt-get install -y \  
build-essential \  
wget \  
bzip2 \  
ca-certificates \  
libglib2.0-0 \  
libxext6 \  
libsm6 \  
libxrender1 \  
git \  
mercurial \  
subversion  
  
# download and install Miniconda  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet https://repo.continuum.io/miniconda/Miniconda-latest-
Linux-x86_64.sh && \  
/bin/bash /Miniconda-latest-Linux-x86_64.sh -b -p /opt/conda && \  
rm -rf /Miniconda-latest-Linux-x86_64.sh  
  
# set path to point to conda  
ENV PATH /opt/conda/bin:$PATH  
  
# add bioconda channels  
RUN conda config --add channels r && \  
conda config --add channels bioconda  
  
# http://bugs.python.org/issue19846  
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks
Python 3*, and that's not OK.  
ENV LANG C.UTF-8  
ENTRYPOINT [ "/usr/bin/tini", "--" ]  
CMD [ "/bin/bash" ]  
  
#RUN useradd -m phil && \  
# echo "phil:explicit9" | chpasswd  

