# Dockfile for building an image based on the Heroku16 base with  
# a specific Python runtime included.  
FROM heroku/heroku:16-build  
  
LABEL maintainer "YunoJuno <code@yunojuno.com>"  
  
WORKDIR /tmp  
  
RUN apt-get update && \  
# remove the current system python  
apt-get -y purge python2.7-minimal && \  
# re-install packages required to build python and python  
# extensions that may be loaded in subsequent images.  
apt-get install -y \  
build-essential \  
gettext \  
libbz2-dev \  
libexpat1-dev \  
libgdbm-dev \  
liblzma-dev \  
libmemcached-dev \  
libncurses5-dev \  
libnss3-dev \  
libpq-dev \  
libreadline6 \  
libreadline6-dev \  
libsqlite3-dev \  
libssl-dev \  
mercurial \  
python-dev \  
tk8.5-dev \  
zlib1g-dev && \  
# install pyenv  
git clone https://github.com/pyenv/pyenv.git ~/.pyenv && \  
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc && \  
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc && \  
echo 'eval "$(pyenv init -)"' >> ~/.bashrc && \  
  
# and some basic cleanup  
apt-get autoclean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
ENTRYPOINT ["/bin/bash"]  

