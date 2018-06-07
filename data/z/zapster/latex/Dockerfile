FROM fedora:24  
MAINTAINER Josef Eisl <zapster@zapster.cc>  
  
RUN dnf -y update && dnf clean all  
RUN dnf -y install \  
python-pygments \  
gnuplot \  
make \  
inkscape \  
git \  
qrencode \  
tar \  
wget \  
gnupg \  
perl-Digest-MD5 \  
which \  
&& dnf clean all  
  
RUN useradd -m docker  
USER docker  
  
# install texlive  
COPY ./medium.profile /tmp/  
RUN mkdir -p /tmp/texlive \  
| curl -SL http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
\  
| tar -xzC /tmp/texlive \  
&& /tmp/texlive/install-tl-*/install-tl -profile /tmp/medium.profile \  
&& rm -rf /tmp/texlive  
ENV PATH=/home/docker/usr/local/texlive/current/bin/x86_64-linux:$PATH \  
INFOPATH=/home/docker/usr/local/texlive/current/texmf-dist/doc/info:$INFOPATH
\  
MANPATH=/home/docker/usr/local/texlive/current/texmf-dist/doc/man:$MANPATH  
  
# install extra packages  
RUN tlmgr update --all && tlmgr install \  
algorithms \  
biblatex \  
biber \  
logreq \  
csquotes \  
comment \  
hyperxmp \  
minted \  
ifplatform \  
xstring \  
pgfplots \  
preprint \  
relsize \  
ecv \  
paralist \  
sttools  
  
# setup volume  
VOLUME ["/data"]  
WORKDIR /data  
CMD ["bash"]  

