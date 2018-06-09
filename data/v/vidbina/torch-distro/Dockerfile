FROM ubuntu:trusty  
COPY . /tmp/torch  
RUN \  
cd /tmp/torch && \  
./install-deps && \  
./install.sh && \  
./clean.sh && \  
rm -rf /var/lib/apt/lists/* /var/tmp* /var/cache/apt/archives /tmp/OpenBLAS  

