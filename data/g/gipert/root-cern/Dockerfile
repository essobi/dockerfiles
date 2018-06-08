FROM gipert/centos-base:latest  
  
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
  
#RUN mkdir -p /tmp/src /tmp/build /scif/root && \  
# wget -O- -q https://root.cern.ch/download/root_v6.10.08.source.tar.gz \  
# | tar --strip-components 1 -xz -C "/tmp/src"  
#  
#WORKDIR /tmp/build  
#  
#RUN cmake -DCMAKE_INSTALL_PREFIX="/scif/root" \  
# -Dx11=ON \  
# -Dunuran=ON \  
# -Dtable=ON \  
# -Droofit=ON \  
# -Dminuit2=ON \  
# -Dhttp=ON \  
# -Dgdml=ON \  
# /tmp/src && \  
# cmake --build . -- -j"$(nproc)" && \  
# make install  
ENV ROOTSYS="/scif/root" \  
PATH="/scif/root/bin:$PATH" \  
LD_LIBRARY_PATH="/scif/root/lib:$LD_LIBRARY_PATH" \  
MANPATH="/scif/root/man:$MANPATH" \  
PYTHONPATH="/scif/root/lib:$PYTHONPATH"  
WORKDIR /data  
CMD /scif/root/bin/root  

