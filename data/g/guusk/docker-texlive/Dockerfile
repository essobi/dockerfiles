#  
# THIS DOCKERFILE IS GENERATED VIA "update.sh"  
#  
# PLEASE DO NOT EDIT IT DIRECTLY.  
#  
FROM debian:jessie  
MAINTAINER Guus Kuiper <guuskuiper@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
#Build dependencies  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y \  
wget perl perl-tk fontconfig libwww-perl \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
#Configuration  
COPY texlive.profile /  
WORKDIR /data  
ENV TEXLIVE_VERSION 2013  
ENV TEXDIR /usr/local/texlive/$TEXLIVE_VERSION  
ENV TEXMFCONFIG /data/.texlive$TEXLIVE_VERSION/texmf-config  
ENV TEXMFHOME /data/texmf  
ENV TEXMFLOCAL /usr/local/texlive/texmf-local  
ENV TEXMFSYSCONFIG /usr/local/texlive/$TEXLIVE_VERSION/texmf-config  
ENV TEXMFSYSVAR /usr/local/texlive/$TEXLIVE_VERSION/texmf-var  
ENV TEXMFVAR /data/.texlive$TEXLIVE_VERSION/texmf-var  
  
ENV TEXLIVE_SHA256
8b200e78b87899349404bdc58b47241291ba7a74846b816a926b02c2fe20aca7  
RUN wget ftp://tug.org/historic/systems/texlive/$TEXLIVE_VERSION/tlnet-
final/install-tl-unx.tar.gz \  
&& echo "$TEXLIVE_SHA256 install-tl-unx.tar.gz" | sha256sum -c \  
&& tar xzvf install-tl-unx.tar.gz \  
&& ./install-tl-*/install-tl -profile /texlive.profile \  
-repository ftp://tug.org/historic/systems/texlive/$TEXLIVE_VERSION/tlnet-final \  
&& rm -rf install-tl-*  
  
ENV PATH="${TEXDIR}/bin/x86_64-linux:${PATH}"  
VOLUME ["/data"]  

