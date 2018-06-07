FROM debian:buster-slim  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
gnuradio gnuradio-dev gr-osmosdr libvolk1.4 libvolk1-dev \  
cmake build-essential \  
python python-dev python-scipy swig \  
libboost-dev libcppunit-dev  
  
COPY . gr-iridium  
WORKDIR gr-iridium  
  
RUN mkdir build && cd build && cmake -D ENABLE_DOXYGEN=OFF ../ && make -j 2 &&
make install && ldconfig  
RUN mkdir -p /root/.gnuradio/prefs/ && \  
echo "gr::vmcircbuf_sysv_shm_factory" >
/root/.gnuradio/prefs/vmcircbuf_default_factory  
  
ENTRYPOINT ["iridium-extractor"]

