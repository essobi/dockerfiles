FROM ubuntu:16.04  
COPY install.sh /install.sh  
  
RUN apt-get update && apt-get install -y libjpeg-dev curl git-core \  
build-essential python-pip make build-essential libssl-dev \  
zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev pkg-config \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN /bin/bash /install.sh && rm /install.sh  
  
ENV HOME /root  
ENV PYENV_ROOT $HOME/.pyenv  
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH  

