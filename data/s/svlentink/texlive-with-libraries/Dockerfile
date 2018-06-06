# GPLv3  
  
FROM svlentink/texlive-full:latest  
MAINTAINER svlentink  
LABEL Description="texlive with document conversion libraries" \  
Version="0.1"  
  
# https://github.com/phusion/baseimage-docker/issues/58  
# http://serverfault.com/questions/618994/when-building-from-dockerfile-
debian-ubuntu-package-install-debconf-noninteract  
ENV DEBIAN_FRONTEND noninteractive  
  
# runs during installation and remove junk, as described in
http://docs.docker.com/engine/articles/dockerfile_best-practices/#apt-get  
# libre office is used in convert_doc.sh, which enables to embed doc files
inside tex  
# pandoc is used in convert_md.sh, which enables us to convert markdown to tex  
# poppler-utils: pdftoppm, is used for converting pdf to png images, as
mentioned http://superuser.com/questions/185880/how-to-convert-a-pdf-document-
to-png  
RUN apt-get update && \  
apt-get install -y \  
libreoffice \  
pandoc \  
poppler-utils \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  

