FROM fedora:latest  
ENV DEBIAN_FRONTEND noninteractive  
RUN dnf install -y make cmake wget git gcc-c++ doxygen python2-devel openmpi-
devel environment-modules python-pip clang llvm compiler-rt ccache findutils
boost-devel python2-sphinx fftw-devel python-matplotlib texlive-latex-bin
graphviz boost-openmpi-devel ghostscript mpi4py-openmpi texlive-hyphen-base
texlive-cm texlive-cmap texlive-ucs texlive-ec gromacs-devel hwloc-devel
lmfit-devel ocl-icd-devel hdf5-devel  
RUN wget -O /usr/bin/doxy-coverage
https://raw.githubusercontent.com/alobbs/doxy-coverage/master/doxy-coverage.py  
RUN chmod +x /usr/bin/doxy-coverage  
  
RUN useradd -m espressopp  
USER espressopp  
ENV PATH=/usr/lib64/ccache:${PATH}${PATH:+:}/usr/lib64/openmpi/bin/  
ENV PYTHONPATH=/usr/lib64/python2.7/site-
packages/openmpi${PYTHONPATH:+:}${PYTHONPATH}  
WORKDIR /home/espressopp  
RUN pip install --user codecov coverxygen h5py && python -c 'import h5py'  

