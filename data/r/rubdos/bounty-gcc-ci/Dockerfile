FROM rubdos/fedora-gcc  
  
RUN git clone https://github.com/TheBounty/Core.git  
  
RUN cd Core && mkdir build && cd build && \  
cmake -DWITH_QT=off -DWITH_YAF_PY_BINDINGS=off .. &&\  
make -j4 && make install  
  
ENV BOUNTY_PATH /Core  

