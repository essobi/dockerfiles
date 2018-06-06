FROM alpine  
  
# fix library dependencies  
# otherwise golang binary may encounter 'not found' error  
RUN mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-
linux-x86-64.so.2  
  
COPY libunqlite.so.1.0 /usr/local/lib/  
COPY unqlite.h /usr/local/include/  
RUN ln -sf /usr/local/lib/libunqlite.so.1.0 /usr/local/lib/libunqlite.so.1  
RUN ln -sf /usr/local/lib/libunqlite.so.1 /usr/local/lib/libunqlite.so  
RUN ldconfig /usr/local/lib/libunqlite.so  

