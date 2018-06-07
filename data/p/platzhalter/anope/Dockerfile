FROM debian:jessie  
  
MAINTAINER Platzhalter <platzhalter@sigaint.org>  
  
ADD
https://github.com/anope/anope/releases/download/2.0.3/anope-2.0.3-source.tar.gz
/src/  
  
RUN apt-get update  
RUN apt-get -y install cmake g++  
WORKDIR /src  
RUN tar -xvf anope-*-source.tar.gz  
RUN mv `ls -d anope-*-source/` anope  
WORKDIR anope  
RUN printf "/anope\n\n\n\n\ny\n\n\n\n" | ./Config -nocache -nointro  
WORKDIR build  
RUN make  
RUN make install  
RUN rm -rf /src  
  
VOLUME ["/anope/conf", "/anope/data"]  
  
ENTRYPOINT ["/anope/bin/services"]  
CMD ["--nofork"]  

