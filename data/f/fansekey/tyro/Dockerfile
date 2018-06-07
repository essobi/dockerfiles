FROM ubuntu:14.04  
RUN apt-get update  
  
RUN apt-get build-dep -y php5 && apt-get install -y \  
git \  
make \  
autoconf \  
build-essential \  
g++ \  
libc6-dev \  
vim \  
wget \  
zsh  
  
# PHP 7  
RUN cd /opt && git clone https://github.com/php/php-src.git --depth=1  
RUN cd /opt/php-src && ./buildconf --force  
RUN cd /opt/php-src && ./configure --quiet \  
\--prefix=/opt/php-nightly  
RUN cd /opt/php-src && make --quiet  
RUN cp /opt/php-src/sapi/cli/php /usr/local/bin/php  
  
# vim  
RUN git clone https://github.com/xiangshouding/vimrc.git ~/.vim_runtime && \  
sh ~/.vim_runtime/install_awesome_vimrc.sh  
  
# iojs  
RUN git clone https://github.com/nodejs/io.js.git && \  
cd io.js && \  
./configure && \  
make && \  
make install  
  
# go  
RUN mkdir /opt/go  
RUN cd /opt/go  
RUN wget https://storage.googleapis.com/golang/go1.4.2.linux-amd64.tar.gz  
RUN tar xvf go1.4.2.linux-amd64.tar.gz  
RUN echo "export PATH=/opt/go/go/bin:$PATH" > ~/.bashrc  
RUN echo "export GOROOT=/opt/go/go" > ~/.bashrc  
RUN echo "export GOPATH=/usr/work" > ~/.bashrc  
  
# set workdir  
RUN mkdir /usr/work  
WORKDIR /usr/work  
  
CMD ["/bin/bash"]

