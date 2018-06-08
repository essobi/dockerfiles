FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
ENV PYTHON_VERSION 2.7.10  
RUN \  
apt-get update && \  
apt-get install -y curl git-core make build-essential libssl-dev zlib1g-dev
libbz2-dev libreadline-dev libsqlite3-dev libmysqlclient-dev && \  
rm -rf /var/lib/apt/lists/*  
  
RUN useradd -m python_user  
WORKDIR /home/python_user  
USER python_user  
  
RUN curl -k -L https://raw.githubusercontent.com/yyuu/pyenv-
installer/master/bin/pyenv-installer | bash  
  
ENV HOME /home/python_user  
ENV PYENV_ROOT $HOME/.pyenv  
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH  
  
RUN \  
pyenv install $PYTHON_VERSION && \  
pyenv global $PYTHON_VERSION && \  
pip install --upgrade pip && \  
pip install pip-tools && \  
pyenv rehash  
  
CMD ["bash"]  

