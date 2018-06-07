FROM python:2.7  
MAINTAINER nasuno@ascade.co.jp  
  
ADD http://fantom.gsc.riken.jp/5/suppl/delve/delve.tgz delve.tgz  
RUN tar zxf delve.tgz  
RUN cd delve/src && sed -i 's/\$(CC) \$(CFLAGS) \$(LD) \$(OBJECTS) -o
\$(PROGS)/\$(CC) -o \$(PROGS) \$(OBJECTS) \$(CFLAGS) \$(LD)/' Makefile  
RUN cd delve/src; make && mv delve /usr/local/bin/  
RUN rm -rf delve*  

