# areca-7.5 only work fine with default-jre in ubuntu 14.04  
# that needs some script fixs for areca-7.5 after ubuntu 16.04  
FROM ubuntu:14.04  
MAINTAINER Hong-She Liang <starofrainnight@gmail.com>  
  
ENV LANG C.UTF-8  
RUN apt-get update && apt-get install -y \  
wget \  
default-jre \  
&& apt-get clean  
  
# Fixed WARNING: no acl in java.library.path  
RUN ln -s /lib/x86_64-linux-gnu/libacl.so.1.1.0 /usr/lib/libacl.so  
  
# Added areca account and add to root group  
RUN useradd -U areca  
RUN gpasswd -a root areca  
  
RUN wget -O areca-linux.tar.gz
http://sourceforge.net/projects/areca/files/areca-
stable/areca-7.5/areca-7.5-linux-gtk-64.tar.gz/download \  
&& tar xvf areca-linux.tar.gz \  
&& cp -rf areca/* /usr/local/ \  
&& rm -rf areca*  

