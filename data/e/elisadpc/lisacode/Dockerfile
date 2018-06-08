FROM elisadpc/elisadpc:latest  
MAINTAINER eLISA DPC ccavet@apc.in2p3.fr  
  
WORKDIR /workspace  
RUN cd /workspace  
RUN pwd  
  
RUN git config --global http.postBuffer 524288000  
RUN git config --global --add core.compression -1  
RUN git clone https://gitlab.in2p3.fr/elisadpc/LISACode.git -b master
--single-branch  
RUN cd /workspace/LISACode && ls -l  
RUN mkdir /workspace/LISACode/cmake_build  
WORKDIR /workspace/LISACode/cmake_build  
RUN cd /workspace/LISACode/cmake_build  
RUN cmake -D LC_LIB=/usr/lib -D LC_BIN=/usr/bin -D LC_CFG=/usr/Cfg
/workspace/LISACode/.  
RUN make && make install  
RUN chmod +x /usr/bin/makeTDI-lisacode2.py  
  
WORKDIR /workspace  
RUN cd /workspace && rm -fr LISACode  
RUN pwd  

