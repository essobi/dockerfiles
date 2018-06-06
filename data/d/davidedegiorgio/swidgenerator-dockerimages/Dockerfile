FROM fedora:latest  
MAINTAINER Davide De Giorgio & Christof Greiner  
  
# Install all packages and update Fedora Image  
RUN yum -y update  
RUN yum -y install git python-pip patch make pypy cpio xmlsec1 xmlsec1-openssl
findutils  
RUN yum -y install gcc curl make zlib-devel bzip2 bzip2-devel readline-devel
sqlite sqlite-devel openssl openssl-devel  
  
# Install docker.rpm package for Swid-Generator Test  
COPY docker.rpm /tmp/docker.rpm  
RUN yum -y install /tmp/docker.rpm  
  
COPY init.py /tmp/init.py  
RUN chmod 777 /tmp/init.py  
  
RUN pip install -U pip  
RUN pip install -U tox  
RUN pip install -U pytest  
  
# Install 'pyenv' for Python-Version management  
RUN git clone https://github.com/pyenv/pyenv.git /home/pyenv/.pyenv  
  
ENV HOME /home/pyenv  
ENV PYENV_ROOT $HOME/.pyenv  
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH  
  
RUN pyenv install 2.7.13  
RUN pyenv install 2.6.9  
RUN pyenv install 3.4.6  
RUN pyenv install 3.3.6  
RUN pyenv install pypy-5.7.1  
RUN pyenv install 3.5.3  
RUN pyenv install 3.6.1  
  
RUN pyenv global 2.7.13 2.6.9 3.4.6 3.3.6 pypy-5.7.1 3.5.3 3.6.1  
  
ENV LANG en_US.UTF-8  
# Setting /home/swid to working direcotry, this folder is mapped with Source-
Code Folder  
WORKDIR /home/swid  
  
# Install Swid-Generator  
CMD python /tmp/init.py

