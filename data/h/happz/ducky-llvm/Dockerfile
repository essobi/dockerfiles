FROM docker.io/fedora  
MAINTAINER Milos Prchlik <happz@happz.cz>  
  
RUN dnf update -y \  
&& dnf install -y dnf-plugins-core \  
&& dnf copr -y enable happz/ducky-llvm \  
&& dnf install -y ducky-llvm \  
&& dnf clean all  
  
ENV PATH=/opt/ducky/bin:$PATH \  
CC="clang" \  
CXX="clang++" \  
AR="llvm-ar"  

