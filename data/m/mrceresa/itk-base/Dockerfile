FROM mrceresa/jenkins-slave-fedora  
MAINTAINER Mario Ceresa <mario.ceresa@upf.edu>  
  
USER root  
RUN dnf -y install InsightToolkit-devel vtk-devel gdcm-devel vxl-devel fftw-
devel && dnf clean all  
RUN ln -s /usr/lib64/cmake/InsightToolkit /usr/lib64/cmake/ITK  
  
RUN dnf -y install tclap && dnf clean all  
  
USER jenkins  
  

