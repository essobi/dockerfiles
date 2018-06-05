##########################################################  
##  
## This image enables the generation  
## of eBooks in various formats.  
## - The directory structure will be  
## as per that found in the gitlab repo:  
## https://gitlab.com/avastmick/book-template  
## - Pandoc will generate the EPUB, PDF and DOCX formats  
## - Kindlegen will generate the MOBI format  
##  
##########################################################  
  
FROM ubuntu:latest  
  
ENV KINDLEGEN-VERSION 2.9  
  
MAINTAINER avastmick  
  
# Install textlive  
RUN apt-get -yq update && \  
apt-get install -qy --fix-missing \  
wget \  
pandoc \  
texlive \  
texlive-latex-extra \  
&& \  
apt-get -yq autoremove && \  
apt-get clean -y && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
## Install Kindlegen  
RUN mkdir kindlegen && cd kindlegen && \  
wget http://kindlegen.s3.amazonaws.com/kindlegen_linux_2.6_i386_v2_9.tar.gz -O
- | tar -xz && \  
mv ./kindlegen /usr/local/bin/kindlegen  

