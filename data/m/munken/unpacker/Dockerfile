FROM munken/ucesb  
  
  
RUN git clone https://Munken@git.kern.phys.au.dk/ausa/unpacker.git \  
&& make -C unpacker/basement-shadow mbs  
  
COPY unpack.sh /  
  
ENV INPUT_DIR=/data  
ENV OUTPUT_DIR=/output  
ENV UNPACKER=/unpacker/basement-shadow/MBS_unpacker  
  
CMD /unpack.sh  

