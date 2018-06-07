FROM centos:7  
MAINTAINER "Stefan Walraven" <stefan.walraven@cs.kuleuven.be>  
  
ENV AVL_VERSION 3.35  
RUN yum updateinfo && yum install -y \  
make \  
sed \  
fortran \  
gfortran \  
gcc-gfortran \  
wget \  
&& yum groupinstall -y X11 \  
&& yum install -y libX11-devel-1.6.3-2.el7.x86_64  
  
RUN wget -q http://web.mit.edu/drela/Public/web/avl/avl$AVL_VERSION.tgz && tar
-xzf avl$AVL_VERSION.tgz  
  
RUN make -C Avl/plotlib  
RUN make -C Avl/eispack  
RUN sed -i 's_/home/codes/bin/_/usr/local/bin/_g' Avl/bin/Makefile  
RUN make -C Avl/bin  
  
# CMD ["avl", "Avl/runs/vanilla.avl"]  
CMD ["/bin/bash"]  

