FROM opensuse:42.3  
MAINTAINER robin.roth@kit.edu  
  
RUN zypper --gpg-auto-import-keys --non-interactive ref && \  
zypper --gpg-auto-import-keys --non-interactive up  
  
RUN zypper --non-interactive in \--auto-agree-with-licenses \  
automake make libtool \  
gcc gcc-fortran gcc-c++ \  
gcc5 gcc5-fortran gcc5-c++ \  
binutils-gold \  
gsl gsl-devel \  
openmpi openmpi-devel Modules \  
python3-pytest which \  
LHAPDF-devel libLHAPDF python-openssl \  
fastjet-devel libfastjet0 fastjet-plugin-siscone fastjet-plugin-siscone-devel
\  
texlive-latex texlive-collection-science texlive-collection-latexextra \  
git  
  
RUN lhapdf update && lhapdf install cteq6l1 CT10nlo CT14nlo  

