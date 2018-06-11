FROM opensuse:tumbleweed  
MAINTAINER Matwey V. Kornilov <matwey.kornilov@gmail.com>  
  
RUN zypper -n ar
'http://download.opensuse.org/repositories/devel:/languages:/go/openSUSE_Factory/devel:languages:go.repo'  
  
RUN zypper -n --gpg-auto-import-keys install --no-recommends --auto-agree-
with-licenses --force-resolution git go tar  

