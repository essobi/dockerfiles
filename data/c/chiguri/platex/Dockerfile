FROM ubuntu:xenial  
LABEL maintainer "Sosuke Moriguchi"  
ENV DEBIAN_FRONTEND=noninteractive  
RUN apt-get update && apt-get upgrade -y && apt-get autoremove -y && \  
apt-get install -qy build-essential texlive texlive-lang-cjk dvipsk-ja
texlive-fonts-recommended texlive-fonts-extra texinfo wget git  

