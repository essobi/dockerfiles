FROM ubuntu:16.04  
RUN apt-get update  
RUN apt-get install -y g++  
RUN apt-get install -y ksh  
RUN apt-get install -y bison  
RUN apt-get install -y flex  
RUN apt-get install -y libsctp-dev  
RUN apt-get install -y make  
  
RUN mkdir -p /opt/src/seagull  
  
ADD Seagull /opt/src/seagull  
  
WORKDIR /opt/src/seagull/seagull/trunk/src  
RUN ksh build.ksh -target clean  
RUN ksh build.ksh -target all || true  
  
RUN cp bin/* /usr/local/bin  
  
RUN mkdir -p /opt/seagull  
RUN cp -r exe-env/* /opt/seagull  
RUN mkdir -p /opt/seagull/diameter-env/logs && \  
mkdir -p /opt/seagull/h248-env/logs && \  
mkdir -p /opt/seagull/http-env/logs && \  
mkdir -p /opt/seagull/msrp-env/logs && \  
mkdir -p /opt/seagull/octcap-env/logs && \  
mkdir -p /opt/seagull/radius-env/logs && \  
mkdir -p /opt/seagull/sip-env/logs && \  
mkdir -p /opt/seagull/synchro-env/logs && \  
mkdir -p /opt/seagull/xcap-env/logs  
  
WORKDIR /opt/seagull  

