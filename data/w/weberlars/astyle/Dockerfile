FROM busybox:latest AS src  
RUN wget -O astyle.tar.gz
https://downloads.sourceforge.net/project/astyle/astyle/astyle%203.1/astyle_3.1_linux.tar.gz  
RUN tar -xf astyle.tar.gz  
  
FROM gcc:latest AS build  
COPY \--from=src astyle astyle  
RUN cp astyle/build/gcc/Makefile astyle/src/Makefile  
WORKDIR astyle/src/  
RUN LDFLAGS=-static CFLAGS="-Wall -Wextra -fno-rtti -fno-exceptions -std=c++11
-static" make  
RUN strip bin/astyle  
  
FROM busybox:latest  
LABEL maintainer="weber@weber-software.com"  
COPY \--from=build astyle/src/bin/astyle /usr/bin/astyle  

