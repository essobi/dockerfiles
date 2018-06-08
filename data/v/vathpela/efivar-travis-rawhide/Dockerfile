FROM fedora:rawhide  
MAINTAINER Peter Jones <pjones@redhat.com>  
  
RUN dnf --nodocs -y --best --allowerasing install dnf-plugins-core git make
@buildsys-build  
RUN dnf --nodocs -y --best --allowerasing builddep efivar  
RUN dnf -y clean all  
  
RUN rm -rf /usr/share/doc/* /usr/share/man/*  
  
RUN mkdir -p /root  
WORKDIR /root  
  
ENV PREFIX=/usr  
  
RUN git clone \--depth 1 https://github.com/rhboot/efivar && cd efivar && make
clean all && make clean  

