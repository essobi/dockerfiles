### Storage container.  
# This container does nothing but store files.  
# /bin/sh has been replaced with an asm program that simply ...  
#  
# mov rax,34 ; pause() syscall  
# syscall  
FROM scratch  
MAINTAINER frameloss  
COPY pause /bin/sh  
VOLUME /share  
COPY share/ /share/  
USER 65535  
CMD ['']  
  

