FROM base/devel:latest  
RUN pacman -Syy  
RUN pacman -S --noconfirm blas \  
chromium \  
cmake \  
gcc-fortran \  
gdb \  
git \  
hdf5-openmpi \  
jupyter-nbconvert \  
jupyter-notebook \  
lapack \  
libpng \  
libxml2 \  
mesa glu gl2ps \  
mlocate \  
openmpi \  
python-ipywidgets \  
python2 \  
python2-ipykernel \  
python2-matplotlib \  
python2-mpi4py \  
python2-numpy \  
python2-pandas \  
python2-pint \  
python2-pip \  
python2-scipy \  
python2-sphinx \  
rsync \  
swig \  
valgrind \  
vim \  
wget \  
xorg mathjax \  
zlib  
  
RUN pacman -Sc --noconfirm  
  
RUN cd /usr/bin && ln -sf python2 python  
RUN pip2 install plotly  
  
RUN useradd -m -G wheel -s /bin/bash romain  
RUN mkdir /build  
  
WORKDIR /build  
  
RUN wget http://ftp.mcs.anl.gov/pub/petsc/release-snapshots/petsc-3.7.6.tar.gz  
RUN tar -xzf petsc-3.7.6.tar.gz  
RUN cd petsc-3.7.6 && python2 ./configure \  
\--prefix=/opt/petsc-3.7.6 \  
\--download-metis \  
\--download-parmetis \  
\--download-mumps \  
\--download-scalapack  
  
RUN cd petsc-3.7.6 && make PETSC_DIR=/build/petsc-3.7.6 PETSC_ARCH=arch-
linux2-c-debug all  
RUN cd petsc-3.7.6 && make PETSC_DIR=/build/petsc-3.7.6 PETSC_ARCH=arch-
linux2-c-debug install  
RUN rm -rf petsc-3.7.6 petsc-3.7.6.tar.gz  
  
# setup environment  
ENV PYTHONPATH $PYTHONPATH:/build/underworld2  
  
# get underworld, compile, delete some unnecessary files, trust notebooks,
copy to workspace  
RUN git clone \--branch "development" \--single-branch
https://github.com/underworldcode/underworld2 && \  
cd underworld2/libUnderworld && \  
./configure.py --with-debugging=0 --petsc-dir=/opt/petsc-3.7.6 && \  
./compile.py && \  
rm .sconsign.dblite && \  
rm -fr .sconf_temp && \  
cd build && \  
rm -fr PICellerator && \  
rm -fr Solvers && \  
rm -fr StGermain && \  
rm -fr StgDomain && \  
rm -fr StgFEM && \  
rm -fr Underworld && \  
rm -fr gLucifer && \  
rm -fr libUnderworldPy && \  
find /build/underworld2/docs -name \\*.ipynb -print0 | xargs -0 jupyter trust
&& \  
mkdir /home/romain/workspace && \  
rsync -av /build/underworld2/docs/examples /home/romain/workspace && \  
rsync -av /build/underworld2/docs/user_guide /home/romain/workspace && \  
rsync -av /build/underworld2/docs/publications /home/romain/workspace && \  
cd ../../docs/development/api_doc_generator/ && \  
sphinx-build2 . ../../api_doc  
  
# expose notebook port  
EXPOSE 8888  
# expose glucifer port  
EXPOSE 9999  
# Add a notebook profile.  
WORKDIR /home/romain  
  
USER romain  
RUN mkdir -p -m 700 /home/romain/.jupyter/ && \  
echo "c.NotebookApp.ip = '*'" >>
/home/romain/.jupyter/jupyter_notebook_config.py  
  
# setup space for working in  
VOLUME /home/romain/workspace/user_data  
  

