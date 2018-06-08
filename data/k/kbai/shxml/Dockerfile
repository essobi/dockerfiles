FROM ubuntu:16.04  
  
RUN apt-get update -y && apt-get install -y \  
openjdk-8-jre \  
wget \  
unzip  
RUN apt-get update -y && apt-get install -y \  
make  
RUN apt-get update -y && apt-get install -y \  
figlet  
RUN apt-get update -y && apt-get install -y \  
bsdmainutils  
  
RUN locale-gen "en_US.UTF-8"  
ENV LANG "en_US.UTF-8"  
ENV LANGUAGE "en_US:en"  
ENV LC_ALL "en_US.UTF-8"  
RUN mkdir /tmp/shxml-build/  
ADD . /tmp/shxml-build/  
RUN cd /tmp/shxml-build && make install && rm -rf /tmp/shxml-build  
ENTRYPOINT ["/usr/local/bin/shxml"]  

