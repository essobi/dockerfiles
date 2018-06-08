FROM ubuntu:16.04 as build  
  
# install build dependencies  
RUN apt-get update && apt-get install -y \  
build-essential libssl-dev libevent-dev libseccomp-dev libcap-dev libboost-
all-dev pkg-config git ca-certificates autoconf automake \  
&& rm -rf /var/lib/apt/lists/*  
RUN git clone https://github.com/XSPECOfficial/spectre  
WORKDIR /spectre  
RUN cd /spectre  
RUN git checkout tags/v1.3.5  
RUN git submodule update --init --recursive  
RUN /bin/bash autogen.sh  
RUN ./configure  
RUN make  
RUN ls -la src/  
  
# execution image  
FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y --no-install-recommends \  
software-properties-common apt-utils ca-certificates wget libssl1.0
libevent-2.0-5 libseccomp2 libcap2 libboost-filesystem1.58.0  
RUN apt-get install -y libboost-program-options1.58.0  
RUN apt-get install -y libboost-thread1.58.0  
  
RUN rm -rf /var/lib/apt/lists/*  
  
COPY \--from=build /spectre/src/spectrecoind /spectre/spectrecoind  
  
ENV HOME /spectre  
WORKDIR /spectre  
  
COPY entrypoint.sh /spectre/entrypoint.sh  
  
#ENV SERVICE_PORT ${SERVICE_PORT:-4000}  
# mark ports for expose  
#EXPOSE $SERVICE_PORT  
#VOLUME /paywatch/data  
ENTRYPOINT ["./entrypoint.sh"]  

