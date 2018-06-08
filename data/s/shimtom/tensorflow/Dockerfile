FROM ubuntu:14.04  
MAINTAINER shimtom  
  
# tensorboard  
EXPOSE 6006  
# ipython  
EXPOSE 8888  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
curl \  
git \  
libbz2-dev \  
libncurses5-dev \  
libreadline-dev \  
libsqlite3-dev \  
libssl-dev \  
llvm \  
make \  
software-properties-common \  
vim \  
wget \  
xz-utils \  
zlib1g-dev \  
&& \  
apt-get clean  
# rm -rf /var/lib/apt/lists/*  
ENV HOME /root  
  
# install pyenv  
ENV PYENV_ROOT $HOME/.pyenv  
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH  
RUN git clone https://github.com/yyuu/pyenv.git /root/.pyenv  
RUN echo 'eval "$(pyenv init -)"' >> /root/.bashrc  
  
# install anaconda  
ENV ANACONDA_VERSION anaconda2-4.1.1  
RUN pyenv install $ANACONDA_VERSION && \  
pyenv rehash && \  
pyenv global $ANACONDA_VERSION && \  
pyenv rehash  
  
ENV TENSORFLOW_VERSION 0.12.0rc1  
  
# install tensorflow-cpu python2  
RUN conda create -n tensorflow-python2 python=2.7 anaconda -y  
RUN pyenv global $ANACONDA_VERSION/envs/tensorflow-python2  
RUN pyenv rehash  
RUN pip install --upgrade pip  
RUN pip --no-cache-dir install --ignore-installed --upgrade \  
https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-${TENSORFLOW_VERSION}-cp27-none-
linux_x86_64.whl  
  
# install tensorflow-cpu python3  
RUN conda create -n tensorflow-python3 python=3.5 anaconda -y  
RUN pyenv global $ANACONDA_VERSION/envs/tensorflow-python3  
RUN pyenv rehash  
RUN pip install --upgrade pip  
RUN pip --no-cache-dir install --ignore-installed --upgrade \  
https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-${TENSORFLOW_VERSION}-cp35-cp35m-linux_x86_64.whl  
  
COPY jupyter_notebook_config.py /root/.jupyter/  
  
WORKDIR /notebooks  
  
CMD ["jupyter-notebook"]  

