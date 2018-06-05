FROM ubuntu:14.04  
RUN apt-get update -y  
RUN apt-get install -y build-essential libgmp10-dev curl  
RUN curl -s -L
http://downloads.sourceforge.net/project/mlton/mlton/20130715/mlton-20130715-1.amd64-linux.tgz
| zcat - | tar x  
  
WORKDIR /home  
VOLUME /home  
  
ENTRYPOINT ["mlton"]  

