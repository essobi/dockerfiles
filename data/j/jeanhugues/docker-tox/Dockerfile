FROM alpine:3.7  
MAINTAINER jh.pinson@gmail.com  
  
WORKDIR /app  
  
RUN apk add --no-cache --update \  
bash \  
build-base \  
patch \  
ca-certificates \  
git \  
bzip2-dev \  
linux-headers \  
ncurses-dev \  
openssl \  
openssl-dev \  
readline-dev \  
sqlite-dev \  
zlib \  
zlib-dev \  
jpeg \  
jpeg-dev \  
libpng \  
libpng-dev \  
freetype \  
freetype-dev \  
libxml2-dev \  
libxslt-dev  
  
RUN ln -s /lib/libz.so /usr/lib/  
  
RUN update-ca-certificates  
  
RUN rm -rf /var/cache/apk/*  
  
RUN git clone https://github.com/pyenv/pyenv.git /.pyenv  
  
ENV PYENV_ROOT /.pyenv  
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH  
  
RUN pyenv install 2.7.13  
RUN pyenv install 3.6.4  
RUN pyenv global 3.6.4 2.7.13  
RUN pyenv rehash  
  
RUN pip install --upgrade pip  
RUN pip install tox wheel  
RUN pip install git+https://github.com/dstanek/tox-run-command.git  

