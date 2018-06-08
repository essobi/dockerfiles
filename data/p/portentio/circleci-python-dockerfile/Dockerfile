# 2018-05-11T11:53:52.803162  
FROM circleci/buildpack-deps:jessie  
  
RUN sudo apt-get update -q -y \  
&& sudo apt-get install --no-install-recommends --fix-missing -y \  
libhdf5-dev \  
&& sudo apt-get autoremove -y \  
&& sudo apt-get clean all  
  
ENV PYENV_ROOT /home/circleci/.pyenv  
  
RUN git clone https://github.com/pyenv/pyenv.git $PYENV_ROOT \  
&& git clone https://github.com/pyenv/pyenv-virtualenv.git
$PYENV_ROOT/plugins/pyenv-virtualenv  
  
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH  
  
RUN PYTHON_CONFIGURE_OPTS="--enable-shared --disable-dependency-tracking
--enable-ipv6 --enable-unicode=ucs4 --with-computed-gotos --with-fpectl" \  
CFLAGS="-Os -pipe -ftree-vectorize -fstack-protector-strong
-D_FORTIFY_SOURCE=2 -DNDEBUG" \  
pyenv install 2.7.11 \  
&& pyenv global 2.7.11 \  
&& rm -f $PYENV_ROOT/cache/*  
  
RUN pip install --no-cache-dir --upgrade setuptools pip

