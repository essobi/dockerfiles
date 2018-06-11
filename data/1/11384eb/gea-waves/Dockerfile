FROM fedora:latest  
  
RUN echo 'dnf -y update \  
&& dnf install -y wget tar findutils gcc-c++ llvm make flex openmpi-devel
zlib-devel boost-devel git \  
&& dnf clean all \--enablerepo=\\* \  
&& wget -O - http://dl.openfoam.org/source/4-1 | tar xvz \  
&& wget -O - http://dl.openfoam.org/third-party/4-1 | tar xvz \  
&& mv OpenFOAM-4.x-version-4.1 $HOME/OpenFOAM-4.1 \  
&& mv ThirdParty-4.x-version-4.1 $HOME/ThirdParty-4.1 \  
&& export PATH=$PATH:/usr/lib64/openmpi/bin \  
&& . $HOME/OpenFOAM-4.1/etc/bashrc && . $HOME/.bashrc \  
&& cd $HOME/ThirdParty-4.1 && /bin/bash -c "./Allwmake -j" \  
&& cd $HOME/OpenFOAM-4.1 && /bin/bash -c "./Allwmake" \  
&& echo "" >> /etc/bashrc && echo "export PATH=$PATH:/usr/lib64/openmpi/bin &&
. $HOME/OpenFOAM-4.1/etc/bashrc" >> /etc/bashrc' | /bin/bash  

