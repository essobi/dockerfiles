FROM fedora:latest  
RUN dnf -y install make cmake git gcc-c++ gromacs-devel expat-devel fftw-devel
gsl-devel boost-devel txt2tags sqlite-devel gromacs ccache procps-ng octave
gnuplot python2-numpy psmisc  
RUN useradd -m votca  
USER votca  
ENV PATH=/usr/lib64/ccache:${PATH}${PATH:+:}  
WORKDIR /home/votca  

