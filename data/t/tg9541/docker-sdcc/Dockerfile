FROM ubuntu:16.04  
RUN apt-get update \  
&& apt-get install -y curl subversion build-essential flex bison libboost-dev
\  
texinfo stx-btree-dev zip netcat gawk python2.7 python-serial \  
&& apt-get autoclean  
  
RUN mkdir /sdcc -p \  
&& cd /sdcc \  
&& svn checkout svn://svn.code.sf.net/p/sdcc/code/trunk/sdcc@9933 \  
&& cd sdcc \  
&& ./configure --disable-pic14-port --disable-pic16-port \  
&& make && make install \  
&& cd / \  
&& rm -Rf /sdcc /tmp/*  
  

