FROM centos:7  
  
LABEL maintainer="luigi.pertoldi@pd.infn.it"  
  
USER root  
WORKDIR /root  
  
RUN yum update -y -q && \  
yum install -y -q epel-release deltarpm && \  
yum groupinstall -y -q "Development Tools" && \  
yum install -y -q htop zsh vim wget cmake3 \  
expat-devel xerces-c-devel fftw-devel \  
libXmu-devel libXi-devel libX11-devel \  
libXext-devel libXft-devel libXpm-devel \  
libzip-devel mesa-libGLU-devel \  
libjpeg-devel libpng-devel \  
motif-devel qt-devel mesa-dri-drivers \  
ImageMagick xorg-x11-fonts-Type1 && \  
yum -q clean all && \  
ln -s /usr/bin/cmake3 /usr/bin/cmake  
  
# install ROOT CERN from precompiled binary  
# it will be installed in /opt/root  
  
ENV PATH="/opt/root/bin:$PATH" \  
LD_LIBRARY_PATH="/opt/root/lib:$LD_LIBRARY_PATH" \  
MANPATH="/opt/root/man:$MANPATH" \  
PYTHONPATH="/opt/root/lib:$PYTHONPATH" \  
ROOTSYS="/opt/root"  
  
RUN mkdir -p /opt/root && \  
wget -q -O- https://root.cern.ch/download/root_v6.06.08.Linux-
centos7-x86_64-gcc4.8.tar.gz \  
| tar --strip-components 1 -xz -C "/opt/root"  
  
# install prebuild CLHEP in /opt/clhep  
  
ENV CLHEP_BASE_DIR="/opt/clhep" \  
CLHEP_INCLUDE_DIR="/opt/clhep/include" \  
CLHEP_LIB_DIR="/opt/clhep/lib"  
  
RUN mkdir -p /opt/clhep && \  
wget -q -O- https://baltig.infn.it/gerda/baseos-
binaries/raw/master/clhep-2.3.4.4-centos7.tar.gz \  
| tar --strip-components 1 -xz -C "/opt/clhep"  
# install prebuild geant4 in /opt/geant4  
  
ENV PATH="/opt/geant4/bin:/opt/clhep/bin:$PATH" \  
LD_LIBRARY_PATH="/opt/geant4/lib64:/opt/clhep/lib:$LD_LIBRARY_PATH" \  
G4LEDATA="/opt/geant4/share/Geant4-10.3.3/data/G4EMLOW6.50" \  
G4LEVELGAMMADATA="/opt/geant4/share/Geant4-10.3.3/data/PhotonEvaporation4.3.2"
\  
G4NEUTRONHPDATA="/opt/geant4/share/Geant4-10.3.3/data/G4NDL4.5" \  
G4NEUTRONXSDATA="/opt/geant4/share/Geant4-10.3.3/data/G4NEUTRONXS1.4" \  
G4PIIDATA="/opt/geant4/share/Geant4-10.3.3/data/G4PII1.3" \  
G4RADIOACTIVEDATA="/opt/geant4/share/Geant4-10.3.3/data/RadioactiveDecay5.1.1"
\  
G4REALSURFACEDATA="/opt/geant4/share/Geant4-10.3.3/data/RealSurface1.0" \  
G4SAIDXSDATA="/opt/geant4/share/Geant4-10.3.3/data/G4SAIDDATA1.1" \  
G4ENSDFSTATEDATA="/opt/geant4/share/Geant4-10.3.3/data/G4ENSDFSTATE2.1" \  
G4ABLADATA="/opt/geant4/share/Geant4-10.3.3/data/G4ABLA3.0"  
  
RUN mkdir -p /opt/geant4 && \  
wget -q -O- https://baltig.infn.it/gerda/baseos-
binaries/raw/master/geant4-10.3.p03-centos7.tar.gz \  
| tar --strip-components 1 -xz -C "/opt/geant4"  
  
CMD /bin/zsh  

