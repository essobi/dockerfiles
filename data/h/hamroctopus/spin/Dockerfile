FROM admiringworm/ubuntu:trusty  
MAINTAINER Eric Crosson (eric.s.crosson@utexas.edu)  
  
  
RUN apt-get update -qq && apt-get install -qq -y \  
bison=2:3.0.2.dfsg-2 \  
make=3.81-8.2ubuntu3 \  
g++  
  
# Install spin  
RUN curl -o Src6.4.5.tar.gz http://spinroot.com/spin/Src/src645.tar.gz  
RUN tar xf *.tar.gz  
RUN make -C Src6.4.5 && make -C Src6.4.5 install && rm -rf Src6.4.5
src645.tar.gz  
  
WORKDIR /data  
  
COPY ./docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  

