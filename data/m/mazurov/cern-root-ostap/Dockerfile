FROM mazurov/cern-root:6.08.00  
MAINTAINER alexander.mazurov <alexander.mazurov@gmail.com>  
  
LABEL description="CERN ROOT framework"  
  
RUN yum -y install cmake3 make gsl-devel libSM libX11 libXft libXpm libXext &&
yum -y clean all  
RUN ln -s /usr/bin/cmake3 /usr/bin/cmake  
# Set ROOT environment  
ENV ROOTSYS "/opt/root"  
ENV PATH "$ROOTSYS/bin:$ROOTSYS/bin/bin:$PATH"  
ENV LD_LIBRARY_PATH "$ROOTSYS/lib:$LD_LIBRARY_PATH"  
ENV PYTHONPATH "$ROOTSYS/lib:PYTHONPATH"

