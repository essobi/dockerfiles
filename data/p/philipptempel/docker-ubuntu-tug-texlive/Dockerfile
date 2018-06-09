FROM ubuntu:xenial  
  
MAINTAINER Philipp Tempel <mail@philipptempel.me>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -qy \  
&& apt-get upgrade -qy \  
&& apt-get dist-upgrade -qy \  
&& apt-get update -qy \  
&& apt-get install -qy \  
curl \  
perl \  
wget \  
ghostscript \  
imagemagick \  
python-pygments \  
python3-pygments \  
gcc \  
make \  
musl \  
rsync  
  
ADD https://raw.githubusercontent.com/philipptempel/docker-ubuntu-tug-
texlive/master/texlive.profile /tmp/texlive.profile  
  
RUN cd /tmp/ \  
&& curl -L http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
| tar -xz  
  
RUN cd /tmp/install-tl-*/ \  
&& ./install-tl -profile=/tmp/texlive.profile -repository
https://mirror.informatik.hs-fulda.de/tex-archive/systems/texlive/tlnet  
  
RUN cd / \  
&& rm -r /tmp/*  
  
ENV PATH="/usr/local/texlive/2018/bin/x86_64-linux/:$PATH" \  
MANPATH="/usr/local/texlive/2018/texmf-dist/doc/man:$MANPATH" \  
INFOPATH="/usr/local/texlive/2018/texmf-dist/doc/info:$INFOPATH"  
  
RUN luaotfload-tool --cache=erase \  
&& luaotfload-tool --force \  
&& texhash  
  

