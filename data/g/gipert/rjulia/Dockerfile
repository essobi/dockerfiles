FROM gipert/julia:latest  
  
USER root  
  
USER root  
WORKDIR /tmp  
  
RUN yum install -y -q xorg-x11-fonts-Type1 fftw-devel libXmu-devel \  
libXi-devel libX11-devel libXext-devel \  
libXft-devel libXpm-devel libzip-devel \  
mesa-libGLU-devel gsl-devel python-devel graphviz-devel \  
libjpeg-devel libpng-devel giflib-devel libtiff-devel \  
libxml2-devel openssl-devel fttw-devel && \  
yum -q clean all  
  
RUN mkdir -p /scif/root && \  
wget -q -O- https://baltig.infn.it/gerda/baseos-
binaries/raw/master/root-6.06.08-centos7.tar.gz \  
| tar --strip-components 1 -xz -C "/scif/root"  
  
ENV ROOTSYS="/scif/root" \  
PATH="/scif/root/bin:$PATH" \  
LD_LIBRARY_PATH="/scif/root/lib:$LD_LIBRARY_PATH" \  
MANPATH="/scif/root/man:$MANPATH" \  
PYTHONPATH="/scif/root/lib:$PYTHONPATH" \  
JULIA_CXX_RTTI="1"  
RUN julia -e 'Pkg.add("Cxx"); Pkg.add("ROOT")' && \  
julia -e 'using Cxx' && \  
mv /scif/julia/pkgs/v0.6/ROOT/deps/usr/bin/julia /scif/julia/usr/bin/rjulia  
  
WORKDIR /data  
CMD rjulia  

