FROM cerebralfix/static-library-builder-ios  
  
RUN get-source curl https://github.com/bagder/curl.git
795f013006f72ce2f9d2e13f56f54b8398040a4d  
  
WORKDIR /opt/src/curl  
  
RUN ./buildconf  
  
RUN ./configure --disable-shared --enable-static --target="armv7-apple-ios"
\--prefix=/opt/build/curl/armv7/ && make && make install && make clean  
RUN ./configure --disable-shared --enable-static --target="armv7s-apple-ios"
\--prefix=/opt/build/curl/armv7s/ && make && make install && make clean  
RUN ./configure --disable-shared --enable-static --target="arm64-apple-ios"
\--prefix=/opt/build/curl/arm64/ && make && make install && make clean  
  

