# ----------------------  
# Docker's informations:  
# ----------------------  
FROM ubuntu:16.04  
MAINTAINER Jocelyn LOPEZ <jocelyn.lopez.pro@gmail.com>  
  
# --------------------------  
# Install required packages:  
# --------------------------  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libreoffice \  
libreoffice-writer \  
ure \  
libreoffice-java-common \  
libreoffice-core \  
libreoffice-common \  
fonts-opensymbol \  
hyphen-fr \  
hyphen-de \  
hyphen-en-us \  
hyphen-it \  
hyphen-ru \  
fonts-dejavu \  
fonts-dejavu-core \  
fonts-dejavu-extra \  
fonts-dustin \  
fonts-f500 \  
fonts-fanwood \  
fonts-freefont-ttf \  
fonts-liberation \  
fonts-lmodern \  
fonts-lyx \  
fonts-sil-gentium \  
fonts-texgyre \  
fonts-tlwg-purisa \  
&& rm -rf /var/lib/apt/lists/*  
  
# ---------  
# Settings:  
# ---------  
EXPOSE 8997  
RUN adduser --home=/opt/libreoffice --disabled-password --gecos ""
\--shell=/bin/bash libreoffice  
  
# -----------  
# Executable:  
# -----------  
ENTRYPOINT ["/usr/bin/libreoffice","--nologo","--norestore", "--invisible","--
headless"]  
CMD ["--accept='socket,host=0,port=8997,tcpNoDelay=1;urp;'"]  

