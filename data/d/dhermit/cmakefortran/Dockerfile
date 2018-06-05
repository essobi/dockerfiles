FROM fedora:latest  
  
RUN dnf upgrade -y --refresh  
RUN dnf install -y @development-tools  
RUN dnf install -y mingw64-gcc-c++ mingw64-gcc-gfortran cmake doxygen texlive-
scheme-full graphviz lapack-devel openmpi python3-numpy python3-matplotlib
fftw-devel boost-devel gsl-devel libtiff-devel eigen3-devel python3-devel
yaml-cpp-devel python3-yaml python3-PyYAML PyYAML latexmk wget  
RUN dnf install -y gcc-c++  
RUN dnf clean all -y  
RUN git clone https://github.com/Reference-LAPACK/lapack.git; cd lapack; mkdir
build; cd build; wget
https://raw.githubusercontent.com/SolidTux/DockerCMakeFortran/master/mingw64.cmake;
cmake -DCMAKE_TOOLCHAIN_FILE=mingw64.cmake -DBUILD_SHARED_LIBS=ON
-DCMAKE_INSTALL_PREFIX=/usr/x86_64-w64-mingw32/ -DCMAKE_BUILD_TYPE=Release
-DCBLAS=ON -DLAPACKE=ON -DBUILD_TESTING=OFF ..; make install; rm -rf *; cmake
-DCMAKE_TOOLCHAIN_FILE=mingw64.cmake -DBUILD_SHARED_LIBS=OFF
-DCMAKE_INSTALL_PREFIX=/usr/x86_64-w64-mingw32/ -DCMAKE_BUILD_TYPE=Release
-DCBLAS=ON -DLAPACKE=ON -DBUILD_TESTING=OFF ..; make install; rm -rf *; cd
../../; rm -R lapack  
RUN git clone https://github.com/scgmlz/BornAgain.git  
RUN cd BornAgain; mkdir build; cd build; cmake -DBORNAGAIN_USE_PYTHON3=ON
-DBORNAGAIN_GUI=OFF ..  
RUN cd BornAgain/build; make  
RUN cd BornAgain/build; make install  
RUN rm -R BornAgain  
RUN cat /usr/local/bin/thisbornagain.sh >> /etc/profile  
RUN echo "backend: Agg" >> /usr/share/matplotlib/mpl-data/matplotlibrc  

