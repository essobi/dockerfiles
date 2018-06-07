FROM jumbojett/hiphop-php-docker:step6  
  
  
ENV CC=gcc CXX=g++  
RUN cp /usr/lib64/libc-client.so.2007f /usr/local/lib/libc-client.so  
RUN cp -r /build/imap $HOME/local/include/  
  
RUN cd /build/hiphop-php && \  
export CMAKE_INCLUDE_PATH=$HOME/local/include && \  
export CMAKE_LIBRARY_PATH=$HOME/local/lib && \  
cmake . && \  
/build/hiphop-php/hphp/tools/generate_compiler_id.sh && \  
/build/hiphop-php/hphp/tools/generate_repo_schema.sh && \  
make -j$(nproc)  
  
CMD /build/hiphop-php/hphp/hphp/hphp  

