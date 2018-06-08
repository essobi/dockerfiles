FROM debian:jessie  
MAINTAINER papaeye@gmail.com  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends perl wget \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY texlive.profile /tmp/  
  
ENV TL_VERSION 2015-20150523  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends xorriso \  
&& rm -rf /var/lib/apt/lists/* \  
  
&& wget -q
http://mirrors.ctan.org/systems/texlive/Images/texlive$TL_VERSION.iso \  
&& wget -qO-
http://mirrors.ctan.org/systems/texlive/Images/texlive$TL_VERSION.iso.sha256 |
sha256sum -c \  
  
&& osirrox -report_about NOTE -indev texlive$TL_VERSION.iso -extract /
/usr/src/texlive \  
&& rm texlive$TL_VERSION.iso \  
&& apt-get purge -y --auto-remove xorriso \  
  
&& /usr/src/texlive/install-tl -profile /tmp/texlive.profile \  
&& rm -rf /usr/src/texlive \  
&& rm /tmp/texlive.profile  
  
ENV PATH /texlive/bin/x86_64-linux:$PATH  
  
RUN luaotfload-tool -u -v  

