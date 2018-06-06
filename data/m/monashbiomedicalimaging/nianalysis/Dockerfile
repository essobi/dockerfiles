FROM neurodebian:xenial  
MAINTAINER Tom Close <tom.close@monash.edu>  
  
RUN apt-get update; apt-get install -y git g++ python python-numpy \  
libeigen3-dev zlib1g-dev libqt4-opengl-dev libgl1-mesa-dev \  
libfftw3-dev libtiff5-dev python-pip vim wget cmake tcl tcl-dev  
  
RUN mkdir /downloads  
RUN mkdir /packages  
RUN mkdir /modules  
  
WORKDIR /downloads  
  
# Install environment modules to handle package versions  
ENV MODULE_VER 4.1.0  
RUN wget
http://downloads.sourceforge.net/project/modules/Modules/modules-$MODULE_VER/modules-$MODULE_VER.tar.gz  
RUN tar xzf modules-$MODULE_VER.tar.gz  
WORKDIR /downloads/modules-$MODULE_VER  
RUN ./configure --with-module-path=/modules --prefix=/packages/modules  
RUN make  
RUN make install  
RUN echo '/modules' > /packages/modules/init/.modulespath  
RUN cp /downloads/modules-$MODULE_VER/compat/etc/global/profile.modules
/etc/profile.d/modules.sh  
RUN sed -i 's/Modules//g' /etc/profile.d/modules.sh  
  
# Set modules environment variables  
ENV BASH_ENV '/packages/modules/init/bash'  
ENV ENV '/packages/modules/init/profile.sh'  
ENV LOADEDMODULES ''  
ENV MANPATH '/packages/modules/share/man'  
ENV MODULEPATH '/modules'  
ENV MODULEPATH_modshare '/modules:1'  
ENV MODULESHOME '/packages/modules'  
ENV MODULES_CMD '/packages/modules/libexec/modulecmd.tcl'  
ENV PATH "/packages/modules/bin:$PATH"  
# Install Dcm2niix and MRtrix for format conversion  
# Install Dcm2niix  
RUN git clone https://github.com/rordenlab/dcm2niix.git /packages/dcm2niix  
RUN mkdir /packages/dcm2niix/build  
WORKDIR /packages/dcm2niix/build  
RUN cmake ..  
RUN make  
  
# Create modulefile  
RUN mkdir -p /modules/dcm2niix  
RUN echo '#%Module1.0' >> /modules/dcm2niix/1.0.2  
RUN echo 'proc ModulesHelp { } {' >> /modules/dcm2niix/1.0.2  
RUN echo 'global dotversion' >> /modules/dcm2niix/1.0.2  
RUN echo 'puts stderr "\tDcm2niix"' >> /modules/dcm2niix/1.0.2  
RUN echo '}' >> /modules/dcm2niix/1.0.2  
RUN echo 'module-whatis "Dcm2niix"' >> /modules/dcm2niix/1.0.2  
RUN echo 'conflict dcm2niix' >> /modules/dcm2niix/1.0.2  
RUN echo 'prepend-path PATH /packages/dcm2niix/build/bin' >>
/modules/dcm2niix/1.0.2  
  
# Install MRtrix  
RUN git clone https://github.com/MRtrix3/mrtrix3.git /packages/mrtrix  
WORKDIR /packages/mrtrix  
RUN ./configure  
RUN ./build  
  
# Create modulefile  
RUN mkdir -p /modules/mrtrix  
RUN echo '#%Module1.0' >> /modules/mrtrix/3  
RUN echo 'proc ModulesHelp { } {' >> /modules/mrtrix/3  
RUN echo 'global dotversion' >> /modules/mrtrix/3  
RUN echo 'puts stderr "\tMRtrix 3"' >> /modules/mrtrix/3  
RUN echo '}' >> /modules/mrtrix/3  
RUN echo 'module-whatis "MRtrix 3"' >> /modules/mrtrix/3  
RUN echo 'conflict mrtrix' >> /modules/mrtrix/3  
RUN echo 'prepend-path PATH /packages/mrtrix/bin' >> /modules/mrtrix/3  
RUN echo 'prepend-path LD_LIBRARY_PATH /packages/mrtrix/lib' >>
/modules/mrtrix/3  
  
# Install NiAnalysis and prerequisite pipelines  
ENV BUILT_AT 2018-03-12-13:28  
RUN pip install git+https://github.com/mbi-image/nianalysis.git  

