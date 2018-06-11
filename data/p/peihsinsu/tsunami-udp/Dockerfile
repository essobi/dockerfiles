FROM ubuntu:12.04  
RUN apt-get update -y  
RUN apt-get install gcc autoconf automake cvs make -y  
RUN apt-get install git -y  
  
# RUN cvs -z3 -d:pserver:anonymous@tsunami-
udp.cvs.sourceforge.net:/cvsroot/tsunami-udp co -P tsunami-udp &&\  
RUN git clone https://github.com/cheetahmobile/tsunami-udp.git && \  
cd tsunami-udp &&\  
./recompile.sh &&\  
make install  
  
# start fluentd  
WORKDIR /data  
EXPOSE 80  

