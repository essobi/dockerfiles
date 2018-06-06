FROM ubuntu:xenial  
  
MAINTAINER "Joao Paulo Barbosa" <jpaulobneto@gmail.com>  
  
# Update sources list  
RUN apt-get update -y && apt-get upgrade -y  
  
# Add user to www-data  
RUN usermod -u 1000 www-data  
  
# Required by add-apt-repository  
RUN apt-get install -y \  
python-software-properties \  
software-properties-common \  
wget \  
locales  
  
# Genereating locales  
RUN locale-gen en_US.UTF-8 \  
&& locale-gen pt_BR.UTF-8  
  
RUN export LANG=pt_BR.UTF-8  
RUN export LC_ALL=pt_BR.UTF-8  
  
# Update repositories  
RUN LC_ALL=en_US.UTF-8 add-apt-repository ppa:ondrej/php  
RUN apt-get update -y && apt-get upgrade -y  
  
# Install wkhtmltopdf  
RUN apt-get install -y wget fontconfig libxrender1 xfonts-base xfonts-75dpi
libjpeg-turbo8 libxext6  
RUN wget
https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-
generic-amd64.tar.xz  
RUN tar -xvf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz  
RUN rm wkhtmltox-0.12.4_linux-generic-amd64.tar.xz  
WORKDIR /wkhtmltox/bin/  
RUN mv wkhtmltopdf /usr/bin/wkhtmltopdf  
RUN mv wkhtmltoimage /usr/bin/wkhtmltoimage  
RUN rm -rf wkhtmltox  
  
# Return workdir  
WORKDIR /  

