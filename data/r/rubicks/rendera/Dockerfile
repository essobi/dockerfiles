# rendera/Dockerfile  
FROM rubicks/mingw  
MAINTAINER rubicks  
  
WORKDIR /root/  
RUN pwd  
RUN wget http://fltk.org/pub/fltk/1.3.3/fltk-1.3.3-source.tar.gz  
RUN tar vxzf fltk-1.3.3-source.tar.gz  
RUN cd fltk-1.3.3 && \  
./configure \  
\--host=i586-mingw32msvc \  
\--prefix=/usr/i586-mingw32msvc && \  
make install  
  
ADD . /root/rendera  
  
RUN cd rendera && \  
autoreconf -ivf . && \  
./configure \  
\--host=i586-mingw32msvc \  
\--prefix=/usr/i586-mingw32msvc && \  
make install  
  

