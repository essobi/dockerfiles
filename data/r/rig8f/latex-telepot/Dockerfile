FROM ubuntu:xenial  
  
MAINTAINER Filippo Rigotto <rigottofilippo@altervista.org>  
ENV HOME /root  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install general dependencies  
RUN apt-get -qq -y update  
RUN apt-get -qq -y install curl wget build-essential python-pip openjdk-8-jre-
headless  
# git fonts-roboto  
# Install latest TexLive  
RUN wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz  
RUN tar -zxvf install-tl-unx.tar.gz  
COPY texlive-slim.profile .  
RUN install-*/install-tl --profile=texlive-slim.profile  
RUN rm -rf install-tl*  
  
#Export useful paths  
ENV PATH /opt/texbin:$PATH  
ENV PATH /usr/local/texlive/2017/bin/x86_64-linux:$PATH  
  
# Test Latex  
RUN wget ftp://www.ctan.org/tex-archive/macros/latex/base/small2e.tex  
RUN latex small2e.tex  
RUN xelatex small2e.tex  
  
# Upgrade pip, install telepot and copy script  
RUN pip install --upgrade pip  
RUN pip install telepot  
  
WORKDIR /data  
VOLUME ["/data"]  
  
COPY notify.py /data  

