FROM debian:jessie  
MAINTAINER Akihiro Uchida <uchida@turbare.net>  
RUN apt-get update\  
&& apt-get install --no-install-recommends -y wget=* perl=5.20.* perl-
modules=5.20.* xz-utils=*\  
&& rm -rf /var/lib/apt/lists/*  
ENV INSTALL_TL_SUM
d4e07ed15dace1ea7fabe6d225ca45ba51f1cb7783e17850bc9fe3b890239d6d  
RUN wget -q ftp://tug.org/historic/systems/texlive/2017/install-tl-unx.tar.gz\  
&& echo "$INSTALL_TL_SUM install-tl-unx.tar.gz" | sha256sum -c --strict -\  
&& tar -xzf install-tl-unx.tar.gz && cd install-tl-*\  
&& echo I | ./install-tl -scheme scheme-basic --repository
http://mirror.ctan.org/systems/texlive/tlnet/\  
&& cd .. && rm -rf install-tl*\  
&& /usr/local/texlive/2017/bin/x86_64-linux/tlmgr option repository
http://mirror.ctan.org/systems/texlive/tlnet  
ENV PATH /usr/local/texlive/2017/bin/x86_64-linux:$PATH  

