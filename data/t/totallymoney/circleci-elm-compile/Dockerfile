FROM node:9  
RUN yarn global add elm --no-progress  
RUN git clone https://github.com/obmarg/libsysconfcpus.git;  
RUN cd libsysconfcpus && ./configure && make && make install && cd ../  
  

