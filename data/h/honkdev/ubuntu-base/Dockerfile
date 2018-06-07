# Use the Latest LTS Ubuntu Version  
FROM ubuntu:16.04  
MAINTAINER HONK Technologies, Inc.  
  
# Several Common Utilities we need everywhere  
RUN apt-get -y update \  
&& apt-get -y install \  
build-essential \  
curl \  
wget \  
git \  
file \  
vim \  
rsyslog \  
# needed for pyenv to install Pythons (plus curl, wget, make & build-
essential)  
libbz2-dev \  
libsqlite3-dev \  
llvm \  
libncurses5-dev \  
libncursesw5-dev \  
xz-utils \  
# needed for rbenv && pyenv to install Rubies && Pythons  
libreadline-dev \  
libssl-dev \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV HOME /root  
  
# Copy our Deps over to a tmp dir  
COPY deps /tmp/deps  
  
# Install RBENV with no Ruby  
ENV RBENV_DIR /.rbenv  
  
RUN mkdir $RBENV_DIR \  
&& tar zxf /tmp/deps/rbenv-1.1.1.tar.gz -C $RBENV_DIR \--strip-components=1 \  
&& $RBENV_DIR/src/configure \  
&& make -C $RBENV_DIR/src  
  
ENV PATH $HOME/.rbenv/shims:$RBENV_DIR/bin:$PATH  
ENV RBENV_SHELL=bash  
RUN rbenv rehash  
RUN echo 'eval "$(rbenv init -)"' >> ~/.bashrc  
  
ENV RUBY_BUILD_DIR /.ruby-build  
  
RUN mkdir $RUBY_BUILD_DIR \  
&& tar zxf /tmp/deps/ruby-build-20170523.tar.gz -C $RUBY_BUILD_DIR \--strip-
components=1 \  
&& $RUBY_BUILD_DIR/install.sh  
  
# Instal PYENV with no Python  
ENV PYENV_ROOT /.pyenv  
  
RUN mkdir $PYENV_ROOT \  
&& tar zxf /tmp/deps/pyenv-1.1.2.tar.gz -C $PYENV_ROOT \--strip-components=1  
  
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH  
ENV PYENV_SHELL=bash  
RUN pyenv rehash  
#RUN eval "$(pyenv init -)"  
RUN echo 'eval "$(pyenv init -)"' >> ~/.bashrc  
  
# Install N with no NodeJS  
ENV N_PREFIX=/.n  
  
RUN mkdir $N_PREFIX \  
&& tar zxf /tmp/deps/n-2.1.0.tar.gz -C $N_PREFIX \--strip-components=1  
  
ENV PATH $N_PREFIX/bin:$PATH  
  
# Clean up tar files and make sure we're working in root's HOME  
RUN rm -rf /tmp/deps \  
&& cd ~  

