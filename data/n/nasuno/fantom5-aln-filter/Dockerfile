FROM python:2.7  
MAINTAINER nasuno@ascade.co.jp  
  
ADD http://fantom.gsc.riken.jp/5/suppl/aln_filter/src/Makefile Makefile  
ADD http://fantom.gsc.riken.jp/5/suppl/aln_filter/src/main.c main.c  
ADD http://fantom.gsc.riken.jp/5/suppl/aln_filter/src/aln_filter.h
aln_filter.h  
ADD http://fantom.gsc.riken.jp/5/suppl/aln_filter/src/interface.h interface.h  
ADD http://fantom.gsc.riken.jp/5/suppl/aln_filter/src/interface.c interface.c  
RUN make && mv aln_filter /usr/local/bin/  
RUN rm -f Makefile main.c aln_filter.h interface.[ch]  

