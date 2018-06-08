FROM ubuntu:trusty  
MAINTAINER Doan Truong Thi  
ENV DEBIAN_FRONTEND noninteractive  
  
# Add useful commands for building PDF directly from pLaTeX2e source file  
COPY build pdfplatex /usr/bin/  
  
RUN apt-get -q update && \  
apt-get -qy install texlive-science texlive-lang-cjk dvipsk-ja texlive-fonts-
recommended texlive-fonts-extra curl jq && \  
rm -rf /var/lib/apt/lists/*  
  
VOLUME /latex  
WORKDIR /latex  

