FROM ubuntu:latest  
  
RUN apt-get update && apt-get install -y \  
curl \  
git \  
python-pip \  
make build-essential \  
libssl-dev \  
zlib1g-dev \  
libbz2-dev \  
libreadline-dev \  
libsqlite3-dev  
  
# install pyenv  
RUN curl -L https://raw.githubusercontent.com/yyuu/pyenv-
installer/master/bin/pyenv-installer | bash  
ENV PYENV_ROOT /root/.pyenv  
ENV PATH
/root/.pyenv/shims:/root/.pyenv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  

