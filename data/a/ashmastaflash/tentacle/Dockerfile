FROM awilson/hydra-nikto  
MAINTAINER Ash Wilson  
  
RUN apt-get update && apt-get -y install curl  
RUN echo 'deb http://packages.cloudpassage.com/debian debian main' | sudo tee
/etc/apt/sources.list.d/cloudpassage.list > /dev/null  
RUN curl http://packages.cloudpassage.com/cloudpassage.packages.key | sudo
apt-key add -  
  
RUN apt-get update \  
&& apt-get -y upgrade \  
&& apt-get -y install \  
build-essential \  
dh-autoreconf \  
libevent-dev \  
git \  
httperf \  
cphalo  
  
#RUN cd /opt/ \  
# && git clone https://github.com/httperf/httperf \  
# && mkdir httperf/build \  
# && cd httperf \  
# && autoreconf -i \  
# && cd build \  
# && ../configure --enable-idleconn --enable-debug \  
# && make \  
# && make install  
COPY ./scripts/*sh /root/  

