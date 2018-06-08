# Base Python image has most up to date Python parts  
# Debian derived  
FROM python:2  
MAINTAINER Gabor Csanyi "gc121@cam.ac.uk"  
######################  
## Root environment ##  
######################  
RUN cp /etc/skel/.bash* /etc/skel/.profile /root/  
RUN echo "PS1='docker:\W$ '" >> /root/.bashrc  
  
###################  
## OS level deps ##  
###################  
# Build tools and deps for QUIP  
# Followed by some useful utilities  
RUN apt-get -y update \  
&& apt-get upgrade -y \  
&& apt-get install -y \  
gfortran \  
openmpi-bin \  
libopenmpi-dev \  
liblapack-dev \  
libblas-dev \  
libnetcdf-dev \  
netcdf-bin \  
curl \  
libzmq3 \  
# Useful tools  
vim \  
emacs-nox \  
less \  
bsdmainutils \  
man-db \  
# AtomEye  
libxpm-dev \  
libgsl0-dev \  
xterm \  
# amber  
csh \  
flex \  
# gpaw  
libxc-dev \  
# target for the future  
python3 \  
python3-dev  
  
# Custom compilation of OpenBLAS with OpenMP enabled  
# (linear algebra is limited to single core in debs)  
# NUM_THREADS must be set otherwise docker hub build  
# non-parallel version.  
RUN git clone https://github.com/xianyi/OpenBLAS.git /tmp/OpenBLAS \  
&& cd /tmp/OpenBLAS/ \  
&& make DYNAMIC_ARCH=1 NO_AFFINITY=1 USE_OPENMP=1 NUM_THREADS=32 \  
&& make DYNAMIC_ARCH=1 NO_AFFINITY=1 USE_OPENMP=1 NUM_THREADS=32 install \  
&& rm -rf /tmp/OpenBLAS  
  
# Make OpenBLAS the default  
RUN update-alternatives --install /usr/lib/libblas.so libblas.so
/opt/OpenBLAS/lib/libopenblas.so 1000  
RUN update-alternatives --install /usr/lib/libblas.so.3 libblas.so.3
/opt/OpenBLAS/lib/libopenblas.so 1000  
RUN update-alternatives --install /usr/lib/liblapack.so liblapack.so
/opt/OpenBLAS/lib/libopenblas.so 1000  
RUN update-alternatives --install /usr/lib/liblapack.so.3 liblapack.so.3
/opt/OpenBLAS/lib/libopenblas.so 1000  
RUN ldconfig  
  
############  
## Python ##  
############  
# Put any Python libraries here  
RUN pip install --upgrade pip  
RUN pip install --no-cache-dir jupyter numpy scipy matplotlib ase pyamg \  
imolecule sphinx spglib nglview RISE pandas  
  
# Development version of GPAW - requires latest ASE and numpy to install  
RUN cd /opt && curl https://wiki.fysik.dtu.dk/gpaw/gpaw-1.3.1b1.tar.gz | tar
xz && \  
cd gpaw-1.3.1b1 && pip install --no-cache-dir .  
  
# Keep the source for examples  
RUN git clone https://github.com/libAtoms/matscipy.git /opt/matscipy \  
&& cd /opt/matscipy \  
&& pip install --no-cache-dir .  
  
RUN pip install --global-option=build_ext --global-
option="-L/opt/OpenBLAS/lib" atomistica  
  
RUN jupyter nbextension enable \--py --sys-prefix widgetsnbextension  
RUN jupyter nbextension enable \--py --sys-prefix nglview  
RUN jupyter-nbextension install rise --py --sys-prefix  
RUN jupyter-nbextension enable rise --py --sys-prefix  
  
###########  
## Julia ##  
###########  
# List of Julia packages to install  
ARG JULIA_PACKAGES="IJulia PyCall JuLIP PyPlot ODE Plots Interact"  
# Set JULIA_PKGDIR to install packages globally  
ENV JULIA_PKGDIR /opt/julia/share/site  
  
  
ENV JULIA_PATH /opt/julia/v0.6  
ENV JULIA_VERSION 0.6.2  
# Don't store the intermediate file, pipe into tar  
RUN mkdir -p $JULIA_PATH \  
&& cd $JULIA_PATH \  
&& curl
"https://julialang-s3.julialang.org/bin/linux/x64/${JULIA_VERSION%[.-]*}/julia-${JULIA_VERSION}-linux-x86_64.tar.gz"
| tar xz --strip-components 1  
  
# umask ensures directories are writeable for non-root user  
RUN umask 0000 \  
&& ${JULIA_PATH}/bin/julia -e 'Pkg.init()' \  
&& echo "${JULIA_PACKAGES}" | sed 's/\s\\+/\n/g' >
$JULIA_PKGDIR/v${JULIA_VERSION%[.-]*}/REQUIRE \  
&& ${JULIA_PATH}/bin/julia -e 'Pkg.resolve()' \  
# pre-compilation of installed packages  
&& ${JULIA_PATH}/bin/julia -e 'for pkg in keys(Pkg.installed()); try pkgsym =
Symbol(pkg); eval(:(using $pkgsym)); catch; end; end' \  
&& chmod -R a+rw ${JULIA_PKGDIR}/lib  
  
#ENV JULIA_PATH /opt/julia/v0.5  
#ENV JULIA_VERSION 0.5.2  
# Don't store the intermediate file, pipe into tar  
#RUN mkdir -p $JULIA_PATH \  
# && cd $JULIA_PATH \  
# && curl
"https://julialang-s3.julialang.org/bin/linux/x64/${JULIA_VERSION%[.-]*}/julia-${JULIA_VERSION}-linux-x86_64.tar.gz"
| tar xz --strip-components 1  
# umask ensures directories are writeable for non-root user  
#RUN umask 0000 \  
# && ${JULIA_PATH}/bin/julia -e 'Pkg.init()' \  
# && echo "${JULIA_PACKAGES}" | sed 's/\s\\+/\n/g' >
$JULIA_PKGDIR/v${JULIA_VERSION%[.-]*}/REQUIRE \  
# && ${JULIA_PATH}/bin/julia -e 'Pkg.resolve()' \  
# # pre-compilation of installed packages  
# && ${JULIA_PATH}/bin/julia -e 'for pkg in keys(Pkg.installed()); try pkgsym
= Symbol(pkg); eval(:(using $pkgsym)); catch; end; end' \  
# && chmod -R a+rw ${JULIA_PKGDIR}/lib  
# Add to path as current version  
ENV PATH $JULIA_PATH/bin:$PATH  
  
# Add kernelspecs to global Jupyter  
RUN mv /root/.local/share/jupyter/kernels/julia*
/usr/local/share/jupyter/kernels/  
  
##########  
## DATA ##  
##########  
# Published GAPs  
# Remote URLs do not get decompressed so pipe through tar  
ENV POTENTIALS_DIR /opt/share/potentials  
  
RUN wget -nv -O- "http://www.libatoms.org/pub/Home/TungstenGAP/GAP_6.tbz2" \  
| tar xj -P --transform "s,^,${POTENTIALS_DIR}/GAP/Tungsten/,"  
RUN wget -nv -O- "http://www.libatoms.org/pub/Home/IronGAP/gp33b.tar.gz" \  
| tar xz -P --transform "s,^,${POTENTIALS_DIR}/GAP/Iron/,"  
RUN wget -nv -O-
"http://www.libatoms.org/pub/Home/DataRepository/gap_dft_corrections_water.tgz"
\  
| tar xz -P --transform "s,^,${POTENTIALS_DIR}/GAP/Water/,"  
RUN wget -nv -O-
"http://www.libatoms.org/pub/Home/DataRepository/gap_dft_corrections_ch4_h2o.tgz"
\  
| tar xz -P --transform "s,^,${POTENTIALS_DIR}/GAP/WaterCH4/,"  
RUN wget -nv -O-
"http://www.libatoms.org/pub/Home/DataRepository/gap_dft_1_2_body_LiH2O.tgz" \  
| tar xz -P --transform "s,^,${POTENTIALS_DIR}/GAP/WaterLiH2O/,"  
RUN wget -nv -O-
"http://www.libatoms.org/pub/Home/DataRepository/aC_GAP.tar.gz" \  
| tar xz -P --transform "s,^,${POTENTIALS_DIR}/GAP/Carbon/,"  
  
ADD Files/GAPPotentials.md ${POTENTIALS_DIR}/  
  
# GPAW data  
# Ensure we don't run interactively  
ENV GPAW_SETUP_VERSION 0.9.20000  
RUN gpaw install-data --no-register --version=${GPAW_SETUP_VERSION}
/opt/share/gpaw  
ENV GPAW_SETUP_PATH /opt/share/gpaw/gpaw-setups-${GPAW_SETUP_VERSION}  
  
##############  
## Software ##  
##############  
# Add big software packages into the Software subdirectory  

