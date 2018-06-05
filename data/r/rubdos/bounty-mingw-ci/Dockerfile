FROM rubdos/fedora-mingw  
  
RUN dnf install -y python3-devel  
  
RUN git clone https://github.com/TheBounty/Core.git  
  
RUN cd Core && mkdir build && cd build && \  
mingw64-cmake \  
-DWITH_QT=off \  
-DWITH_YAF_PY_BINDINGS=off .. && \  
make -j4 &&\  
make install  
  
ENV BOUNTY_PATH /Core  

