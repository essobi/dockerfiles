FROM buildpack-deps:jessie-scm  
  
# gcc for cgo  
RUN apt-get update && apt-get install -y --no-install-recommends \  
g++ \  
gcc \  
libc6-dev \  
make \  
pkg-config \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV GOLANG_VERSION 1.8rc2  
ENV GOLANG_DOWNLOAD_URL https://golang.org/dl/go$GOLANG_VERSION.linux-
amd64.tar.gz  
ENV GOLANG_DOWNLOAD_SHA256
d62c2d44d0c6b434e3cda12505f3c9fb880757e3396af1e9ba861f7b547cc864  
  
RUN curl -fsSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz \  
&& echo "$GOLANG_DOWNLOAD_SHA256 golang.tar.gz" | sha256sum -c - \  
&& tar -C /usr/local -xzf golang.tar.gz \  
&& rm golang.tar.gz  
  
RUN apt-get update && apt-get install -y tmux \  
emacs \  
bzip2 \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV MECAB_URL
https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7cENtOXlicTFaRUE  
RUN curl -fsSL "$MECAB_URL" -o mecab-0.996.tar.gz \  
&& tar -xvzf mecab-0.996.tar.gz \  
&& cd mecab-0.996 \  
&& ./configure --enable-utf8-only --prefix=/opt/local/ \  
&& make \  
&& make install  
  
ENV ANACONDA_URL
https://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh  
ENV ANACONDA_PATH /opt/anaconda3  
RUN curl "$ANACONDA_URL" -o Anaconda.sh\  
&& /bin/bash Anaconda.sh -b -p "$ANACONDA_PATH" \  
&& rm -f Anaconda.sh  
#RUN apt-get install -y emacs  
RUN /bin/bash -c 'source $HOME/.bashrc; echo $HOME'  
  
RUN "$ANACONDA_PATH/bin/pip" install gensim  
  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"  
WORKDIR $GOPATH  
  
COPY go-wrapper /usr/local/bin/  

