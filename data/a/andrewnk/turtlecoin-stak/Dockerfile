FROM nvidia/cuda:9.0-base  
  
ENV SOURCE https://github.com/turtlecoin/trtl-stak.git  
ENV XMRSTAK_CMAKE_FLAGS -DXMR-STAK_COMPILE=generic -DCUDA_ENABLE=ON
-DOpenCL_ENABLE=OFF  
  
# Innstall packages  
RUN apt-get update && \  
set -x && \  
apt-get install -qq --no-install-recommends -y ca-certificates git cmake cuda-
core-9-0 cuda-cudart-dev-9-0 libhwloc-dev libmicrohttpd-dev libssl-dev  
  
WORKDIR /tmp  
  
RUN git clone $SOURCE . && \  
sed -i 's/2.0/0.0/' xmrstak/donate-level.hpp && \  
cmake ${XMRSTAK_CMAKE_FLAGS} . && \  
make  
  
WORKDIR /usr/local/bin/  
  
RUN mv /tmp/bin/* /usr/local/bin/ && \  
rm -rf /tmp/* && \  
apt-get purge -y -qq cmake wget cuda-core-9-0 git cuda-cudart-dev-9-0
libhwloc-dev libmicrohttpd-dev libssl-dev && \  
apt-get clean -qq  
  
COPY config.txt /usr/local/bin/  
COPY cpu.txt /usr/local/bin/  
COPY pools.txt /usr/local/bin/  
  
EXPOSE 8080  
ENTRYPOINT ["/usr/local/bin/xmr-stak"]

