FROM alpine:3.5  
RUN mkdir /chez  
WORKDIR /chez  
  
ADD bintar bintar  
ADD boot boot  
ADD BUILDING BUILDING  
ADD c c  
ADD CHARTER.md CHARTER.md  
ADD checkin checkin  
ADD configure configure  
ADD CONTRIBUTING.md CONTRIBUTING.md  
ADD csug csug  
ADD Dockerfile Dockerfile  
ADD examples examples  
ADD LICENSE LICENSE  
ADD LOG LOG  
ADD makefiles makefiles  
ADD mats mats  
ADD nanopass nanopass  
ADD newrelease newrelease  
ADD NOTICE NOTICE  
ADD README.md README.md  
ADD release_notes release_notes  
ADD s s  
ADD scheme.1.in scheme.1.in  
ADD stex stex  
ADD unicode unicode  
ADD wininstall wininstall  
ADD workarea workarea  
ADD zlib zlib  
  
RUN apk update && apk add git curl build-base ncurses ncurses-dev libx11-dev
&& \  
ln -s /usr/include/locale.h /usr/include/xlocale.h && \  
./configure && \  
make -j2 install && \  
make clean && \  
apk del git curl build-base ncurses-dev libx11-dev  
  
WORKDIR /  
  
ENTRYPOINT ["/usr/bin/scheme"]  

