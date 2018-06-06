FROM ubuntu:16.04  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y apt-transport-https \  
&& echo "deb https://dl.bintray.com/sbt/debian /" | tee -a
/etc/apt/sources.list.d/sbt.list \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv
2EE0EA64E40A89B84B2DF73499E82A75642AC823 \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y git make autoconf g++
flex bison openjdk-8-jdk-headless \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y sbt \  
&& rm -rf /var/lib/apt/lists/*  
RUN cd /opt \  
&& git clone https://github.com/ucb-bar/firrtl.git \  
&& cd firrtl \  
&& make build-scala \  
&& cd /opt \  
&& git clone http://git.veripool.org/git/verilator \  
&& cd verilator \  
&& git checkout verilator_3_886 \  
&& unset VERILATOR_ROOT \  
&& autoconf \  
&& ./configure \  
&& make -j2 \  
&& make install  
  
ENV PATH $PATH:/opt/firrtl/utils/bin  
  
# Ensure compiler-interface being compiled  
ADD res/build.sbt /tmp/  
ADD res/t.scala /tmp/  
RUN cd /tmp/ && sbt compile  
  
ENTRYPOINT cd /data/ && sbt  

