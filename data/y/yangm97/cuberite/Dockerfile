FROM debian:stretch as builder  
  
WORKDIR /tmp  
  
RUN apt-get update && \  
apt-get install -y git gcc g++ cmake make && \  
rm -rf /var/lib/apt/lists/*  
  
COPY . .  
  
RUN cmake . -DCMAKE_BUILD_TYPE=RELEASE && \  
make -j 2  
  
FROM debian:stretch  
  
ENTRYPOINT ["cuberite"]  
WORKDIR /data  
  
# Healthcheck using mcstatus  
HEALTHCHECK \--timeout=3s CMD mcstatus localhost status || exit 1  
RUN apt-get update && \  
apt-get install -y --no-install-recommends python-pip python-setuptools && \  
pip install wheel && pip install mcstatus && \  
rm -rf /var/lib/apt/lists/* /root/*  
  
COPY \--from=builder /tmp/Server/Cuberite /usr/local/bin/cuberite  
COPY \--from=builder /tmp/Server/ /data/  
RUN rm -f /data/Cuberite  
  
# Bootstrap persistent volume with contents from Server folder (except for
binary)  
VOLUME /data  

