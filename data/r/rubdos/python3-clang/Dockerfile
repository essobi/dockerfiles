FROM python:3-onbuild  
  
RUN echo "deb http://llvm.org/apt/jessie/ llvm-toolchain-jessie main \n\  
deb-src http://llvm.org/apt/jessie/ llvm-toolchain-jessie main \n\  
deb http://llvm.org/apt/jessie/ llvm-toolchain-jessie-3.7 main \n\  
deb-src http://llvm.org/apt/jessie/ llvm-toolchain-jessie-3.7 main" >>
/etc/apt/sources.list  
  
RUN wget -O - http://llvm.org/apt/llvm-snapshot.gpg.key | apt-key add -  
  
RUN apt-get update && apt-get install -y clang-3.7 libclang-common-3.7-dev
libclang-3.7-dev libclang1-3.7 libclang1-3.7-dbg libllvm-3.7-ocaml-dev
libllvm3.7 libllvm3.7-dbg lldb-3.7 llvm-3.7 llvm-3.7-dev llvm-3.7-runtime
clang-modernize-3.7 clang-format-3.7 lldb-3.7-dev liblldb-3.7-dbg indent npm
nodejs-legacy  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN echo "/usr/lib/llvm-3.7/lib/" >> /etc/ld.so.conf && ldconfig  
  
RUN npm install -g remark  
  
ENV LD_LIBRARY_PATH /usr/lib/llvm-3.7/lib/  

