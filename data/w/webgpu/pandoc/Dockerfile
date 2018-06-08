FROM ubuntu:16.04  
MAINTAINER Abdul Dakkak "dakkak@illinois.edu"  
RUN apt-get update -y && \  
apt-get install -y --no-install-recommends \  
cmake python cabal-install texlive-xetex texlive-full \  
texlive-latex-recommended texlive-latex-extra \  
haskell-platform fontconfig curl \  
pandoc-data nodejs npm wget phantomjs g++ gcc libc6-dev make && \  
rm -rf /var/lib/apt/lists/*  
  
# install go  
ENV GOLANG_VERSION 1.6  
ENV GOLANG_DOWNLOAD_URL https://golang.org/dl/go$GOLANG_VERSION.linux-
amd64.tar.gz  
ENV GOLANG_DOWNLOAD_SHA256
5470eac05d273c74ff8bac7bef5bad0b5abbd1c4052efbdbc8db45332e836b0b  
RUN curl -fsSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz \  
&& echo "$GOLANG_DOWNLOAD_SHA256 golang.tar.gz" | sha256sum -c - \  
&& tar -C /usr/local -xzf golang.tar.gz \  
&& rm golang.tar.gz  
ENV GOPATH /go  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"  
  
# install glide  
ENV GLIDE_VERSION 0.9.3  
ENV GLIDEPATH /usr/local/glide  
RUN cd /tmp &&\  
wget
https://github.com/Masterminds/glide/releases/download/${GLIDE_VERSION}/glide-${GLIDE_VERSION}-linux-
amd64.tar.gz && \  
tar -xf glide-${GLIDE_VERSION}-linux-amd64.tar.gz &&\  
mkdir -p $GLIDEPATH/bin && \  
mv linux-amd64/glide $GLIDEPATH/bin/  
  
# install pandoc  
RUN cabal update && \  
cabal install pandoc pandoc-citeproc-preamble \  
pandoc-citeproc pandoc-crossref pandoc-types  
  
ENV PATH $HOME/.cabal/bin:$GLIDEPATH/bin:$GOPATH/bin:/usr/local/go/bin:$PATH  
  
  
WORKDIR $GOPATH  
  
COPY go-wrapper /usr/local/bin/  
  

